import os
import sys
import urllib.request
from urllib.parse import urljoin
import time
import urllib3
import urllib.parse
from urllib.parse import urlparse
sys.path.append(os.getcwd())
sys.path.insert(0,os.getcwd())
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
from lib.core.request.proxy.proxy import use_proxy,set_proxy
from lib.core.parser.cmdline import proxy_port
from lib.core.parser.cmdline import proxy_server
from lib.core.enums.payloads import Payload
from lib.core.parser.cmdline import user_proxy
from lib.core.payloads.blindbased import BlindBased
from tamper.maintamper import apply_tamper
from lib.core.parser.cmdline import tamper
from lib.core.tester.injector.checks import newline_fixation
from lib.core.tester.injector.parameters import get_url_part
from extra.averagetime import average_response
from lib.core.parser.cmdline import url as _url
from lib.datastruc.tree import root
from lib.datastruc.tree import Tree
from lib.core.parser.cmdline import beep
from lib.core.enums.devstatus import DevStatus
from lib.core.enums.priority import PRIORITY
from lib.datastruc.injectdict import injeciondict

__status__ = DevStatus.READY_FOR_PRODUCTION_AND_USE
__priority__ = PRIORITY.VERY_HIGH

def host_injection(url,vuln_parameter="", payload="" ):

    payload = urlparse(url).netloc + payload

    def inject_host(url, vuln_parameter, payload):

        http = urllib3.PoolManager()  
        logger.debug(settings.SESSION_HANDLER_CREATED%url)

        url = url.partition('?')[0]
        headers = {'Host': payload}

        try:
            response = http.request('GET', url, headers=headers)
            logger.debug(settings.RESPONSE_RECIEVED_FROM_HOST%url%response)
            return response.data.decode('utf-8')  
        except Exception as err_msg:
            return str(err_msg)

    try:
        response = inject_host(url, vuln_parameter, payload)
        logger.debug(settings.RESPONSE_SENT_TO_BE_INSPECTED_FOR_SQL_VULN%url)
    except Exception as err_msg:
        response = str(err_msg)

    return response

def error_based_injection(url,param=None,payload=True,isauto=True,addheader=True):
    try:
        _error_based = Tree("error_based")
        _content = None
        if isauto:
            if payload:
                for _payload in error_based().split("\n"):
                    request = urllib.request.Request(url,data=_payload.encode(),method=REQUESTS.POST)
                    response = urllib.request.urlopen(request)
                    logger.debug(settings.CONNECTION_ESTABLISHED_WITH_TARGET%url)
                    injeciondict.place = settings.ERROR_BASED_INJ_RESPONSE
                    injeciondict.parameter = str(response) if not isinstance(response,str) else response
                    if addheader:
                        try:
                            request.add_header(settings.CUSTOM_HEADER_NAME, settings.CUSTOM_HEADER_VALUE.replace(settings.TESTABLE_VALUE + settings.INJECT_TAG, settings.INJECT_TAG).replace(settings.INJECT_TAG, payload))
                            logger.debug(settings.HEADERS_ADDED_TO_THE_REQUEST)
                            response = urllib.request.urlopen(request,timeout=settings.DEFAULT_TIME_OUT)
                            _content = response.read()
                            _error_based.add_child(Tree(_content),Tree(response))
                        
                        except:
                            pass
                    
                    if user_proxy:
                        url_proxy = set_proxy(proxy_server,proxy_port)
                        result_use_general_proxy = use_proxy(request, proxy=url_proxy)
                        _content = result_use_general_proxy.read()
                        logger.debug(settings.USING_PRXOY%url_proxy)
                        _error_based.add_child(Tree(_content))


                    
                    else:
                        _content = response.read()
                        _error_based.add_child(str(Tree(_content if not isinstance(_content,bytes) else str(bytes.decode()))))
    
    except Exception as e:
        logger.debug(str(e))
        return

