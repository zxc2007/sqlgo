#!/usr/bin/env python
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
    import sqlite3
except:
    pass

import logging

import os

from sqlmap.lib.core.common import getSafeExString
from sqlmap.lib.core.convert import getText
from sqlmap.lib.core.data import conf
from sqlmap.lib.core.data import logger
from sqlmap.lib.core.exception import SqlmapConnectionException
from sqlmap.lib.core.exception import SqlmapMissingDependence
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
    Homepage: http://pysqlite.googlecode.com/ and http://packages.ubuntu.com/quantal/python-sqlite
    User guide: http://docs.python.org/release/2.5/sqlmap.lib/module-sqlite3.html
    API: http://docs.python.org/library/sqlite3.html
    Debian package: python-sqlite (SQLite 2), python-pysqlite3 (SQLite 3)
    License: MIT

    Possible connectors: http://wiki.python.org/moin/SQLite
    """

    def __init__(self):
        GenericConnector.__init__(self)
        self.__sqlite = sqlite3

    def connect(self):
        self.initConnection()
        self.checkFileDb()

        try:
            self.connector = self.__sqlite.connect(database=self.db, check_same_thread=False, timeout=conf.timeout)

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
                    errMsg = "sqlmap requires 'python-sqlite' third-party library "
                    errMsg += "in order to directly connect to the database '%s'" % self.db
                    raise SqlmapMissingDependence(errMsg)

                self.__sqlite = sqlite
                self.connector = self.__sqlite.connect(database=self.db, check_same_thread=False, timeout=conf.timeout)
            except (self.__sqlite.DatabaseError, self.__sqlite.OperationalError) as ex:
                raise SqlmapConnectionException(getSafeExString(ex))

        self.initCursor()
        self.printConnected()

    def fetchall(self):
        try:
            return self.cursor.fetchall()
        except self.__sqlite.OperationalError as ex:
            logger.log(logging.WARN if conf.dbmsHandler else logging.DEBUG, "(remote) '%s'" % getSafeExString(ex))
            return None

    def execute(self, query):
        try:
            self.cursor.execute(getText(query))
        except self.__sqlite.OperationalError as ex:
            logger.log(logging.WARN if conf.dbmsHandler else logging.DEBUG, "(remote) '%s'" % getSafeExString(ex))
        except self.__sqlite.DatabaseError as ex:
            raise SqlmapConnectionException(getSafeExString(ex))

        self.connector.commit()

    def select(self, query):
        self.execute(query)
        return self.fetchall()
