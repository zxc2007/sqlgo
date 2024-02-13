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
import re
from bs4 import BeautifulSoup
try:
    import thirdparty.requests as requests
except:
    pass
from src.logger.log import logger
from src.core.tester.injector._requests import union_based_injection
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