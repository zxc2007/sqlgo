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
from lib.core.tester.injector.injections import make_set_injection_func,time_based_injection_func,host_injection,error_based_INJECTION

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
        threads = [
            union(),
            substring(),
            time_based(),
            error_based(),
            XSS(),
            make_set_injection_func(),
            time_based_injection_func(),
            error_based_INJECTION(),
        ]

        thread_objects = []

        for thread_func in threads:
            _thread = threading.Thread(target=thread_func)
            _thread.start()
            thread_objects.append(_thread)

        # Wait for all threads to finish
        for _thread in thread_objects:
            _thread.join()
    
    except Exception as e:
        logger.error(e)


