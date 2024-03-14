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
from sqlmap.lib.core.common import Backend
from sqlmap.lib.core.common import Format
from sqlmap.lib.core.data import conf
from sqlmap.lib.core.data import kb
from sqlmap.lib.core.data import logger
from sqlmap.lib.core.enums import DBMS
from sqlmap.lib.core.session import setDbms
from sqlmap.lib.core.settings import METADB_SUFFIX
from sqlmap.lib.core.settings import SQLITE_ALIASES
from sqlmap.lib.request import inject
from sqlmap.plugins.generic.fingerprint import Fingerprint as GenericFingerprint

class Fingerprint(GenericFingerprint):
    def __init__(self):
        GenericFingerprint.__init__(self, DBMS.SQLITE)

    def getFingerprint(self):
        value = ""
        wsOsFp = Format.getOs("web server", kb.headersFp)

        if wsOsFp:
            value += "%s\n" % wsOsFp

        if kb.data.banner:
            dbmsOsFp = Format.getOs("back-end DBMS", kb.bannerFp)

            if dbmsOsFp:
                value += "%s\n" % dbmsOsFp

        value += "back-end DBMS: "

        if not conf.extensiveFp:
            value += DBMS.SQLITE
            return value

        actVer = Format.getDbms()
        blank = " " * 15
        value += "active fingerprint: %s" % actVer

        if kb.bannerFp:
            banVer = kb.bannerFp.get("dbmsVersion")

            if banVer:
                banVer = Format.getDbms([banVer])
                value += "\n%sbanner parsing fingerprint: %s" % (blank, banVer)

        htmlErrorFp = Format.getErrorParsedDBMSes()

        if htmlErrorFp:
            value += "\n%shtml error message fingerprint: %s" % (blank, htmlErrorFp)

        return value

    def checkDbms(self):
        """
        References for fingerprint:

        * http://www.sqlite.org/lang_corefunc.html
        * http://www.sqlite.org/cvstrac/wiki?p=LoadableExtensions
        """

        if not conf.extensiveFp and Backend.isDbmsWithin(SQLITE_ALIASES):
            setDbms(DBMS.SQLITE)

            self.getBanner()

            return True

        infoMsg = "testing %s" % DBMS.SQLITE
        logger.info(infoMsg)

        result = inject.checkBooleanExpression("LAST_INSERT_ROWID()=LAST_INSERT_ROWID()")

        if result:
            infoMsg = "confirming %s" % DBMS.SQLITE
            logger.info(infoMsg)

            result = inject.checkBooleanExpression("SQLITE_VERSION()=SQLITE_VERSION()")

            if not result:
                warnMsg = "the back-end DBMS is not %s" % DBMS.SQLITE
                logger.warning(warnMsg)

                return False
            else:
                infoMsg = "actively fingerprinting %s" % DBMS.SQLITE
                logger.info(infoMsg)

                result = inject.checkBooleanExpression("RANDOMBLOB(-1)>0")
                version = '3' if result else '2'
                Backend.setVersion(version)

            setDbms(DBMS.SQLITE)

            self.getBanner()

            return True
        else:
            warnMsg = "the back-end DBMS is not %s" % DBMS.SQLITE
            logger.warning(warnMsg)

            return False

    def forceDbmsEnum(self):
        conf.db = "%s%s" % (DBMS.SQLITE, METADB_SUFFIX)
