#!/usr/bin/env python
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
try:
    import urllib.request
except:
    import urllib2 as urllib
try:
    import urllib.parse
except:
    import urlparse as urllib

import src.core.setting.setting as settings
from src.logger.log import logger
from src.core.tester.detector import sql_injection_basic_detection
from extras.bs4funs import get_form_from_response
from extras.bs4funs import *  # Import the missing function
from src.core.tester.XSSfuns import get_all_forms, get_form_details
import random
from extras.useragents import useragents

from colorama import Fore,init
from src.data import arg
import socket
import requests
from extras.logo import logo

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

try:
    _req = requests.get(arg.url)
    if arg.url is not None:
        crawler = Crawler(arg.url)
    else:
        print(logo)
        print()
        _msg = "No url has been set for sqlgo to test the injection\n"
        _msg += "\nEXITING!!!"
        logger.critical(_msg)
        raise SystemExit

except requests.exceptions.MissingSchema:
    print(logo)
    print()
    _msg = "No url has been set for sqlgo to test the injection,\n or having messing schema.make sure you include http://| https:// in url."
    _msg += "\nEXITING!!!"
    logger.critical(_msg)
    raise SystemExit

except UnicodeError:
    _msg = "entered domain is wrong or does not exists.please check your domain.\n"
    logger.critical(_msg)
    raise SystemExit

