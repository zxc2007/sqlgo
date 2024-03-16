#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

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
from enum import Enum
import os
import sys
from utilis.colorago.colorago import Fore

class Payload(Enum):
    UNION_ALL_SELECT = "'%s\033[2m\033[1mUNION all select MYSQL query\033[0m%s'"%(Fore.WHITE,Fore.RESET)
    MAKE_SET = "'%s\033[2m\033[1mMAKE SET MYSQL query\033[0m%s'"%(Fore.WHITE,Fore.RESET)
    SUBSTRING = "'%s\033[2m\033[1mSUBSTRING MYSQL query\033[0m%s'"%(Fore.WHITE,Fore.RESET)
    TIME_BASED = "'%s\033[2m\033[1mTIME BASED MYSQL query\033[0m%s'"%(Fore.WHITE,Fore.RESET)
    ERROR_BASED = "'%s\033[2m\033[1mERROR BASED MYSQL query\033[0m%s'"%(Fore.WHITE,Fore.RESET)
    MYSQL_BLIND_BASED = "'%s\033[2m\033[1mBLIND BASED MYSQL version query\033[0m%s'"%(Fore.WHITE,Fore.RESET)
    POSTGRE_SQL_VERSION_QUERY_BLIND_BASED = "'%s\033[2m\033[1mBLIND BASED POSTGRE SQL version query\033[0m%s'"%(Fore.WHITE,Fore.RESET)
    TIME_BASED_HEAVY_Q = "'%s\033[2m\033[1mTIME BASED HEAVY QUERY\033[0m%s'"%(Fore.WHITE,Fore.RESET)
    INLINE_Q = "'%s\033[2m\033[1mINLINE HEAVY QUERY\033[0m%s'"%(Fore.WHITE,Fore.RESET)
    ERROR_BOOL = "'%s\033[2m\033[1mERROR BOOLEAN HEAVY QUERY\033[0m%s'"%(Fore.WHITE,Fore.RESET)
    STACK_Q = "'%s\033[2m\033[1mSTACK HEAVY QUERY\033[0m%s'"%(Fore.WHITE,Fore.RESET)


