import xml.etree.ElementTree as ET
import os
import sys
import glob
import requests



class XML:
    class XMLreq_boolean_based:
        def __init__(self,url):
            self._cwd = os.getcwd()
            self._xml_all = glob.glob(self._cwd + "/data/xml/*.xml")
            self.url = url

        def _read_payload(self):
            for file in self._xml_all:
                with open(file, 'r') as f:
                    payload = f.read()
                    yield payload

        def parse_xml(self, xml_string):
            root = ET.fromstring(xml_string)
            # Process the XML data as needed
            # For example, print the payload to the terminal
            return xml_string

        def process_payloads(self):
            payloads = self._read_payload()
            for _payload in payloads:
                self.parse_xml(_payload)
        


