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
try:
    from urllib.parse import urlparse
except:
    import urlparse
    
import os
import sys
from plugin.dbms.mysql.connector import Connector as MysqlConn
from plugin.dbms.oracle.connector import Connector as OracleConn
from plugin.dbms.sqlite.connector import Connector as SqliteCon
from src.core.dumper.dump import dumper
from extras.extracttablenames import read_common_tables as common_tables
from src.core.parser.cmdline import *

from sqlmap.lib.core.data import conf,kb

try:
    conf.dbmsUser = dbms_user or ""
    conf.dbmsPass = dbms_pass or ""
    conf.hostname = urlparse(url).hostname
    conf.port = 3306 if dbms == "mysql" and dbms is    not None else ""
    conf.dbmsDb = dbs or ""
    conf.dbms = dbms or "mysql"
    kb.timeout = dbs_timeout
    conf.timeout = dbs_timeout
    conf.dbmsHandler = "f"

    comn_table = common_tables()
except:
    pass
def handle_dbms_connection():
    global comn_table
    for _ in comn_table:
        print("attacking")
        for table in _:
            if conf.dbmsUser == "mysql" or dbms == "mysql":
                x = MysqlConn()
                x.connect()
                e = x.execute("SELECT * FROM %s;"%table)
                return e
            
            elif conf.dbmsUser.lower() == "oracle":
                x = OracleConn()
                x.connect()
                e = x.execute("SELECT * FROM %s;"%table)
                return e
            
            elif conf.dbmsUser.lower() == "sqlite":
                x = SqliteCon()
                x.connect()
                e = x.execute("SELECT * FROM %s;"%table)
                return e
    
    
# handle_dbms_connection()