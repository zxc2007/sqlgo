try:
    import pymysql
except:
    pass

import logging
import struct

from sqlmap.lib.core.common import getSafeExString
from sqlmap.lib.core.data import conf,kb
from sqlmap.lib.core.data import logger
from sqlmap.lib.core.exception import SqlmapConnectionException
import os


from sqlmap.lib.core.data import conf
from sqlmap.lib.core.data import logger
from sqlmap.lib.core.exception import SqlmapFilePathException
from sqlmap.lib.core.exception import SqlmapUndefinedMethod

class GenericConnector(object):
    """
    This class defines generic dbms protocol functionalities for plugins.
    """

    def __init__(self):
        self.connector = None
        self.cursor = None
        self.hostname = None

    def initConnection(self):
        self.user = conf.dbmsUser or ""
        self.password = conf.dbmsPass or ""
        self.hostname = conf.hostname
        self.port = conf.port
        self.db = conf.dbmsDb

    def printConnected(self):
        if self.hostname and self.port:
            infoMsg = "connection to %s server '%s:%d' established" % (conf.dbms, self.hostname, self.port)
            logger.info(infoMsg)

    def closed(self):
        if self.hostname and self.port:
            infoMsg = "connection to %s server '%s:%d' closed" % (conf.dbms, self.hostname, self.port)
            logger.info(infoMsg)

        self.connector = None
        self.cursor = None

    def initCursor(self):
        self.cursor = self.connector.cursor()

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connector:
                self.connector.close()
        except Exception as ex:
            logger.debug(ex)
        finally:
            self.closed()

    def checkFileDb(self):
        if not os.path.exists(self.db):
            errMsg = "the provided database file '%s' does not exist" % self.db
            raise SqlmapFilePathException(errMsg)

    def connect(self):
        errMsg = "'connect' method must be defined "
        errMsg += "inside the specific DBMS plugin"
        raise SqlmapUndefinedMethod(errMsg)

    def fetchall(self):
        errMsg = "'fetchall' method must be defined "
        errMsg += "inside the specific DBMS plugin"
        raise SqlmapUndefinedMethod(errMsg)

    def execute(self, query):
        errMsg = "'execute' method must be defined "
        errMsg += "inside the specific DBMS plugin"
        raise SqlmapUndefinedMethod(errMsg)

    def select(self, query):
        errMsg = "'select' method must be defined "
        errMsg += "inside the specific DBMS plugin"
        raise SqlmapUndefinedMethod(errMsg)


class Connector(GenericConnector):
    """
    Homepage: https://github.com/PyMySQL/PyMySQL
    User guide: https://pymysql.readthedocs.io/en/latest/
    Debian package: python3-pymysql
    License: MIT

    Possible connectors: http://wiki.python.org/moin/MySQL
    """

    def connect(self):
        self.initConnection()

        try:
            self.connector = pymysql.connect(host=self.hostname, user=self.user, passwd=self.password, db=self.db, port=self.port, connect_timeout=5, use_unicode=True)
        except (pymysql.OperationalError, pymysql.InternalError, pymysql.ProgrammingError, struct.error) as ex:
            raise SqlmapConnectionException(getSafeExString(ex))

        self.initCursor()
        self.printConnected()

    def fetchall(self):
        try:
            return self.cursor.fetchall()
        except pymysql.ProgrammingError as ex:
            logger.log(logging.WARN if conf.dbmsHandler else logging.DEBUG, "(remote) %s" % getSafeExString(ex))
            return None

    def execute(self, query):
        retVal = False

        try:
            self.cursor.execute(query)
            retVal = True
        except (pymysql.OperationalError, pymysql.ProgrammingError) as ex:
            logger.log(logging.WARN if conf.dbmsHandler else logging.DEBUG, "(remote) %s" % getSafeExString(ex))
        except pymysql.InternalError as ex:
            raise SqlmapConnectionException(getSafeExString(ex))

        self.connector.commit()

        return retVal

    def select(self, query):
        retVal = None

        if self.execute(query):
            retVal = self.fetchall()

        return retVal

# conf.dbmsUser = ""
# conf.dbmsPass = ""
# conf.hostname = "testfire.net"
# conf.port = 3306
# conf.dbmsDb = ""
# kb.timeout = 4

# from sqlmap.lib.core.data import conf,kb

# x = Connector()
# x.connect()