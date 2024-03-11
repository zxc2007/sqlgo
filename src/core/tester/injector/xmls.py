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
import xml.etree.ElementTree as ET
import os
import sys
import glob
try:
    import requests
except:
    import third.requester as requests
from src.logger.log import logger
from src.core.payloadgen import loadPayloads
import src.core.setting.setting as settings
from extras.bs4funs import getFormFromResponse
from src.core.tester.XSSfuns import getAllForms,getFormDetails
from src.core.tester.detector import sqlInjectionBasicDetection
from src.core.tester.injector._requests import is_sql_injection_vulnerable
from src.core.parser.cmdline import level

class XML:
    class XMLALL:
        def __init__(self, url):
            loadPayloads()
            self.url = url
            self._cwd = os.getcwd()
            self._xml_all = glob.glob(self._cwd + "/data/xml/*.xml")
            self.__request = requests
            self.__headers = {'Content-Type': 'application/xml'}

        def _read_payload(self):
            for file in self._xml_all:
                with open(file, 'r') as f:
                    payload = f.read()
                    yield payload

        def parse_xml(self, xml_string):
            root = ET.fromstring(xml_string)
            logger.debug(xml_string)
            return xml_string

        def send_to_website(self):
            payloads = self._read_payload()
            for payload in payloads:
                xml_payload = self.parse_xml(payload)
                # Replace the URL with the actual endpoint you want to send the data to
                url = self.url
                response = self.__request.post(url, data=xml_payload, headers=self.__headers)

                if response.status_code == 200:
                    logger.info(settings.SUBMITTING_XML_INF_MSG%payload)
                    form_in_response = getFormFromResponse(response.text)
                    form_details = getFormDetails(form_in_response)
                    sqlInjectionBasicDetection(form_in_response, form_details)
                    logger.info("Successfully sent XML payload to the website.")
                    logger.debug("Response:%s"% response.text)  
                    if sqlInjectionBasicDetection(form_in_response, form_details) or level > 4:
                        logger.info("sql injections might exists in response")
                        if is_sql_injection_vulnerable(form_in_response, form_details):
                            logger.warning("sql injection vulnerability probably exists")
                        else:
                            logger.warning("sql injection might not certainly exists.")
                    
                else:
                    logger.error("failed")
                    logger.info("Response:%s"% response.text)  

# Instantiate the class and send XML payloads to the website




