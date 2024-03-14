#!/usr/bin/env python
"""
# SQLGO License - Version 1.3

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
try:
    from urllib.parse import urljoin
except:
    from urlparse import urljoin

from bs4 import BeautifulSoup as bs
from src.logger.log import logger
from src.data import arg
try:
    import requests
except:
    import third.requester as requests
from src.core.tester.vuln import vulnerable
import re
s = requests.session()

def getAllForms(url):
    """Given a `url`, it returns all forms from the HTML content"""
    soup = bs(requests.get(url,verify=False if arg.warningDisable else True).content, "html.parser")
    return soup.find_all("form")

def getFormDetails(form):
    """
    This function extracts all possible useful information about an HTML `form`
    """
    details = {}
    action = form.attrs.get("action", "").lower() if hasattr(form, 'attrs') else ""
    method = form.attrs.get("method", "get").lower() if hasattr(form, 'attrs') else ""
    inputs = []
    for input_tag in form.find_all("input") if hasattr(form, 'find_all') else []:
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")  # Handle the case where "value" is not present
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submitForm(form_details, url, value):
    if "http" not in arg.url:
        url = re.sub(r'^(?!http)(.+)', r'http://\1', url)
    
    if "https" not  in arg.url:
        url = re.sub(r'^(?!https)(.+)', r'https://\1',url)
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        data[input["name"]] = input["value"]

    logger.info("[+] Submitting malicious payload to %s"%target_url)
    logger.info("[+] Data: %s"%data)
    if form_details["method"] == "post":
        if "http" not in arg.url:
            target_url = re.sub(r'^(?!http)(.+)', r'http://\1', target_url)
        
        if "https" not  in arg.url:
            target_url = re.sub(r'^(?!https)(.+)', r'https://\1', target_url)
        return requests.post(target_url, data=data,verify=False if arg.warningDisable else True)
    else:
        if "http" not in arg.url:
            target_url = re.sub(r'^(?!http)(.+)', r'http://\1', target_url)
        
        if "https" not in arg.url:
            target_url = re.sub(r'^(?!https)(.+)', r'https://\1', target_url)
        return requests.get(target_url, params=data,verify=False if arg.warningDisable else True)

def scan_xss(url):
    forms = getAllForms(url)
    logger.info("[+] Detected %d forms on %s."%(len(forms),url))
    js_script = "<script>alert('hi')</script>"
    is_vulnerable = False
    for form in forms:
        form_details = getFormDetails(form)
        content = submitForm(form_details, url, js_script).content.decode()
        if js_script in content:
            logger.warning("[+] XSS Detected on %s"%url)
            logger.info("[*] Form details:")
            logger.info(form_details)
            is_vulnerable = True
    return is_vulnerable

res = None
def sqlInjectionBasicDetection(url):
    global res
    forms = getAllForms(url)
    print(len(forms))
    for form in forms:
        form_details = getFormDetails(form)
    
    for i in "\"'":
        data = {}
        for input_flag in form_details["inputs"]:
            if input_flag["type"] == "hidden" or input_flag["value"]:
                data[input_flag['name']] = input_flag.get("value", "") + i
            elif input_flag["type"] != "submit":
                data[input_flag["name"]] = "test%s" % i
    
    print(url)
    if form_details["method"] == "post":
        res = s.post(url, data=data)
    elif form_details["method"] == "get":
        res = s.get(url, params=data)
    
    if vulnerable(res):
        logger.info("basic tests shows that target %s might be injectable to sql injection."%url)
        return True
    else:
        logger.critical("basic tests shows that target: %s might not be injectable to sql injection."%url)

