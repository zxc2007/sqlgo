#!/usr/bin/env python
"""
# SQLGO License - Version 1.1

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
import threading
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
from src.core.tester.injector._requests import user_agent_injection
from src.core.tester.injector.injections import crawler_threads
from src.core.tester.injector.vernosesresponses import Verbose
from src.core.parser.cmdline import dump
from src.datastruc.injectdict import extract_injection
from src.core.controler.handler import handle_dbms_connection
from src.core.tester.crawler import crawl as _crawl,kb
from src.core.testing import vulnTest
from src.core.sqlmapcommons import parseTargetDirect,conf,pushValue
from src.core.parser.cmdline import hydra
from src.core.tester.hydram import hydra_handler
from src.core.tester.injector.dump import dump_data_gather
from src.core.tester.injector._requests import stack_query
from src.core.tester.injector._requests import inline
from src.core.tester.injector._requests import error_boolean
from src.core.tester.injector._requests import time_based_heavy_q
from src.core.tester.injector._requests import sqlQuery
from src.data import arg


import urllib3
def gather_exploit():
    global xml
    if "?" not in arg.url:
        cr_msg = "No get parameters has been set for injection test.\n example: https://test.php?id=1"
        logger.critical(cr_msg)
        raise SystemExit
    
    if arg.install_dep:
        install_dependent()
        raise SystemExit
    if arg.warning_disable:
        urllib3.disable_warnings()
    try:
        test_connection()
        extract_cookies()
        prompt_parameter()
        basic_threads = [
            heuristic_injection_test_union_based(arg.url),
            heuristic_time_based_tests(arg.url),
            substring_heuristic_basic_injections(arg.url),
            error_based_heuristic_tests(arg.url),
            heuristic_time_based_tests(arg.url),
            make_set_url_replace(arg.url),
            time_based_url_replace(arg.url),
            error_based_url_replace(arg.url),
            union_based_url_replace(arg.url)
        ]

 
        for _thread_ in basic_threads:
            if not arg.skipBasic:
                _thread_ = threading.Thread(target=_thread_)
                _thread_.start()
                _thread_.join()
        
        if arg.hydra:
            hydra_handler.run_hydra()

        if arg.level >= 3:
            subber
            threads = [
                XSS(),
                make_set_injection_func(),
                time_based_injection_func(),
                error_based_INJECTION(),
                union_based_injection_function(),
                postgre_sql_function(),
                mysql_blind_based_function(),
                stack_query(arg.url),
                inline(arg.url),
                time_based_heavy_q(arg.url),
                error_boolean(arg.url),
                make_set_url_replace(arg.url),
                time_based_url_replace(arg.url),
                error_based_url_replace(arg.url),
                union_based_url_replace(arg.url),
                sqlQuery()
                
            ]
            if not arg.skipBasic:
                threads.append(
                union(),
                substring(),
                time_based(),
                error_based(),
                )
        if arg.dump:
            try:
                dump_data_gather()
            except (SystemExit,KeyboardInterrupt):
                pass
        


            thread_objects = []

            for thread_func in threads:
                _thread = threading.Thread(target=thread_func)
                _thread.start()
                thread_objects.append(_thread)

            # Wait for all threads to finish
            for _thread in thread_objects:
                _thread.join()
        
        if arg.level >= 4:
            threads = [
                injection_test_is_vuln_time_based(),
            ]
            if arg.dump:
                try:
                    threads.append(dump_data_gather())
                except (KeyboardInterrupt,SystemExit):
                    pass

            for _thread in threads:
                _thread = threading.Thread(target=_thread)
                _thread.start()
                _thread.join()
        if arg.crawl:
            crawler_threads()
            host_injection(arg.url)
            kb.targets = arg.url
            _crawl(arg.url)
        


        
        Verbose.verbose_response()
    
    except Exception as e:
        logger.debug(e)
        if any([isinstance(e,ConnectionResetError),"Connection reset by peer" in str(e),"[Errno 54] Connection reset by peer" in str(e)]):
            logger.warning("It looks like that the target has been closed the connection due to the harmful requests.please try using the proxy or vpn.")
            logger.critical("This can be a protection of WAF/IPS against harmful requests.")
        


