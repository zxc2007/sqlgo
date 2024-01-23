

from sqlmap.lib.core.data import conf,kb
import os
import sys
sys.path.append(os.getcwd())
from plugins.dbms.mysql.connector import Connector

conf.dbmsUser = "root"
conf.dbmsPass = "alimirmohammad"
conf.hostname = "localhost"
conf.port = 3306
conf.dbmsDb = ""
conf.dbms = "mysql"
kb.timeout = 4
conf.timeout = 3
conf.dbmsHandler = "f"

x = Connector()
x.connect()
x.execute("USE ali;")
e = x.execute("SELECT * FROM employees;")
print(e)