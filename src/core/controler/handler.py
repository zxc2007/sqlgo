from urllib.parse import urlparse
import os
import sys
from _plugins.dbms.mysql.connector import Connector as MysqlConn
from _plugins.dbms.oracle.connector import Connector as OracleConn
from _plugins.dbms.sqlite.connector import Connector as SqliteCon

from src.core.parser.cmdline import *

from sqlmap.lib.core.data import conf,kb


conf.dbmsUser = dbms_user or ""
conf.dbmsPass = dbms_pass or ""
conf.hostname = urlparse(url).hostname
conf.port = 3306 if dbms == "mysql" and dbms is not None else ""
conf.dbmsDb = dbs or ""
conf.dbms = dbms or "mysql"
kb.timeout = dbs_timeout
conf.timeout = dbs_timeout
conf.dbmsHandler = "f"
def handle_dbms_connection():
    if conf.dbmsUser == "mysql" or dbms == "mysql":
        x = MysqlConn()
        x.connect()
        e = x.execute("SELECT * FROM employees;")
        print(e)
    
    elif conf.dbmsUser.lower() == "oracle":
        x = OracleConn()
        x.connect()
        e = x.execute("SELECT * FROM employees;")
        print(e)
    
    elif conf.dbmsUser.lower() == "sqlite":
        x = SqliteCon()
        x.connect()
        e = x.execute("SELECT * FROM employees;")
        print(e)
    
    
# handle_dbms_connection()