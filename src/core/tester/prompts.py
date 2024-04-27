#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

Copyright (C) 2023-2024 AliMirmohammad

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
import time
from utilis._regex.extractparam import replace_url_parameter
from src.logger.log import logger
from src.data import arg
from extras.logo import logo

def prompt_parameter(url=arg.url):
    """
    A function that gets the parameter of the given url.
    """
    _,param = replace_url_parameter(url,new_value=None)
    logger.info("testing if %s is injectable."%param)
    time.sleep(5)

def get_parameter(url=arg.url):
    """
    A function that gets the parameter of the given url.
    """
    _,param = replace_url_parameter(url,new_value=None)
    return param
try:
    parameter = get_parameter()
except:
    print(logo)
    print("Usage: {} sqlgo.py [options]".format("python"+str(sys.version_info.major)+"."+str(sys.version_info.minor)))
    logger.error("Missing mandatory arguments (-u/--url,--list-tamper,--update)\nExample usage: {} sqlgo.py -u http:/vulnweb.php?id=1 [other options]".format("python"+str(sys.version_info.major)+"."+str(sys.version_info.minor)))
    raise SystemExit


