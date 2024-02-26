"""
# SQLGO License - Version 1.1

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
from src.core.payloads.substringpayload import sub_string_sql_inj as payload
from src.core.request.POSt.post import subber
from src.logger.log import logger
from src.core.enums.payloads import Payload
from src.datastruc.keygendict import Keygendict

def substring():
    _caps = Keygendict()
    _dmdg = None
    _demerite = 0
    for _payload in payload().split("\n"):
        subber.submit_data(_payload)
        logger.info("testing%s"%Payload.SUBSTRING.value)
        logger.debug(subber.response)
        _caps.add_cap(key="Debug response:%d%s"%(random.randint(0,100),random.choice(string.ascii_letters)),value=subber.response)
        if re.search(r"\bid",subber.response) or re.search(r"\wid",subber.response):
            _dmdg = "Found id for some values in html response."
            logger.debug(_dmdg)
            _caps.add_cap(key="IDcap%s%d"%(random.choice(string.ascii_letters),random.randint(0,100)))
            _demerite +=1
            
        
        elif re.search(r"SELECT[^ ]+\Z",subber.response):
            _dmdg = "Found SELECT for some values in html response."
            logger.debug(_dmdg)
            _caps.add_cap(key="SELECTcap%s%d"%(random.choice(string.ascii_letters),random.randint(0,100)))
            _demerite +=1
        
        elif re.search(pattern=r"ORDER BY[^ ]+\Z",string=subber.response,flags=re.IGNORECASE):
            _dmdg = "Found ORDER BY for some values in html response."
            logger.debug(_dmdg)
            _caps.add_cap(key="ORDERBYcap%s%d"%(random.choice(string.ascii_letters),random.randint(0,100)))
            _demerite +=1
        
        elif re.search(r"HAVING[^ ]+\Z",subber.response):
            _dmdg = "Found HAVING for some values in html response."
            logger.debug(_dmdg)
            _caps.add_cap(key="HAVINGcap%s%d"%(random.choice(string.ascii_letters),random.randint(0,100)))
            _demerite +=1

