import os
import sys
import sqlite3
sys.path.append(os.getcwd())

from plugins.generic.connector import Connector as GenericConnector
from lib.logger.log import logger

class Connector(GenericConnector):
    """
    Homepage: http://pysqlite.googlecode.com/ and http://packages.ubuntu.com/quantal/python-sqlite
    User guide: http://docs.python.org/release/2.5/lib/module-sqlite3.html
    API: http://docs.python.org/library/sqlite3.html
    Debian package: python-sqlite (SQLite 2), python-pysqlite3 (SQLite 3)
    License: MIT

    Possible connectors: http://wiki.python.org/moin/SQLite
    """

    def __init__(self):
        GenericConnector.__init__(self)
        self.__sqlite = sqlite3

    def connect(self):
        self.initconnection()
        self.checkFileDb()

        try:
            self.connector = self.__sqlite.connect(database=self.db, check_same_thread=False, timeout=6)

            cursor = self.connector.cursor()
            cursor.execute("SELECT * FROM sqlite_master")
            cursor.close()

        except (self.__sqlite.DatabaseError, self.__sqlite.OperationalError):
            warnMsg = "unable to connect using SQLite 3 library, trying with SQLite 2"
            logger.warning(warnMsg)

            try:
                try:
                    import sqlite
                except ImportError:
                    errMsg = "sqlgo requires 'python-sqlite' third-party library "
                    errMsg += "in order to directly connect to the database '%s'" % self.db
                    raise errMsg

                self.__sqlite = sqlite
                self.connector = self.__sqlite.connect(database=self.db, check_same_thread=False, timeout=10)
            except (self.__sqlite.DatabaseError, self.__sqlite.OperationalError) as ex:
                raise ex

        self.init_cursor()
        self.print_connected()

    def fetchall(self):
        return self.cursor.fetchall()

        # try:
        #     return self.cursor.fetchall()
        # except self.__sqlite.OperationalError as ex:
        #     print(ex)
        #     logger.error(ex)
        #     return None

    def execute(self, query):
        try:
            self.connector = self.__sqlite.connect(self.db)
            self.cursor = self.connector.cursor()
            self.cursor.execute(query)
        except self.__sqlite.OperationalError as ex:
            logger.error(ex)
        except self.__sqlite.DatabaseError as ex:
            raise ex

        self.connector.commit()

    def select(self, query):
        self.execute(query)
        return self.fetchall()
    

con = Connector()
con.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT UNIQUE,
        birthdate DATE
    );
''')
f = con.execute("SELECT * FROM users;")
fet = con.fetchall()
print(fet)
