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
    _SENDING = f"{formatted_time}[{Fore.BLUE}PAYLOAD{Fore.RESET}] code:"
    SENDING = _SENDING + "%s"

