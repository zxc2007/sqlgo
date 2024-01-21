import os
import sys
sys.path.append(os.getcwd())
from plugins.generic.connector import Connector as GenericConnector
from lib.core.Exceptions.exceptions import SQLGOConnectionException
from lib.logger.log import logger
from lib.core.parser.cmdline import time_out as _timeout
import logging
try:
    import pymysql
except:
    pass


class Connector(GenericConnector):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def connect(self):
        self.initconnection()

        try:
            if self.connector is None:
                self.connector = pymysql.connect(
                    host=self.hostname,
                    user=self.user,
                    passwd=self.password,
                    db=self.db,
                    port=self.port,
                    connect_timeout=_timeout if _timeout is not None else 5,
                    use_unicode=True
                )
                print("Connection successful")  # Add this line for debugging
                self.init_cursor()  # Move the cursor initialization here
        except (pymysql.OperationalError, pymysql.InternalError, pymysql.ProgrammingError) as ex:
            raise SQLGOConnectionException(str(ex))

        self.print_connected()


    def fetchall(self):
        try:
            return self.cursor.fetchall()
        except pymysql.ProgrammingError as ex:
            logger.error(str(ex))
            return None

    def execute(self, query):
        retVal = False

        try:
            if self.cursor is None:
                self.init_cursor()
                self.connector = pymysql.connect(
                    host=self.hostname,
                    user=self.user,
                    passwd=self.password,
                    db=self.db,
                    port=self.port,
                    connect_timeout=5,
                    use_unicode=True
                )
            self.cursor = self.connector.cursor()
            _ = self.cursor.execute(query)
            retVal = str(_)
        except (pymysql.OperationalError, pymysql.ProgrammingError) as ex:
            logger.error(str(ex))
        except pymysql.InternalError as ex:
            raise SQLGOConnectionException(str(ex))

        self.connector.commit()

        return retVal

    def select(self, query):
        retVal = None

        if self.execute(query):
            retVal = self.fetchall()

        return retVal
