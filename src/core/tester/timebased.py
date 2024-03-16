#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
import os
import sys
import re
import random
import string
from src.core.payloads.timebased import time_based_payload
from src.core.request.POSt.post import subber
from utilis._regex.extractparam import replace_url_parameter
from src.logger.log import logger
from src.datastruc.keygendict import Keygendict

def time_based():
    try:
        _dmsg = None
        _caps = Keygendict()
        _demerite = 0

        for payload in time_based_payload().split("\n"):
            subber.submit_data(payload)
            _caps.add_cap(key="Debug response:%d%s"%(random.randint(0,100,random.choice(string.ascii_letters))),value=subber.response)
            if re.search(r"HAVING[^ ]+\Z",subber.response):
                _dmsg = "Found HAVING for some values in html response."
                _caps.add_cap(key="HAVINGcap%s%d"%(random.choice(string.ascii_letters),random.randint(0,100)))
                _demerite +=1
                logger.debug(_dmsg)
            
            elif re.search(r"SELECT[^ ]+\Z",subber.response):
                _dmsg = "Found SELECT for some values in html response."
                _caps.add_cap(key="SELECTcap%s%d"%(random.choice(string.ascii_letters),random.randint(0,100)))
                logger.debug(_dmsg)
                _demerite +=1

    except Exception as e:
        logger.error(e)

