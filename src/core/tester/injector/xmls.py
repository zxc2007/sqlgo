import xml.etree.ElementTree as ET
import os
import sys
import glob
import requests
from src.logger.log import logger
from src.core.payloadgen import loadPayloads

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
            logger.info(xml_string)
            return xml_string

        def send_to_website(self):
            payloads = self._read_payload()
            for payload in payloads:
                xml_payload = self.parse_xml(payload)
                # Replace the URL with the actual endpoint you want to send the data to
                url = self.url
                response = self.__request.post(url, data=xml_payload, headers=self.__headers)

                if response.status_code == 200:
                    logger.info("Successfully sent XML payload to the website.")
                    logger.debug("Response:%s"% response.text)  
                else:
                    logger.info(f"Failed to send XML payload. Status code: {response.status_code}")
                    logger.info("Response:%s"% response.text)  

# Instantiate the class and send XML payloads to the website




