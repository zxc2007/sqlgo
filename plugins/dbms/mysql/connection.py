import os
import sys

sys.path.append(os.getcwd())

from plugins.dbms.mysql.connector import Connector
from lib.core.dumper.dump import dumper


def connect():
    x = Connector()
    x.connect()
    tb = x.execute("SELECT * FROM User")
    print(tb)

    dumper.DbTableCount({"table":tb})
    print("ff")
#sudo python plugins/dbms/mysql/connection.py
# python sqlgo.py -u http://localhost:3000/#/search?q=fe --port 3000 --dump
