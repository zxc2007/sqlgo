import threading
from src.core.tester.maintestcheck import main_exploit
from src.intruder.intruder import Intruder_substring,MakeSet
from src.core.request.POSt.post import subber
from src.core.tester.union import union
from src.core.tester.substring import substring
from src.logger.log import logger
from src.core.tester.timebased import time_based
from src.core.request.connection import test_connection
from src.core.request.cookies.cookies import extract_cookies
from src.core.tester.prompts import prompt_parameter
from src.core.tester.errorb import error_based
from src.core.XSS.xss import XSS
from src.core.parser.cmdline import url
from src.core.parser.cmdline import install_dep
from extras.installdep import install_dependent
from src.core.parser.cmdline import warning_disable
from src.core.tester.injector._requests import error_based_injection
from src.core.tester.injector._requests import time_based_url_replace
from src.core.tester.injector._requests import make_set_url_replace
from src.core.tester.injector._requests import error_based_url_replace
from src.core.tester.injector._requests import union_based_url_replace
from src.core.tester.injector._requests import make_set_sql_injection
from src.core.tester.injector.injections import make_set_injection_func
from src.core.tester.injector.injections import time_based_inejction
from src.core.tester.injector.injections import host_injection
from src.core.tester.injector.injections import error_based_INJECTION
from src.core.tester.injector.injections import time_based_injection_func
from src.core.tester.injector.injections import postgre_sql_function
from src.core.tester.injector.injections import mysql_blind_based_function
from src.core.tester.injector.injections import union_based_injection_function
from src.core.controler.controller import heuristic_injection_test_union_based
from src.core.controler.controller import error_based_heuristic_tests
from src.core.controler.controller import heuristic_time_based_tests
from src.core.controler.controller import heuristic_time_based_tests
from src.core.controler.controller import substring_heuristic_basic_injections
from src.core.parser.cmdline import level
import src.core.setting.setting as settings
from src.core.tester.injector.timebased.tb_injector import injection_test_is_vuln_time_based
from src.core.parser.cmdline import crawl
from src.core.tester.useragentparam.useragent import crawler
from src.core.tester.injector._requests import user_agent_injection
from src.core.tester.injector.injections import crawler_threads
from src.core.tester.injector.vernosesresponses import Verbose
from src.core.parser.cmdline import dump
from src.datastruc.injectdict import extract_injection
from src.core.controler.handler import handle_dbms_connection
from src.core.tester.crawler import crawl as _crawl,kb
from src.core.testing import vulnTest
from src.core.parser.cmdline import xml
from src.core.tester.injector.xmls import XML
from src.core.sqlmapcommons import parseTargetDirect,conf,pushValue
from src.core.parser.cmdline import hydra
from src.core.tester.hydram import hydra_handler
from sqlmap.lib.core.data import conf



import urllib3



def dump_actions():
    from foreign.bindinjection import main as run_further
    from foreign.accessinjection import main as dumper_injections

    run_further()
    dumper_injections()


def gather_exploit():
    global xml
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
            heuristic_time_based_tests(url),
            make_set_url_replace(url),
            time_based_url_replace(url),
            error_based_url_replace(url),
            union_based_url_replace(url)
        ]
        if conf.vuln:
            dump_actions()
 
        for _thread_ in basic_threads:
            _thread_ = threading.Thread(target=_thread_)
            _thread_.start()
            _thread_.join()
        
        if hydra:
            hydra_handler.run_hydra()

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
                make_set_url_replace(url),
                time_based_url_replace(url),
                error_based_url_replace(url),
                union_based_url_replace(url),
                
            ]
            if conf.vuln:
                dump_actions()
        


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
                injection_test_is_vuln_time_based(),
            ]
            vulnTest()

            vulnTest()
            for _thread in threads:
                _thread = threading.Thread(target=_thread)
                _thread.start()
                _thread.join()
        

        if dump:
            try:
                conf.direct = url
                pushValue(conf.direct)
                conf.direct = url
                parseTargetDirect()
                print(conf.dbmsPass)
                handle_dbms_connection()
            
            except Exception as e:
                logger.error("error occurred during connection to the database:%s"%str(e))
        
        if xml:
            xml = XML.XMLALL(url)
            xml.send_to_website()
            logger.info("testing xml data to the target: %s"%url)
            import sys
        if crawl:
            crawler_threads()
            host_injection(url)
            kb.targets = url
            _crawl(url)
        


        
        Verbose.verbose_response()
        # python sqlgo.py -u http://localhost:3000/#/search?q=fe --port 3000 --dump --username root --password alimirmohammad
        # extract_injection()
    
    except Exception as e:
        logger.debug(e)
        raise

#  python sqlgo.py -u http://testfire.net/index.jsp?content=business_deposit.htm --port 443 --dbms mysql --dbms-port 3306 --tamper space2plus 


