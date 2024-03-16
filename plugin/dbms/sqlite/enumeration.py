#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

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
from sqlmap.lib.core.data import logger
from sqlmap.lib.core.exception import SqlmapUnsupportedFeatureException
from sqlmap.plugins.generic.enumeration import Enumeration as GenericEnumeration

class Enumeration(GenericEnumeration):
    def getCurrentUser(self):
        warnMsg = "on SQLite it is not possible to enumerate the current user"
        logger.warning(warnMsg)

    def getCurrentDb(self):
        warnMsg = "on SQLite it is not possible to get name of the current database"
        logger.warning(warnMsg)

    def isDba(self, user=None):
        warnMsg = "on SQLite the current user has all privileges"
        logger.warning(warnMsg)

        return True

    def getUsers(self):
        warnMsg = "on SQLite it is not possible to enumerate the users"
        logger.warning(warnMsg)

        return []

    def getPasswordHashes(self):
        warnMsg = "on SQLite it is not possible to enumerate the user password hashes"
        logger.warning(warnMsg)

        return {}

    def getPrivileges(self, *args, **kwargs):
        warnMsg = "on SQLite it is not possible to enumerate the user privileges"
        logger.warning(warnMsg)

        return {}

    def getDbs(self):
        warnMsg = "on SQLite it is not possible to enumerate databases (use only '--tables')"
        logger.warning(warnMsg)

        return []

    def searchDb(self):
        warnMsg = "on SQLite it is not possible to search databases"
        logger.warning(warnMsg)

        return []

    def searchColumn(self):
        errMsg = "on SQLite it is not possible to search columns"
        raise SqlmapUnsupportedFeatureException(errMsg)

    def getHostname(self):
        warnMsg = "on SQLite it is not possible to enumerate the hostname"
        logger.warning(warnMsg)

    def getStatements(self):
        warnMsg = "on SQLite it is not possible to enumerate the SQL statements"
        logger.warning(warnMsg)

        return []
