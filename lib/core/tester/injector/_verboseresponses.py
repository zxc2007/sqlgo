import os
import sys
sys.path.append(os.getcwd())
from lib.core.tester.injector.injections import make_set_injection_func
from lib.core.tester.injector.injections import time_based_injection_func
from lib.core.tester.injector.injections import error_based_INJECTION
from lib.core.tester.injector.injections import union_based_injection_function
from lib.core.tester.injector.injections import mysql_blind_based_function
from lib.core.tester.injector.injections import postgre_sql_function
from lib.logger.log import logger
from lib.datastruc.magiclist import Magiclist



class Verbose:
    @staticmethod
    def verbose_response():
        _verboses = Magiclist()
        first = make_set_injection_func()
        sec = time_based_injection_func()
        third = error_based_INJECTION()
        fourth = union_based_injection_function()
        fifth = mysql_blind_based_function()
        sixth = postgre_sql_function()
        _verboses.append(first,sec,third,fourth,fifth,sixth)
        for _ in _verboses:
            logger.debug(_)
    