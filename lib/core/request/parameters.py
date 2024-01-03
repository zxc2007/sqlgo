import urllib.parse
import os
import sys
import re

sys.path.append(os.getcwd())
import lib.core.setting.setting as settings
from lib.checker.check import get_value_inside_boundaries

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

# print(vuln_GET_param("http://testfire.net/index.jsp?content=business_deposit.htm"))
