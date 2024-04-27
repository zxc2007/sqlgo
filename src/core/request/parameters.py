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
try:
    import urllib.parse
except:
    import urlparse as urllib
import os
import sys
import re

import src.core.setting.setting as settings
from src.checker.check import get_value_inside_boundaries

def get_url_part(url):
    o = urllib.parse.urlparse(url)
    url_part = o.scheme + "://" + o.netloc + o.path
    return url_part

def vuln_GET_param(url):
    # Define the vulnerable parameter
    if "?" not in url:
        # Grab the value of parameter.
        value = re.findall(r'/(.)/' + settings.INJECT_TAG + "", url)
        value = ''.join(value)
        vuln_parameter = re.sub(r"/(.)/", "", value)
    elif (re.search(r"\?(.)=[^\S]*(\/)*" + re.escape(settings.INJECT_TAG), url) or
          re.search(r"&(.)=[^\S]*(\/)*" + re.escape(settings.INJECT_TAG), url)):
        pairs = url.split("?")[1].split(settings.PARAMETER_DELIMITER)
        for param in range(0, len(pairs)):
            if settings.INJECT_TAG in pairs[param]:
                vuln_parameter = pairs[param].split("=")[0]
                if settings.WILDCARD_CHAR_APPLIED:
                    try:
                        settings.POST_WILDCARD_CHAR = pairs[param].split("=")[1].split(settings.INJECT_TAG)[1]
                    except Exception:
                        pass
                settings.TESTABLE_VALUE = pairs[param].split("=")[1].replace(settings.INJECT_TAG, "")
                if re.search(settings.VALUE_BOUNDARIES, settings.TESTABLE_VALUE) and settings.INJECT_INSIDE_BOUNDARIES:
                    settings.TESTABLE_VALUE = get_value_inside_boundaries(settings.TESTABLE_VALUE)
                if settings.BASE64_PADDING in pairs[param]:
                    settings.TESTABLE_VALUE = settings.TESTABLE_VALUE + settings.BASE64_PADDING
                break
    else:
        vuln_parameter = url

    return vuln_parameter


def get_parameter_sections(url):
    o = urllib.parse.urlparse(url)
    url_part = o.scheme + "://" + o.netloc + o.path
    return url_part





