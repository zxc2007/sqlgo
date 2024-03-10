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
from sqlmap.lib.core.exception import SqlmapUnsupportedFeatureException
from sqlmap.plugins.generic.filesystem import Filesystem as GenericFilesystem

class Filesystem(GenericFilesystem):
    def readFile(self, remoteFile):
        errMsg = "on SQLite it is not possible to read files"
        raise SqlmapUnsupportedFeatureException(errMsg)

    def writeFile(self, localFile, remoteFile, fileType=None, forceCheck=False):
        errMsg = "on SQLite it is not possible to write files"
        raise SqlmapUnsupportedFeatureException(errMsg)