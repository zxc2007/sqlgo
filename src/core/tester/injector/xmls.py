import xml.etree.ElementTree as ET
import os
import sys
import glob
import requests
from src.logger.log import logger
from src.core.payloadgen import loadPayloads
import src.core.setting.setting as settings
from extras.bs4funs import get_form_from_response
from src.core.tester.XSSfuns import get_all_forms,get_form_details
from src.core.tester.detector import sql_injection_basic_detection
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
                    form_in_response = get_form_from_response(response.text)
                    form_details = get_form_details(form_in_response)
                    sql_injection_basic_detection(form_in_response, form_details)
                    logger.info("Successfully sent XML payload to the website.")
                    logger.debug("Response:%s"% response.text)  
                    if sql_injection_basic_detection(form_in_response, form_details) or level > 4:
                        logger.info("sql injections might exists in response")
                        if is_sql_injection_vulnerable(form_in_response, form_details):
                            logger.warning("sql injection vulnerability probably exists")
                        else:
                            logger.warning("sql injection might not certainly exists.")
                    
                else:
                    logger.error(f"Failed to send XML payload. Status code: {response.status_code}")
                    logger.info("Response:%s"% response.text)  

# Instantiate the class and send XML payloads to the website




