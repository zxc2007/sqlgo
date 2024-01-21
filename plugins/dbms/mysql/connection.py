import os
import sys

sys.path.append(os.getcwd())

from plugins.dbms.mysql.connector import Connector

x = Connector()
x.connect()
x.execute("SELECT * FROM Users")
