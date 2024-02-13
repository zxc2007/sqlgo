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
import urllib.request
import requests
import re
import time
import urllib.parse
from src.core.setting.setting import ALTER_SHELL_BASIC_COMMAND_INJECTION_PAYLOADS, WHITESPACES, IDENTIFIED_COMMAND_INJECTION, MULTI_TARGETS, SINGLE_WHITESPACE, TESTABLE_VALUE, INJECT_TAG, print_payload
from src.core.payloads.unionpayload import union_payload
import traceback
import src.core.setting.setting as settings
from utilis._regex.extractparam import replace_url_parameter
from src.logger.log import logger
from src.core.enums.payloads import Payload
from src.core.payloads.errorb import error_based as error_based_payload
from src.core.payloads.timebased import time_based_payload
from src.core.payloads.substringpayload import sub_string_sql_inj
from src.core.common.urlreplace import update_url
from src.core.tester.XSSfuns import get_form_details,submit_form
from extras.bs4funs import get_form_from_response
from src.core.parser.cmdline import verbose
from src.core.tester.XSSfuns import get_all_forms
from src.core.tester.XSSfuns import get_form_details
from src.core.tester.detector import sql_injection_basic_detection 
from src.core.tester.injector._requests import is_sql_injection_vulnerable
from tampers.maintamper import apply_tamper
from src.core.parser.cmdline import tamper
from src.core.enums.enums import PAYLOAD_SENDING
from src.core.payloads.errorb import error_based

def heuristic_injection_test_union_based(url):
    _verbose = 0
    payload = None
    _msg = None
    __ = 0
    basic_payloads = ALTER_SHELL_BASIC_COMMAND_INJECTION_PAYLOADS
    WHITESPACE = WHITESPACES[0]
    
    try:
        for _payload in union_payload().split("\n"):
            logger.info("testing %s"%Payload.UNION_ALL_SELECT.value)
            if not IDENTIFIED_COMMAND_INJECTION or MULTI_TARGETS:
                payload = urllib.parse.quote(_payload)
                payload = payload.replace(SINGLE_WHITESPACE, WHITESPACE)
                if _verbose >= 1:
                    print(print_payload(payload))
                    print(payload)
                
                data = payload
                tmp_url = url.replace(TESTABLE_VALUE + INJECT_TAG, INJECT_TAG).replace(INJECT_TAG, payload)
                
                try:
                    request = urllib.request.Request(tmp_url, data.encode())
                    response = urllib.request.urlopen(request)
                    _data = response.read().decode()
                    if re.search(settings.UNION_BASED_VULN_RETURNS,_data):
                        if __< 1:
                            __+= 1
                        _,param = replace_url_parameter(url,new_value=None)
                        _msg = "heuristic tests shows that parameter %s might be vulnerable to union based sql injection."%param
                        _msg +="\n you can skip the rest of the tests for the vulnerabilities if you wish."
                        logger.info(_msg)
                        time.sleep(3)
                    
                    else:
                        if __ < 1:
                            __ += 1
                            _,param = replace_url_parameter(url,new_value=None)
                            _msg = "heuristic tests shows that parameter %s might not be vulnerable to union based sql injection."%param
                            _msg +="\n you can skip the rest of the tests for the vulnerabilities if you wish."
                            logger.warning(_msg)
                            time.sleep(3)
                    # print(_data)
                except urllib.error.URLError as e:
                    print(f"URLError: {e.reason}")
                except urllib.error.HTTPError as e:
                    print(f"HTTPError: {e.code}")
    
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()

def error_based_heuristic_tests(url):
    _verbose = 0
    payload = None
    _msg = None
    __ = 0
    basic_payloads = ALTER_SHELL_BASIC_COMMAND_INJECTION_PAYLOADS
    WHITESPACE = WHITESPACES[0]
    
    try:
        for _payload in error_based_payload().split("\n"):
            logger.info("testing %s"%Payload.ERROR_BASED.value)
            if not IDENTIFIED_COMMAND_INJECTION or MULTI_TARGETS:
                payload = urllib.parse.quote(_payload)
                payload = payload.replace(SINGLE_WHITESPACE, WHITESPACE)
                if _verbose >= 1:
                    print(print_payload(payload))
                    print(payload)
                
                data = payload
                tmp_url = url.replace(TESTABLE_VALUE + INJECT_TAG, INJECT_TAG).replace(INJECT_TAG, payload)
                
                try:
                    request = urllib.request.Request(tmp_url, data.encode())
                    response = urllib.request.urlopen(request)
                    _data = response.read().decode()
                    if re.search(settings.UNION_BASED_VULN_RETURNS,_data):
                        if __< 1:
                            __+= 1
                        _,param = replace_url_parameter(url,new_value=None)
                        _msg = "heuristic tests shows that parameter %s might be vulnerable to union based sql injection."%param
                        _msg +="\n you can skip the rest of the tests for the vulnerabilities if you wish."
                        logger.info(_msg)
                        time.sleep(3)
                    
                    else:
                        if __ < 1:
                            __ += 1
                            _,param = replace_url_parameter(url,new_value=None)
                            _msg = "heuristic tests shows that parameter %s might not be vulnerable to error based sql injection."%param
                            _msg +="\n you can skip the rest of the tests for the vulnerabilities if you wish."
                            logger.warning(_msg)
                            time.sleep(3)
                    # print(_data)
                except urllib.error.URLError as e:
                    print(f"URLError: {e.reason}")
                except urllib.error.HTTPError as e:
                    print(f"HTTPError: {e.code}")
    
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()


