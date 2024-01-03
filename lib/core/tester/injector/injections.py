from lib.core.tester.injector._requests import *
from lib.core.parser.cmdline import url

def make_set_injection_func():
    make_set_sql_injection(url)

def time_based_injection_func():
    time_based_inejction(url)

def host_injection_func():
    host_injection(url)

def error_based_INJECTION():
    error_based_injection(url)






