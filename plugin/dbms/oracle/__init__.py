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
from sqlmap.lib.core.enums import DBMS
from sqlmap.lib.core.settings import MYSQL_SYSTEM_DBS
from sqlmap.lib.core.unescaper import unescaper
from sqlmap.plugins.dbms.mysql.enumeration import Enumeration
from sqlmap.plugins.dbms.mysql.filesystem import Filesystem
from sqlmap.plugins.dbms.mysql.fingerprint import Fingerprint
from sqlmap.plugins.dbms.mysql.syntax import Syntax
from sqlmap.plugins.dbms.mysql.takeover import Takeover
from sqlmap.plugins.generic.misc import Miscellaneous

class MySQLMap(Syntax, Fingerprint, Enumeration, Filesystem, Miscellaneous, Takeover):
    """
    This class defines MySQL methods
    """

    def __init__(self):
        self.excludeDbsList = MYSQL_SYSTEM_DBS
        self.sysUdfs = {
            # UDF name: UDF return data-type
            "sys_exec": {"return": "int"},
            "sys_eval": {"return": "string"},
            "sys_bineval": {"return": "int"}
        }

        for cls in self.__class__.__bases__:
            cls.__init__(self)

    unescaper[DBMS.MYSQL] = Syntax.escape
