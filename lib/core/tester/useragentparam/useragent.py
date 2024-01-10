import os
import sys
sys.path.append(os.getcwd())
import urllib.request
import urllib.parse
import lib.core.setting.setting as settings
from lib.logger.log import logger
from lib.core.tester.detector import sql_injection_basic_detection
from extra.bs4funs import get_form_from_response
from extra.bs4funs import *  # Import the missing function
from lib.core.tester.XSSfuns import get_all_forms, get_form_details
import random
from extra.useragents import useragents
from thirdparty.colorama import Fore,init
from lib.core.parser.cmdline import url as _url

init()

class Crawler:
    def __init__(self, url):
        self._useragent = useragents()
        self.url = url
        self._parsed_url = None
        self.headers = {settings.HTTP_HEADERS[0]: random.choice(settings.USER_AGENT_LIST)}
        self.request = urllib.request.Request(url)

    def _user_agent(self):
        pass

    def _user_agent_injection(self):
        if self._parsed_url is None:
            self._parsed_url = urllib.parse.urlparse(self.url)
            request = urllib.request.Request(self.url, headers=self.headers)
            response = urllib.request.urlopen(request)
            modified_url = response.geturl()
            return modified_url

    def user_agent_injection(self):
        form_in_response = get_form_from_response(self._user_agent_injection())
        form_details = get_form_details(form_in_response)
        _ = sql_injection_basic_detection(form_details=form_details,form_soup="")
        if _ is False:
            logger.warning(settings.CRAWLING_TESTS_SHOWS_THAT_PARAMETER_MIGHT_NOT_BE_INJECTABLE%settings.HTTP_HEADERS[0])
            return False
        
        logger.warning(settings.CRAWLING_SHOWS_THAT_PARAMETER_MIGHT_BE_INJECTABLE%settings.HTTP_HEADERS[0])
        return True
    
    def referer_parameter(self):
        refrer = self.request.get_header(settings.HTTP_HEADERS[1])
        if refrer:
            logger.warning(settings.CRAWLING_SHOWS_THAT_PARAMETER_MIGHT_BE_INJECTABLE%settings.HTTP_HEADERS[1])

            return True
        
        logger.warning(settings.CRAWLING_TESTS_SHOWS_THAT_PARAMETER_MIGHT_NOT_BE_INJECTABLE%settings.HTTP_HEADERS[1])
        logger.critical("Parameter was not found in the response.")
        return False
    
    
    
# Assuming the missing functions are defined somewhere in your project

# obj = Crawler("http://altoro.testfire.net/index.jsp?content=jobs/20061023.htm")
# obj.referer_parameter()

if _url is not None:
    crawler = Crawler(_url)
else:
    _msg = "No url has been set for sqlgo to test the injection\n"
    _msg += "\nEXITING!!!"
    logger.critical(_msg)
    raise SystemExit