def time_based_inejction(url,payload=True,isauto=True):
    _ = 0
    _retval = None
    _time_based = Tree("time_based")

    try:
        forms = get_all_forms(url)

        for form in forms:
            form_data = {}
            for input_field in form.find_all('input'):
                form_data[input_field.get('name')] = input_field.get('value', '')
                logger.debug(settings.CTREATED_FROM_FOR_INJECTION%input_field)

            for _payload in time_based_payload().split("\n"):
                for line in settings.INJECTABLE_ARES_ON_THE_FORM:
                    _payload = apply_tamper(_payload if tamper is not None else None)
 

                    logger.debug(settings.TESTING_INJECTABLE_AREAS_ON_HTML_FORM%line)
                    form_data_copy = form_data.copy()
                    payload_field_name = line  
                    form_data_copy[payload_field_name] = _payload

                    # Make the POST request
                    request = urllib.request.Request(url, data=urllib.parse.urlencode(form_data_copy).encode(), method='POST')
                    response = urllib.request.urlopen(request)
                    logger.debug(settings.SENT_REQUEST_TO_TARGET%url)
                    injeciondict.place = settings.TIME_BASED_INJ_RESPONSE
                    injeciondict.parameter = str(response) if not isinstance(response,str) else response

                    response_content = response.read()
                    _time_based.add_child(Tree(response),Tree(response_content))


                    form_in_response = get_form_from_response(response_content)
                    form_details = get_form_details(form_in_response)
                    logger.debug(settings.READING_FORM_OF_HTML)

                    if is_sql_injection_vulnerable(response_content):
                        logger.warning("Potential sql injection detected!!!")
                        sql_injection_basic_detection(form_in_response, form_details)
                        logger.debug(settings.PERFORMING_SQL_INJECTION_DETECTION%url)
                    else:
                        if _ < 1:
                            logger.critical("No injectable areas found on the target")
                            sql_injection_basic_detection(form_in_response, form_details)
                            _ += 1



                    return form_in_response,_time_based

    except ValueError:
        pass

    except Exception as e:
        logger.debug(e)
        return



def is_sql_injection_vulnerable(response):
    try:
        # Decode the response content to string
        response_text = response.decode('utf-8')
        logger.debug(settings.DECODING_RESPONSE)
        error_keywords = ["error", "exception", "syntax", "mysql", "sql", "warning"]
        return any(keyword in response_text.lower() for keyword in error_keywords)
    except Exception as e:
        print(f"Error decoding response: {str(e)}")
        return False

def make_set_sql_injection(url,random_header=False):
    _retval = None
    _make_set = Tree("make_set")
    _ = 0
    try:
        url = get_url_part(url=url)
        forms = get_all_forms(url)
        logger.debug(settings.CTREATED_FROM_FOR_INJECTION%forms)

        for form in forms:
            form_data = {}
            for input_field in form.find_all('input'):
                form_data[input_field.get('name')] = input_field.get('value', '')
                logger.debug(settings.GOT_INPUT_FIELD%input_field)

            for _payload in make_set_sql_payload().split("\n"):
                _payload = apply_tamper(_payload if tamper is not None else None)
                logger.info("testing %s"%Payload.MAKE_SET.value)
                for line in settings.INJECTABLE_ARES_ON_THE_FORM:
                    form_data_copy = form_data.copy()
                    payload_field_name = line  
                    form_data_copy[payload_field_name] = _payload
                    logger.debug(settings.SUBMITED_PAYLOAD_ON_FORM%_payload)

                    request = urllib.request.Request(url, data=urllib.parse.urlencode(form_data_copy).encode(), method='POST')
                    if random_header is True:
                        if settings.CUSTOM_HEADER_INJECTION:
                            logger.debug(settings.PREAPARING_HEADERS)
                            custom_header_name = settings.CUSTOM_HEADER_NAME
                            custom_header_value = settings.CUSTOM_HEADER_VALUE

                            if custom_header_name and custom_header_value:
                                request.add_header(custom_header_name, custom_header_value)
                            else:
                                logger.info("Skipping invalid header name or value.")
                        else:
                            logger.warning("header injection disabled.")



                    response = urllib.request.urlopen(request)
                    logger.debug(settings.SENT_REQUEST_TO_TARGET%url)
                    injeciondict.place = settings.MAKE_SET_INJ_RESPONSE
                    injeciondict.parameter = str(response) if not isinstance(response,str) else response
                    response_content = response.read()
                    _make_set.add_child(Tree(response))

                    form_in_response = get_form_from_response(response_content)
                    form_details = get_form_details(form_in_response)
                    logger.debug(settings.READING_FORM_OF_HTML+settings.CRAFTING_FORM_IN_DETAILS)

                    if is_sql_injection_vulnerable(response_content):
                        logger.warning("Potential SQL injection detected!!!")
                        sql_injection_basic_detection(form_in_response, form_details)
                        logger.debug(settings.PERFORMING_SQL_INJECTION_DETECTION+"sql injection vulnerability already exists in the url %s"%url)
                    else:
                        if _ < 1:
                            logger.critical("No SQL injection detected on the target")
                            logger.debug("using payload:%s"%_payload)
                            _ += 1

                return form_in_response,_make_set
                    
    
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return
        # Handle the exception as needed


