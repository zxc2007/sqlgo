"""
# SQLGO License - Version 1.3

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
    import cx_Oracle
except:
    pass

import logging
import os
import re

from sqlmap.lib.core.common import getSafeExString
from sqlmap.lib.core.convert import getText
from sqlmap.lib.core.data import conf
from sqlmap.lib.core.data import logger
from sqlmap.lib.core.exception import SqlmapConnectionException

os.environ["NLS_LANG"] = ".AL32UTF8"

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
    Homepage: https://oracle.github.io/python-cx_Oracle/
    User https://cx-oracle.readthedocs.io/en/latest/
    API: https://wiki.python.org/moin/DatabaseProgramming
    License: https://cx-oracle.readthedocs.io/en/latest/license.html#license
    """

    def connect(self):
        self.initConnection()
        self.__dsn = cx_Oracle.makedsn(self.hostname, self.port, self.db)
        self.__dsn = getText(self.__dsn)
        self.user = getText(self.user)
        self.password = getText(self.password)

        try:
            self.connector = cx_Oracle.connect(dsn=self.__dsn, user=self.user, password=self.password, mode=cx_Oracle.SYSDBA)
            logger.info("successfully connected as SYSDBA")
        except (cx_Oracle.OperationalError, cx_Oracle.DatabaseError, cx_Oracle.InterfaceError) as ex:
            if "Oracle Client library" in getSafeExString(ex):
                msg = re.sub(r"DPI-\d+:\s+", "", getSafeExString(ex))
                msg = re.sub(r': ("[^"]+")', r" (\g<1>)", msg)
                msg = re.sub(r". See (http[^ ]+)", r'. See "\g<1>"', msg)
                raise SqlmapConnectionException(msg)

            try:
                self.connector = cx_Oracle.connect(dsn=self.__dsn, user=self.user, password=self.password)
            except (cx_Oracle.OperationalError, cx_Oracle.DatabaseError, cx_Oracle.InterfaceError) as ex:
                raise SqlmapConnectionException(ex)

        self.initCursor()
        self.printConnected()

    def fetchall(self):
        try:
            return self.cursor.fetchall()
        except cx_Oracle.InterfaceError as ex:
            logger.log(logging.WARN if conf.dbmsHandler else logging.DEBUG, "(remote) '%s'" % getSafeExString(ex))
            return None

    def execute(self, query):
        retVal = False

        try:
            self.cursor.execute(getText(query))
            retVal = True
        except cx_Oracle.DatabaseError as ex:
            logger.log(logging.WARN if conf.dbmsHandler else logging.DEBUG, "(remote) '%s'" % getSafeExString(ex))

        self.connector.commit()

        return retVal

    def select(self, query):
        retVal = None

        if self.execute(query):
            retVal = self.fetchall()

        return retVal


