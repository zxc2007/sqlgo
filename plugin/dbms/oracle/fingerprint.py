#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

Copyright (C) 2023-2024 AliMirmohammad

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
import re

from sqlmap.lib.core.common import Backend
from sqlmap.lib.core.common import Format
from sqlmap.lib.core.data import conf
from sqlmap.lib.core.data import kb
from sqlmap.lib.core.data import logger
from sqlmap.lib.core.enums import DBMS
from sqlmap.lib.core.session import setDbms
from sqlmap.lib.core.settings import ORACLE_ALIASES
from sqlmap.lib.request import inject
from sqlmap.plugins.generic.fingerprint import Fingerprint as GenericFingerprint

class Fingerprint(GenericFingerprint):
    def __init__(self):
        GenericFingerprint.__init__(self, DBMS.ORACLE)

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
            value += DBMS.ORACLE
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
        if not conf.extensiveFp and Backend.isDbmsWithin(ORACLE_ALIASES):
            setDbms(DBMS.ORACLE)

            self.getBanner()

            return True

        infoMsg = "testing %s" % DBMS.ORACLE
        logger.info(infoMsg)

        # NOTE: SELECT LENGTH(SYSDATE)=LENGTH(SYSDATE) FROM DUAL does
        # not work connecting directly to the Oracle database
        if conf.direct:
            result = True
        else:
            result = inject.checkBooleanExpression("LENGTH(SYSDATE)=LENGTH(SYSDATE)")

        if result:
            infoMsg = "confirming %s" % DBMS.ORACLE
            logger.info(infoMsg)

            # NOTE: SELECT NVL(RAWTOHEX([RANDNUM1]),[RANDNUM1])=RAWTOHEX([RANDNUM1]) FROM DUAL does
            # not work connecting directly to the Oracle database
            if conf.direct:
                result = True
            else:
                result = inject.checkBooleanExpression("NVL(RAWTOHEX([RANDNUM1]),[RANDNUM1])=RAWTOHEX([RANDNUM1])")

            if not result:
                warnMsg = "the back-end DBMS is not %s" % DBMS.ORACLE
                logger.warning(warnMsg)

                return False

            setDbms(DBMS.ORACLE)

            self.getBanner()

            if not conf.extensiveFp:
                return True

            infoMsg = "actively fingerprinting %s" % DBMS.ORACLE
            logger.info(infoMsg)

            # Reference: https://en.wikipedia.org/wiki/Oracle_Database
            for version in ("23c", "21c", "19c", "18c", "12c", "11g", "10g", "9i", "8i", "7"):
                number = int(re.search(r"([\d]+)", version).group(1))
                output = inject.checkBooleanExpression("%d=(SELECT SUBSTR((VERSION),1,%d) FROM SYS.PRODUCT_COMPONENT_VERSION WHERE ROWNUM=1)" % (number, 1 if number < 10 else 2))

                if output:
                    Backend.setVersion(version)
                    break

            return True
        else:
            warnMsg = "the back-end DBMS is not %s" % DBMS.ORACLE
            logger.warning(warnMsg)

            return False

    def forceDbmsEnum(self):
        if conf.db:
            conf.db = conf.db.upper()

        if conf.tbl:
            conf.tbl = conf.tbl.upper()
