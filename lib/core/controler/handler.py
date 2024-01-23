from sqlmap.lib.core.data import conf,kb
from urllib.parse import urlparse
import os
import sys
sys.path.append(os.getcwd())
from plugins.dbms.mysql.connector import Connector as MysqlConn
from plugins.dbms.oracle.connector import Connector as OracleConn
from plugins.dbms.sqlite.connector import Connector as SqliteCon


def handle_dbms_connection():
    if conf.dbmsUser == "mysql":
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
    
    
handle_dbms_connection()