import threading
from lib.core.tester.maintestcheck import main_exploit
from lib.intruder.intruder import Intruder_substring,MakeSet
from lib.core.request.POSt.post import subber
from lib.core.tester.union import union
from lib.core.tester.substring import substring
from lib.logger.log import logger
from lib.core.tester.timebased import time_based
from lib.core.request.connection import test_connection
from lib.core.request.cookies.cookies import extract_cookies
from lib.core.tester.prompts import prompt_parameter
from lib.core.tester.errorb import error_based
from lib.core.XSS.xss import XSS
from lib.core.parser.cmdline import url
from lib.core.parser.cmdline import install_dep
from extra.installdep import install_dependent
from lib.core.parser.cmdline import warning_disable
from lib.core.tester.injector._requests import error_based_injection
from lib.core.tester.injector._requests import make_set_sql_injection
from lib.core.tester.injector.injections import make_set_injection_func
from lib.core.tester.injector.injections import time_based_inejction
from lib.core.tester.injector.injections import host_injection
from lib.core.tester.injector.injections import error_based_INJECTION
from lib.core.tester.injector.injections import time_based_injection_func
from lib.core.tester.injector.injections import postgre_sql_function
from lib.core.tester.injector.injections import mysql_blind_based_function
from lib.core.tester.injector.injections import union_based_injection_function
from lib.core.controler.controller import heuristic_injection_test_union_based
from lib.core.controler.controller import error_based_heuristic_tests
from lib.core.controler.controller import heuristic_time_based_tests
from lib.core.controler.controller import heuristic_time_based_tests
from lib.core.controler.controller import substring_heuristic_basic_injections
from lib.core.parser.cmdline import level
import lib.core.setting.setting as settings
from lib.core.tester.injector.timebased.tb_injector import injection_test_is_vuln_time_based
from lib.core.parser.cmdline import crawl
from lib.core.tester.useragentparam.useragent import crawler
from lib.core.tester.injector._requests import user_agent_injection

import urllib3
def gather_exploit():
    if install_dep:
        install_dependent()
        raise SystemExit
    if warning_disable:
        urllib3.disable_warnings()
    try:
        test_connection()
        extract_cookies()
        prompt_parameter()
        basic_threads = [
            heuristic_injection_test_union_based(url),
            heuristic_time_based_tests(url),
            substring_heuristic_basic_injections(url),
            error_based_heuristic_tests(url),
            heuristic_time_based_tests(url)
        ]
        for _thread_ in basic_threads:
            _thread_ = threading.Thread(target=_thread_)
            _thread_.start()
            _thread_.join()
        if level >= 3:
            subber
            threads = [
                union(),
                substring(),
                time_based(),
                error_based(),
                XSS(),
                make_set_injection_func(),
                time_based_injection_func(),
                error_based_INJECTION(),
                union_based_injection_function(),
                postgre_sql_function(),
                mysql_blind_based_function(),
                
            ]
        


            thread_objects = []

            for thread_func in threads:
                _thread = threading.Thread(target=thread_func)
                _thread.start()
                thread_objects.append(_thread)

            # Wait for all threads to finish
            for _thread in thread_objects:
                _thread.join()
        
        if level >= 4:
            threads = [
                injection_test_is_vuln_time_based()
            ]
            for _thread in threads:
                _thread = threading.Thread(target=_thread)
                _thread.start()
                _thread.join()
        
        if crawl:
            crawl_t = [
                user_agent_injection(url)
            ]
            for _threads_c in crawl_t:
                _threads_c = threading.Thread(target=_threads_c)
                _threads_c.start()
                _threads_c.join()
    
    except Exception as e:
        logger.debug(e)
        raise


