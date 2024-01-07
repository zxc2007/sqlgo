from lib.core.tester.injector._requests import *
from lib.core.parser.cmdline import url
import threading
import lib.core.setting.setting as settings


def make_set_injection_func():
    make_set_sql_injection(url)

def time_based_injection_func():
    time_based_inejction(url)

def host_injection_func():
    host_injection(url)

def error_based_INJECTION():
    error_based_injection(url)

def union_based_injection_function():
    union_based_injection(url)

def mysql_blind_based_function():
    mysql_blind_based_injection(url=url)

def postgre_sql_function():
    postgre_sql_blind_injection(url=url)

def crawler_threads():
    for payload in time_based_payload().split("\n"):
        for line in settings.INJECTABLE_ARES_ON_THE_FORM:
            referer_injection(url=url,payload=payload,vuln_parameter=line),
            user_agent_injection(url=url,payload=payload,vuln_parameter=line)
                





