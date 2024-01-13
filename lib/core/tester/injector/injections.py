from lib.core.tester.injector._requests import *
from lib.core.parser.cmdline import url
import threading
import lib.core.setting.setting as settings


def make_set_injection_func():
    _ = make_set_sql_injection(url)
    return _

def time_based_injection_func():
    _ = time_based_inejction(url)
    return _

def host_injection_func():
    _ = host_injection(url)
    return _

def error_based_INJECTION():
    _ = error_based_injection(url)
    return _

def union_based_injection_function():
    _ = union_based_injection(url)
    return _

def mysql_blind_based_function():
    _ = mysql_blind_based_injection(url=url)
    return _

def postgre_sql_function():
    _ = postgre_sql_blind_injection(url=url)
    return _

def crawler_threads():
    for payload in time_based_payload().split("\n"):
        for line in settings.INJECTABLE_ARES_ON_THE_FORM:
            referer_injection(url=url,payload=payload,vuln_parameter=line),
            user_agent_injection(url=url,payload=payload,vuln_parameter=line)
                





