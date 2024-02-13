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
from sqlmap.plugins.generic.takeover import Takeover as GenericTakeover

class Takeover(GenericTakeover):
    def osCmd(self):
        errMsg = "Operating system command execution functionality not "
        errMsg += "yet implemented for Oracle"
        raise SqlmapUnsupportedFeatureException(errMsg)

    def osShell(self):
        errMsg = "Operating system shell functionality not yet "
        errMsg += "implemented for Oracle"
        raise SqlmapUnsupportedFeatureException(errMsg)

    def osPwn(self):
        errMsg = "Operating system out-of-band control functionality "
        errMsg += "not yet implemented for Oracle"
        raise SqlmapUnsupportedFeatureException(errMsg)

    def osSmb(self):
        errMsg = "One click operating system out-of-band control "
        errMsg += "functionality not yet implemented for Oracle"
        raise SqlmapUnsupportedFeatureException(errMsg)
