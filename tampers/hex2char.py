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

import re
from sqlmap.lib.core.convert import getOrds
from sqlmap.lib.core.convert import decodeHex
def tamper(payload, **kwargs):
    """
    Replaces each (MySQL) 0x<hex> encoded string with equivalent CONCAT(CHAR(),...) counterpart

    Requirement:
        * MySQL

    Tested against:
        * MySQL 4, 5.0 and 5.5

    Notes:
        * Useful in cases when web application does the upper casing

    >>> tamper('SELECT 0xdeadbeef')
    'SELECT CONCAT(CHAR(222),CHAR(173),CHAR(190),CHAR(239))'
    """

    retVal = payload

    if payload:
        for match in re.finditer(r"\b0x([0-9a-f]+)\b", retVal):
            if len(match.group(1)) > 2:
                result = "CONCAT(%s)" % ','.join("CHAR(%d)" % _ for _ in getOrds(decodeHex(match.group(1))))
            else:
                result = "CHAR(%d)" % ord(decodeHex(match.group(1)))
            retVal = retVal.replace(match.group(0), result)

    return retVal

x = tamper('SELECT 0xdeadbeef')
print(x)