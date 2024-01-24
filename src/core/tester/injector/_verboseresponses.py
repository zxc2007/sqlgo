import os
import sys
sys.path.append(os.getcwd())
from src.core.tester.injector.injections import make_set_injection_func
from src.core.tester.injector.injections import time_based_injection_func
from src.core.tester.injector.injections import error_based_INJECTION
from src.core.tester.injector.injections import union_based_injection_function
from src.core.tester.injector.injections import mysql_blind_based_function
from src.core.tester.injector.injections import postgre_sql_function
from src.logger.log import logger
from src.datastruc.magiclist import Magiclist
from src.core.enums.devstatus import DevStatus
from src.core.enums.priority import PRIORITY

__status__ = DevStatus.READY_FOR_PRODUCTION_AND_USE
__priority__ = PRIORITY.NORMAL



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
    