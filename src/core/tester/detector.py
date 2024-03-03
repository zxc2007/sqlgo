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
try:
    import requests
except:
    import third.requester as requests
from bs4 import BeautifulSoup
import os
import sys

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
            try:
                res = requests.post(form_details["action"], data=data)
            except:
                pass
        elif form_details["method"] == "get":
            res = requests.get(form_details["action"], params=data)
        
        if vulnerable(res):
            logger.warning("Basic tests show that the target might be injectable to SQL injection.")
            return True
    
    return False

# Example usage

