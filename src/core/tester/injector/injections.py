#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

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
from src.core.tester.injector._requests import *
from src.data import arg
import threading
import src.core.setting.setting as settings
import os
import sys
from src.core.enums.devstatus import DevStatus
from src.core.enums.priority import PRIORITY

__status__ = DevStatus.READY_FOR_PRODUCTION_AND_USE
__priority__ = PRIORITY.VERY_HIGH

def make_set_injection_func():
    """
    A function that used to gather all MAKE SET injection attacks
    Usage: mainExploit function @ gather.py file
    More info : https://github.com/HeisenbergCipherCracker/sqlgo/wiki/Injection-types 
    """
    _ = make_set_sql_injection(arg.url)
    return _

def time_based_injection_func():
    """
    A function that used to gather all time based injection attacks
    Usage: mainExploit function @ gather.py file
    More info : https://github.com/HeisenbergCipherCracker/sqlgo/wiki/Injection-types 
    """
    _ = time_based_inejction(arg.url)
    return _

def host_injection_func():
    """
    A function that used to gather all host based injection attacks
    Usage: mainExploit function @ gather.py file
    More info : https://github.com/HeisenbergCipherCracker/sqlgo/wiki/Injection-types 
    """
    _ = host_injection(arg.url)
    return _

def error_based_INJECTION():
    """
    A function that used to gather all error based injection attacks
    Usage: mainExploit function @ gather.py file
    More info : https://github.com/HeisenbergCipherCracker/sqlgo/wiki/Injection-types 
    """
    _ = error_based_injection(arg.url)
    return _

def union_based_injection_function():
    """
    A function that used to gather all union based injection attacks
    Usage: mainExploit function @ gather.py file
    More info : https://github.com/HeisenbergCipherCracker/sqlgo/wiki/Injection-types 
    """
    _ = union_based_injection(arg.url)
    return _

def mysql_blind_based_function():
    """
    A function that used to gather all mysql blind based injection attacks
    Usage: mainExploit function @ gather.py file
    More info : https://github.com/HeisenbergCipherCracker/sqlgo/wiki/Injection-types 
    """
    _ = mysql_blind_based_injection(url=arg.url)
    return _

def postgre_sql_function():
    """
    A function that used to gather all postgre blind based injection attacks
    Usage: mainExploit function @ gather.py file
    More info : https://github.com/HeisenbergCipherCracker/sqlgo/wiki/Injection-types 
    """
    _ = postgre_sql_blind_injection(url=arg.url)
    return _

def crawler_threads():
    """
    A function that used to gather all crawler based injection attacks
    Usage: mainExploit function @ gather.py file
    More info : https://github.com/HeisenbergCipherCracker/sqlgo/wiki/Injection-types 
    """
    for payload in time_based_payload().split("\n"):
        for line in settings.INJECTABLE_ARES_ON_THE_FORM:
            referer_injection(url=arg.url,payload=payload,vuln_parameter=line),
            user_agent_injection(url=arg.url,payload=payload,vuln_parameter=line)
                





