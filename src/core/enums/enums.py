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
from colorama import Fore,init
from enum import Enum
from datetime import datetime

init()


class DBMS(object):
    ACCESS = "Microsoft Access"
    DB2 = "IBM DB2"
    FIREBIRD = "Firebird"
    MAXDB = "SAP MaxDB"
    MSSQL = "Microsoft SQL Server"
    MYSQL = "MySQL"
    ORACLE = "Oracle"
    PGSQL = "PostgreSQL"
    SQLITE = "SQLite"
    SYBASE = "Sybase"
    INFORMIX = "Informix"
    HSQLDB = "HSQLDB"
    H2 = "H2"
    MONETDB = "MonetDB"
    DERBY = "Apache Derby"
    VERTICA = "Vertica"
    MCKOI = "Mckoi"
    PRESTO = "Presto"
    ALTIBASE = "Altibase"
    MIMERSQL = "MimerSQL"
    CLICKHOUSE = "ClickHouse"
    CRATEDB = "CrateDB"
    CUBRID = "Cubrid"
    CACHE = "InterSystems Cache"
    EXTREMEDB = "eXtremeDB"
    FRONTBASE = "FrontBase"
    RAIMA = "Raima Database Manager"
    VIRTUOSO = "Virtuoso"

class AUTOCOMPLETE_TYPE(object):
    SQL = 0
    OS = 1
    SQLMAP = 2
    API = 3

class PAYLOAD_SENDING(object):
    timestamp = "[2024-02-03 11:52:14.337308]"
    parsed_time = datetime.strptime(timestamp, "[%Y-%m-%d %H:%M:%S.%f]")
    formatted_time = parsed_time.strftime("[%Y-%m-%d %H:%M]")
    SENDING = "%s[%sPAYLOAD%s] code:{}" % (formatted_time, Fore.BLUE, Fore.RESET)
