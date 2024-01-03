from lib.core.tester.injector._requests import *
from lib.core.parser.cmdline import url

def make_set_injection_func():
    return make_set_sql_injection(url)

def time_based_injection_func():
    return time_based_inejction(url)

def host_injection():
    return host_injection(url)

def error_based_INJECTION():
    return error_based_injection(url)