def union_based_injection(url):
    _ = 0
    _tamreq = None
    _tresponse = None
    _retval = None
    _union_based = Tree("union_based")
    for __ in union_payload().split("\n"):
        try:
            forms = get_all_forms(url)
            logger.debug(settings.CTREATED_FROM_FOR_INJECTION%""+"testing possible parameters on the received form.")
            for form in forms:
                form_data = {}
                for input_field in form.find_all('input'):
                    form_data[input_field.get('name')] = input_field.get('value', '')
                for _payload in union_payload().split("\n"):

                    for line in settings.INJECTABLE_ARES_ON_THE_FORM:
                        _payload = apply_tamper(_payload if tamper is not None else None)

                        logger.info(f"testing {Payload.UNION_ALL_SELECT.value}")
                        form_data_copy = form_data.copy()
                        payload_field_name = line  
                        form_data_copy[payload_field_name] = _payload
                        logger.debug(settings.TESTING_INJECTABLE_AREAS_ON_HTML_FORM%_payload)

                        # Make the POST request
                        request = urllib.request.Request(url, data=urllib.parse.urlencode(form_data_copy).encode(), method='POST')
                        response = urllib.request.urlopen(request)

                        logger.debug(settings.SENT_REQUEST_TO_TARGET%url)
                        injeciondict.place = settings.UNION_BASED_INJ_RESPONSE
                        injeciondict.parameter = str(response) if not isinstance(response,str) else response
                        logger.debug(settings.CRAFTED_REQUEST_TO_BE_SENT%url)

                        response_content = response.read()
                        _union_based.add_child(Tree(response_content),Tree(response))

                        form_in_response = get_form_from_response(response_content)
                        form_details = get_form_details(form_in_response)
                        sql_injection_basic_detection(form_in_response, form_details)

                        if is_sql_injection_vulnerable(response_content):
                            if beep:
                                __import__("extra.beep.beep")
                            logger.warning("Potential sql injection detected!!!")
                            # Call sql_injection_basic_detection with both parameters
                            sql_injection_basic_detection(form_in_response, form_details)
                        else:
                            logger.debug("No injectable areas found on the target via payload%s"%_payload)
                            sql_injection_basic_detection(form_in_response, form_details)
                    
                    return _union_based
                




                # return form_in_response

        except ValueError:
            continue

        except Exception as e:
            logger.error(e)
            return


def mysql_blind_based_injection(url):
    _ = 0
    _retval = None
    _blind_based = Tree("blind_based")
    for __ in BlindBased.mysql_version_query().split("\n"):
        try:
            forms = get_all_forms(url)
            logger.debug(settings.CRAFTING_FORM_IN_DETAILS+"created form of html from target %s"%url)
            for form in forms:
                logger.debug(settings.INCLUDING_FORMS%form)
                form_data = {}
                for input_field in form.find_all('input'):
                    form_data[input_field.get('name')] = input_field.get('value', '')
                for _payload in BlindBased.mysql_version_query().split("\n"):
                    for line in settings.INJECTABLE_ARES_ON_THE_FORM:
                        logger.info(f"testing {Payload.MYSQL_BLIND_BASED.value}")
                        form_data_copy = form_data.copy()
                        logger.debug("copied the data form %s"%form_data_copy)
                        payload_field_name = line 
                        form_data_copy[payload_field_name] = _payload
                        logger.debug(settings.TESTING_INJECTABLE_AREAS_ON_HTML_FORM%line)

                        # Make the POST request
                        request = urllib.request.Request(url, data=urllib.parse.urlencode(form_data_copy).encode(), method='POST')
                        response = urllib.request.urlopen(request)

                        logger.debug(settings.SENT_REQUEST_TO_TARGET%url)
                        injeciondict.place = settings.BLIND_BASED_INJ_RESPONSE
                        injeciondict.parameter = str(response) if not isinstance(response,str) else response

                        response_content = response.read()
                        _blind_based.add_child(Tree(response_content))


                        form_in_response = get_form_from_response(response_content)
                        form_details = get_form_details(form_in_response)
                        sql_injection_basic_detection(form_in_response, form_details)

                        if is_sql_injection_vulnerable(response_content):
                            if beep:
                                __import__("extra.beep.beep")
                            logger.debug(settings.PERFORMING_SQL_INJECTION_DETECTION%url)
                            logger.warning("Potential sql injection detected!!!")
                            sql_injection_basic_detection(form_in_response, form_details)
                        else:
                            logger.debug("No injectable areas found on the target via payload%s"%_payload)
                            sql_injection_basic_detection(form_in_response, form_details)
                    
                    return _blind_based

                # return form_in_response

        except ValueError:
            continue

        except Exception as e:
            logger.debug(e)
            return

