import os
import sys
import urllib.parse
import urllib.request
import re
import time
sys.path.append(os.getcwd())
import lib.core.setting.setting as settings
from lib.core.request.parameters import vuln_GET_param
from lib.core.payloads.timebased import time_based_payload
from lib.core.parser.cmdline import url as _url
from lib.logger.log import logger
import lib.core.setting.setting as settings
from lib.core.enums.payloads import Payload as P_type
from utilis.colorago.resetor import reset_tested_payload

def injection_test(payload, url, http_request_method="POST"):

    start = 0
    end = 0
    start = time.monotonic()

    if not settings.USER_DEFINED_POST_DATA:

        vuln_parameter = vuln_GET_param(url)
        target = url.replace(settings.TESTABLE_VALUE + settings.INJECT_TAG, settings.INJECT_TAG).replace(settings.INJECT_TAG, payload)
        request = urllib.request.Request(target)

    else:
        #parameter = urllib.parse.unquote(parameter)
        # Check if its not specified the 'INJECT_HERE' tag
        parameter = ''.join(str(e) for e in parameter).replace("+","%2B")
        # Define the vulnerable parameter
        # Define the POST data
        if settings.IS_JSON:
            data = parameter.replace(settings.TESTABLE_VALUE + settings.INJECT_TAG, settings.INJECT_TAG).replace(settings.INJECT_TAG, urllib.parse.unquote(payload.replace("\"", "\\\"")))
            try:
                pass
            except ValueError:
                pass
        elif settings.IS_XML:
            data = parameter.replace(settings.TESTABLE_VALUE + settings.INJECT_TAG, settings.INJECT_TAG).replace(settings.INJECT_TAG, urllib.parse.unquote(payload))
        else:
            data = parameter.replace(settings.TESTABLE_VALUE + settings.INJECT_TAG, settings.INJECT_TAG).replace(settings.INJECT_TAG, payload)
            request = urllib.request.Request(url, data.encode(settings.DEFAULT_CODEC))

    # Check if defined extra headers.
    # Get the response of the request
    response = urllib.request.urlopen(request)
    response = response.read()

    end  = time.monotonic()
    how_long = float(end - start)
    return (how_long, vuln_parameter)



def injection_test_is_vuln_time_based(url=_url):
    _retval = None
    _inj = None
    _imsg = None
    if settings.USER_SKIPPED_ADVANCED_TIME_BASED_TESTS is True:
        _imsg = "User skipped the other tests for the target"
        logger.info(_imsg)
        return
    for _payload in time_based_payload().split("\n"):
        _inj = injection_test(payload=_payload,url=url)
        assert isinstance(_inj,tuple), tuple(_inj)
        logger.debug(settings.TESTING_TIME_BASED_ADVANCED_AGAINST%url)
        logger.debug(settings.TESTING_TIME_BASED_PAYLOAD%_payload)
        logger.info("testing %s"%P_type.TIME_BASED.value)
        if _inj[0] > settings.ADVANCED_TIME_BASED_TRESHOLD:
            logger.info(settings.ADVANCED_TESTS_SHOWS_THAT_TARGET_MIGHT_BE_INJECTABLE%(url,reset_tested_payload(_payload))+"\n Do you want to skip the further testing for the target %s (Y,n)?"%url)
            _ = input("")
            if _.lower() == "y":
                settings.USER_SKIPPED_ADVANCED_TIME_BASED_TESTS = True
                return
            elif _.lower() == "n":
                settings.USER_SKIPPED_ADVANCED_TIME_BASED_TESTS = False
            
            else:
                pass


# "http://testphp.vulnweb.com/artists.php?artist=1"
    
# print(injection_test_is_vuln_time_based("http://testphp.vulnweb.com/artists.php?artist=1"))