import os
import sys
import urllib.request
from urllib.parse import urljoin

import urllib3
import urllib.parse
from urllib.parse import urlparse
sys.path.append(os.getcwd())
from lib.core.payloads.errorb import error_based
from lib.core.setting.setting import REQUESTS
import lib.core.setting.setting as settings
from lib.core.payloads.makesetsqlpayload import make_set_sql_payload
from lib.core.payloads.timebased import time_based_payload
from lib.core.payloads.unionpayload import union_payload
from lib.logger.log import logger
from lib.core.tester.XSSfuns import get_form_details
from lib.core.tester.detector import sql_injection_basic_detection 
import traceback
from lib.core.tester.XSSfuns import get_all_forms
from lib.core.tester.XSSfuns import get_form_details,submit_form
from extra.bs4funs import get_form_from_response
from lib.core.request.parameters import get_url_part
from lib.core.request.agent import header

def host_injection(vuln_parameter, payload, url):

    payload = urlparse(url).netloc + payload

    def inject_host(url, vuln_parameter, payload):

        http = urllib3.PoolManager()  # Use PoolManager to manage connections

        url = url.partition('?')[0]
        headers = {'Host': payload}

        try:
            response = http.request('GET', url, headers=headers)
            return response.data.decode('utf-8')  # Convert bytes to string
        except Exception as err_msg:
            return str(err_msg)

    try:
        response = inject_host(url, vuln_parameter, payload)
    except Exception as err_msg:
        response = str(err_msg)

    return response

def error_based_injection(url,param=None,payload=True,isauto=True,addheader=True):
    try:
        _content = None
        if isauto:
            if payload:
                for _payload in error_based().split("\n"):
                    request = urllib.request.Request(url,data=_payload.encode(),method=REQUESTS.POST)
                    response = urllib.request.urlopen(request)
                    if addheader:
                        request.add_header(settings.CUSTOM_HEADER_NAME, settings.CUSTOM_HEADER_VALUE.replace(settings.TESTABLE_VALUE + settings.INJECT_TAG, settings.INJECT_TAG).replace(settings.INJECT_TAG, payload))
                        response = urllib.request.urlopen(request,timeout=settings.DEFAULT_TIME_OUT)
                        _content = response.read()
                        return _content

                    
                    else:
                        _content = response.read()
                        return _content
    
    except Exception as e:
        logger.error(str(e))
        traceback.print_exc()

def time_based_inejction(url,payload=True,isauto=True):
    _retval = None

    try:
        forms = get_all_forms(url)

        for form in forms:
            form_data = {}
            for input_field in form.find_all('input'):
                form_data[input_field.get('name')] = input_field.get('value', '')

            for _payload in time_based_payload().split("\n"):
                form_data_copy = form_data.copy()
                payload_field_name = 'username'  # Replace with the actual name
                form_data_copy[payload_field_name] = _payload

                # Make the POST request
                request = urllib.request.Request(url, data=urllib.parse.urlencode(form_data_copy).encode(), method='POST')
                response = urllib.request.urlopen(request)

                response_content = response.read()

                form_in_response = get_form_from_response(response_content)
                form_details = get_form_details(form_in_response)

                if is_sql_injection_vulnerable(response_content):
                    logger.warning("Potential sql injection detected!!!")
                    # Call sql_injection_basic_detection with both parameters
                    sql_injection_basic_detection(form_in_response, form_details)
                else:
                    logger.critical("No injectable areas found on the target")
                    sql_injection_basic_detection(form_in_response, form_details)


                return form_in_response

    except ValueError:
        pass

    except Exception as e:
        logger.error(e)
        traceback.print_exc()




def is_sql_injection_vulnerable(response):
    try:
        # Decode the response content to string
        response_text = response.decode('utf-8')

        # Customize this function based on the characteristics of a vulnerable response
        # For simplicity, it just checks if the response contains an error message
        error_keywords = ["error", "exception", "syntax", "mysql", "sql", "warning"]
        return any(keyword in response_text.lower() for keyword in error_keywords)
    except Exception as e:
        print(f"Error decoding response: {str(e)}")
        return False

def make_set_sql_injection(url,random_header=False):
    _retval = None
    try:
        url = get_url_part(url=url)
        forms = get_all_forms(url)

        for form in forms:
            form_data = {}
            for input_field in form.find_all('input'):
                form_data[input_field.get('name')] = input_field.get('value', '')

            for _payload in make_set_sql_payload().split("\n"):
                form_data_copy = form_data.copy()
                payload_field_name = 'username'  # Replace with the actual name
                form_data_copy[payload_field_name] = _payload

                request = urllib.request.Request(url, data=urllib.parse.urlencode(form_data_copy).encode(), method='POST')
                if random_header is True:
                    if settings.CUSTOM_HEADER_INJECTION:
                        custom_header_name = settings.CUSTOM_HEADER_NAME
                        custom_header_value = settings.CUSTOM_HEADER_VALUE

                        if custom_header_name and custom_header_value:
                            request.add_header(custom_header_name, custom_header_value)
                        else:
                            print("Skipping invalid header name or value.")
                    else:
                        logger.warning("header injection disabled.")



                response = urllib.request.urlopen(request)

                response_content = response.read()

                form_in_response = get_form_from_response(response_content)
                form_details = get_form_details(form_in_response)

                if is_sql_injection_vulnerable(response_content):
                    logger.warning("Potential SQL injection detected!!!")
                    # Call sql_injection_basic_detection with both parameters
                    sql_injection_basic_detection(form_in_response, form_details)
                else:
                    logger.critical("No SQL injection detected on the target")
                    logger.debug("using payload:%s"%_payload)
                    
    
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        traceback.print_exc()
        # Handle the exception as needed





# make_set_sql_injection("http://testfire.net/index.jsp?content=business_deposit.htm",random_header=True)