import os
import sys
sys.path.append(os.getcwd())
import urllib.request
import re
import time
import urllib.parse
from lib.core.setting.setting import ALTER_SHELL_BASIC_COMMAND_INJECTION_PAYLOADS, WHITESPACES, IDENTIFIED_COMMAND_INJECTION, MULTI_TARGETS, SINGLE_WHITESPACE, TESTABLE_VALUE, INJECT_TAG, print_payload
from lib.core.payloads.unionpayload import union_payload
import traceback
import lib.core.setting.setting as settings
from utilis._regex.extractparam import replace_url_parameter
from lib.logger.log import logger
from lib.core.enums.payloads import Payload
from lib.core.payloads.errorb import error_based as error_based_payload
from lib.core.payloads.timebased import time_based_payload
from lib.core.payloads.substringpayload import sub_string_sql_inj
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
