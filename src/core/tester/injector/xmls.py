import xml.etree.ElementTree as ET
import os
import sys
import glob
import requests
from src.logger.log import logger


class XML:
    class XMLreq_boolean_based:
        def __init__(self,url):
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
            # Process the XML data as needed
            # For example, logger.info the payload to the terminal
            logger.info(xml_string)
            # Send the XML payload to a website
            self.send_to_website(xml_string)

        def send_to_website(self, xml_payload):
            # Replace the URL with the actual endpoint you want to send the data to
            url = self.url
            response = self.__request.post(url, data=xml_payload, headers=self.__headers)

            if response.status_code == 200:
                logger.info("Successfully sent XML payload to the website.")
                logger.info("Response:", response.text)  # Print the website's response
            else:
                logger.info(f"Failed to send XML payload. Status code: {response.status_code}")
                logger.info("Response:", response.text)  # Print the website's response in case of failure

        def process_payloads(self):
            payloads = self._read_payload()
            for _payload in payloads:
                self.parse_xml(_payload)


