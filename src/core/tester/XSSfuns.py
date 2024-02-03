import os
import sys
sys.path.append(os.getcwd())
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
from src.logger.log import logger
from src.core.parser.cmdline import url as _url
try:
    import thirdparty.requests as requests
except:
    import requests
from src.core.tester.vuln import vulnerable
import re
s = requests.session()

def get_all_forms(url):
    """Given a `url`, it returns all forms from the HTML content"""
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
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

def submit_form(form_details, url, value):
    if "http" not in _url:
        url = re.sub(r'^(?!http)(.+)', r'http://\1', url)
    
    if "https" not  in _url:
        url = re.sub(r'^(?!https)(.+)', r'https://\1',url)
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        data[input["name"]] = input["value"]

    logger.info(f"[+] Submitting malicious payload to {target_url}")
    logger.info(f"[+] Data: {data}")
    if form_details["method"] == "post":
        if "http" not in _url:
            target_url = re.sub(r'^(?!http)(.+)', r'http://\1', target_url)
        
        if "https" not  in _url:
            target_url = re.sub(r'^(?!https)(.+)', r'https://\1', target_url)
        return requests.post(target_url, data=data)
    else:
        if "http" not in _url:
            target_url = re.sub(r'^(?!http)(.+)', r'http://\1', target_url)
        
        if "https" not in _url:
            target_url = re.sub(r'^(?!https)(.+)', r'https://\1', target_url)
        return requests.get(target_url, params=data)

def scan_xss(url):
    forms = get_all_forms(url)
    logger.info(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script>alert('hi')</script>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            logger.warning(f"[+] XSS Detected on {url}")
            logger.info(f"[*] Form details:")
            logger.info(form_details)
            is_vulnerable = True
    return is_vulnerable

res = None
def sql_injection_basic_detection(url):
    global res
    forms = get_all_forms(url)
    print(len(forms))
    for form in forms:
        form_details = get_form_details(form)
    
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

