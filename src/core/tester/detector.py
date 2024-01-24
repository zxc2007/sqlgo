import requests
from bs4 import BeautifulSoup
import os
import sys
sys.path.append(os.getcwd())

res = None

from src.core.tester.vuln import *
from src.logger.log import logger
def sql_injection_basic_detection(form_soup, form_details):
    global res
    for i in "\"'":
        data = {}
        for input_flag in form_details["inputs"]:
            if input_flag["type"] == "hidden" or input_flag["value"]:
                data[input_flag['name']] = input_flag.get("value", "") + i
            elif input_flag["type"] != "submit":
                data[input_flag["name"]] = "test%s" % i
    
        if form_details["method"] == "post":
            res = requests.post(form_details["action"], data=data)
        elif form_details["method"] == "get":
            res = requests.get(form_details["action"], params=data)
        
        if vulnerable(res):
            logger.warning("Basic tests show that the target might be injectable to SQL injection.")
            return True
    
    logger.warning("Basic tests show that the target might not be injectable to SQL injection.")
    return False

# Example usage