def postgre_sql_blind_injection(url):
    _ = 0
    _retval = None
    _postgre = Tree("postgre")
    for __ in BlindBased.postgre_sql_payload_version_query().split("\n"):
        try:
            forms = get_all_forms(url)

            for form in forms:
                form_data = {}
                for input_field in form.find_all('input'):
                    form_data[input_field.get('name')] = input_field.get('value', '')
                for _payload in BlindBased.postgre_sql_payload_version_query().split("\n"):
                    for line in settings.INJECTABLE_ARES_ON_THE_FORM:
                        _payload = apply_tamper(_payload if tamper is not None else None)

                        logger.info(f"testing {Payload.POSTGRE_SQL_VERSION_QUERY_BLIND_BASED.value}")
                        form_data_copy = form_data.copy()
                        payload_field_name = line  # Replace with the actual name
                        form_data_copy[payload_field_name] = _payload
                        logger.debug(settings.TESTING_INJECTABLE_AREAS_ON_HTML_FORM%_payload)

                        # Make the POST request
                        request = urllib.request.Request(url, data=urllib.parse.urlencode(form_data_copy).encode(), method='POST')
                        response = urllib.request.urlopen(request)

                        logger.debug(settings.SENT_REQUEST_TO_TARGET%url)
                        injeciondict.place = settings.POSTGRE_RESPONSE_IN_INJ_DICT
                        injeciondict.parameter = str(response) if not isinstance(response,str) else response

                        response_content = response.read()
                        _postgre.add_child(Tree(response_content))
                        logger.debug(settings.SENT_POST_REQUEST%url)

                        form_in_response = get_form_from_response(response_content)
                        form_details = get_form_details(form_in_response)
                        sql_injection_basic_detection(form_in_response, form_details)
                        logger.debug("inspecting injection on %s"%form_details)
                        if is_sql_injection_vulnerable(response_content):
                            if beep:
                                __import__("extra.beep.beep")
                            logger.warning("Potential sql injection detected!!!")
                            # Call sql_injection_basic_detection with both parameters
                            sql_injection_basic_detection(form_in_response, form_details)
                        else:
                            logger.debug("No injectable areas found on the target via payload%s"%_payload)
                            sql_injection_basic_detection(form_in_response, form_details)
                    
                    return _postgre
                




                # return form_in_response

        except ValueError:
            continue

        except Exception as e:
            logger.error(e)
            return

def user_agent_injection(url, vuln_parameter, payload):
    _responses = []
    def inject_user_agent(url, vuln_parameter, payload):
        nonlocal _responses
        logger.info(settings.TESTING_IF_CRAWLING_PARAMETER_IS_INJECTABLE%"User-agent")

        request = urllib.request.Request(url)
        url = get_url_part(url)
        request = urllib.request.Request(url)
        payload = newline_fixation(payload)
        request.add_header('User-Agent', payload)
        try:
            response = urllib.request.urlopen(request, timeout=settings.TIMEOUT)
            logger.debug(settings.CRAWLING_TEST_RESPONSE%str(response))
        except ValueError:
            pass

    if settings.TIME_RELATIVE_ATTACK or True:
        start = 0
        end = 0
        start = time.monotonic()

    try:
        response = inject_user_agent(url, vuln_parameter, payload)
    except Exception as err_msg:
        response = str(err_msg)
        logger.debug(response)

    if settings.TIME_RELATIVE_ATTACK:
        end = time.monotonic()
        how_long = float(end - start)
        _responses.append(how_long)
        _avres = average_response(_responses)
        return how_long,_avres

    else:
        return response


def referer_injection(url, vuln_parameter, payload):
    if settings.REFERER_INJECTION is not None:
        logger.info(settings.REFERER_INJECTION)
    _responses = []
    def inject(url, vuln_parameter, payload):
        nonlocal _responses
        logger.info(settings.TESTING_IF_CRAWLING_PARAMETER_IS_INJECTABLE%"Referer")

        request = urllib.request.Request(url)
        url = get_url_part(url)
        request = urllib.request.Request(url)
        payload = newline_fixation(payload)
        request.add_header("Referer", payload)
        try:
            response = urllib.request.urlopen(request, timeout=settings.TIMEOUT)
            logger.debug(settings.CRAWLING_TEST_RESPONSE%str(response))
        except ValueError:
            pass

    if settings.TIME_RELATIVE_ATTACK or True:
        start = 0
        end = 0
        start = time.monotonic()

    try:
        response = inject(url, vuln_parameter, payload)
    except Exception as err_msg:
        response = str(err_msg)
        logger.info(response if response is not None else "")

    if settings.TIME_RELATIVE_ATTACK:
        end = time.monotonic()
        how_long = float(end - start)
        _responses.append(how_long)
        _avres = average_response(_responses)
        return how_long,_avres

    else:
        return response
# from lib.core.parser.cmdline import crawl 

# crawl = True
# for payload in time_based_payload().split("\n"):
#     print(user_agent_injection("http://testfire.net/index.jsp?content=business_deposit.htm","id",payload))
# make_set_sql_injection("http://testfire.net/index.jsp?content=business_deposit.htm")