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
import re
import os
import sys
from src.core.Exceptions.exceptions import SQLgoNoParameterFoundException
from src.core.payloads.makesetsqlpayload import classify,_sorted
from utilis.colorago.colorago import Fore

def replace_url_parameter(url, new_value):
    """
    >>> url = "www.example.com?id=1&name=John&age=25"
    >>> new_value = input("Enter the new value: ")

    >>> replaced_url = replace_url_parameter(url, new_value)
    >>> print(replaced_url)
    NOTE: return would be url,parameter
    """
    pattern = r"(\?|\&)([^=]+)=[^&]*"
    replaced_url = re.sub(pattern, r"\1\2=%s"%new_value, url)
    extracted_value = re.search(pattern, url).group()
    if not replace_url_parameter:
        raise SQLgoNoParameterFoundException
    return replaced_url,Fore.BRIGHT_CYAN+str(extracted_value)+Fore.RESET