def heuristic_time_based_tests(url):
    _verbose = 0
    payload = None
    _msg = None
    __ = 0
    basic_payloads = ALTER_SHELL_BASIC_COMMAND_INJECTION_PAYLOADS
    WHITESPACE = WHITESPACES[0]
    
    try:
        for _payload in time_based_payload().split("\n"):
            logger.info("testing %s"%Payload.TIME_BASED.value)
            if not IDENTIFIED_COMMAND_INJECTION or MULTI_TARGETS:
                payload = urllib.parse.quote(_payload)
                payload = payload.replace(SINGLE_WHITESPACE, WHITESPACE)
                if _verbose >= 1:
                    print(print_payload(payload))
                    print(payload)
                
                data = payload
                tmp_url = url.replace(TESTABLE_VALUE + INJECT_TAG, INJECT_TAG).replace(INJECT_TAG, payload)
                
                try:
                    request = urllib.request.Request(tmp_url, data.encode())
                    response = urllib.request.urlopen(request)
                    _data = response.read().decode()
                    if re.search(settings.UNION_BASED_VULN_RETURNS,_data):
                        if __< 1:
                            __+= 1
                        _,param = replace_url_parameter(url,new_value=None)
                        _msg = "heuristic tests shows that parameter %s might be vulnerable to time based sql injection."%param
                        _msg +="\n you can skip the rest of the tests for the vulnerabilities if you wish."
                        logger.info(_msg)
                        time.sleep(3)
                    
                    else:
                        if __ < 1:
                            __ += 1
                            _,param = replace_url_parameter(url,new_value=None)
                            _msg = "heuristic tests shows that parameter %s might not be vulnerable to union based sql injection."%param
                            _msg +="\n you can skip the rest of the tests for the vulnerabilities if you wish."
                            logger.warning(_msg)
                            time.sleep(3)
                    # print(_data)
                except urllib.error.URLError as e:
                    print(f"URLError: {e.reason}")
                except urllib.error.HTTPError as e:
                    print(f"HTTPError: {e.code}")
    
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()


def substring_heuristic_basic_injections(url):
    _verbose = 0
    payload = None
    _msg = None
    __ = 0
    basic_payloads = ALTER_SHELL_BASIC_COMMAND_INJECTION_PAYLOADS
    WHITESPACE = WHITESPACES[0]
    
    try:
        for _payload in sub_string_sql_inj().split("\n"):
            logger.info("testing %s"%Payload.SUBSTRING.value)
            if not IDENTIFIED_COMMAND_INJECTION or MULTI_TARGETS:
                payload = urllib.parse.quote(_payload)
                payload = payload.replace(SINGLE_WHITESPACE, WHITESPACE)
                if _verbose >= 1:
                    print(print_payload(payload))
                    print(payload)
                
                data = payload
                tmp_url = url.replace(TESTABLE_VALUE + INJECT_TAG, INJECT_TAG).replace(INJECT_TAG, payload)
                
                try:
                    request = urllib.request.Request(tmp_url, data.encode())
                    response = urllib.request.urlopen(request)
                    _data = response.read().decode()
                    if re.search(settings.UNION_BASED_VULN_RETURNS,_data):
                        if __< 1:
                            __+= 1
                        _,param = replace_url_parameter(url,new_value=None)
                        _msg = "heuristic tests shows that parameter %s might be vulnerable to substring based sql injection."%param
                        _msg +="\n you can skip the rest of the tests for the vulnerabilities if you wish."
                        logger.info(_msg)
                        time.sleep(3)
                    
                    else:
                        if __ < 1:
                            __ += 1
                            _,param = replace_url_parameter(url,new_value=None)
                            _msg = "heuristic tests shows that parameter %s might not be vulnerable to union based sql injection."%param
                            _msg +="\n you can skip the rest of the tests for the vulnerabilities if you wish."
                            logger.warning(_msg)
                            time.sleep(3)
                    # print(_data)
                except urllib.error.URLError as e:
                    print(f"URLError: {e.reason}")
                except urllib.error.HTTPError as e:
                    print(f"HTTPError: {e.code}")
    
    except Exception as e:
        logger.debug(e)
        traceback.print_exc()


# heuristic_injection_test_union_based("http://testfire.net/index.jsp?content=business_deposit.htm")
