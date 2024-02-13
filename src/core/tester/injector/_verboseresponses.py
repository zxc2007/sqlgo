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
import os
import sys
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
    