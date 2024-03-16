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
from src.core.payloads.unionpayload import union_payload
from src.core.request.POSt.post import subber
from src.logger.log import logger
from utilis._regex.extractparam import replace_url_parameter
from src.data import arg
from src.core.enums.payloads import Payload
from src.datastruc.keygendict import Keygendict
import src.core.setting.setting as settings


def union():
    for payload in union_payload().split("\n"):
        try:
            _infomsg = None
            msg = None
            _testmsg = None
            subber.submit_data(payload)
            logger.debug(subber.response)
            _testmsg = "testing: %s"%Payload.UNION_ALL_SELECT.value
            logger.info(_testmsg)
        except (ConnectionResetError,ConnectionRefusedError,
                ConnectionAbortedError,ConnectionError) as exc:
            errmsg = "It looks like the server is not responding to the requests,or the WAF/IPS is dropping the requests.please use proxy for more efficiency while sending requests."
            logger.error(errmsg)
            logger.debug(str(exc)) 
            break
        try:
            if re.search(r"ORDER BY [^ ]+\Z",subber.response):
                msg = "ORDER BY"
                msg += "founded in the response"
                logger.debug(msg)
                _infomsg = "Some ORDER BY statement weaknesses leaked in the response"
                logger.info(_infomsg)
                logger.debug(settings.ORDER_BY_PARAMETER)
            
            elif re.search(r"SELECT * [^ ]+\Z",subber.response):
                msg = "SELECT *"
                msg += "founded in the response"
                logger.debug(msg)
                _infomsg = "Some possible SELECT statement leaks in the response"
                logger.info(_infomsg)
                logger.debug(settings.SELECT_PARAMETER_FOUND)
            
            elif re.search(r"\bid",subber.response):
                _pattern = re.search(r"\bid",subber.response)
                index = _pattern.end()
                words_after = re.findall(r"\b\w+\b", subber.response[index:index+100])
                logger.info(words_after)
                logger.debug(settings.ID_PARAMETER)
        except KeyboardInterrupt:
            logger.info("Canceled by user,making the way to the other payloads")
    

def union_man():
    for payload in union_payload().split("\n"):
        rep = (replace_url_parameter(url=arg.url,new_value=payload))
        logger.info(rep[0])
    

