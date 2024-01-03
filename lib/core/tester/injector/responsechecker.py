import os
import sys
import re
sys.path.append(os.getcwd())
from bs4 import BeautifulSoup
import thirdparty.requests as requests
from lib.logger.log import logger
from lib.core.tester.injector._requests import union_based_injection
import json

# form = union_based_injection("http://testfire.net/index.jsp?content=business_deposit.htm")


# def response_checker(form:BeautifulSoup):
#     inputs = []
#     print("checking!!!")
#     for input_tag in form.find_all("input"):
#         input_value = input_tag.get("value")
#         if input_value and re.search(r"(SELECT|UNION|INSERT|UPDATE|DELETE|DROP|CREATE)", input_value):
#             inputs.append(input_tag)
#             print("found area injectable!!!")
#             return 
        
#     print("no injectable area found")
#     return

# response_checker(form)