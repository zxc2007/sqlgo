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
import os
import re
def tamper(payload, **kwargs):
    """
    Replaces (MySQL) instances like 'MID(A, B, C)' with 'MID(A FROM B FOR C)' counterpart

    Requirement:
        * MySQL

    Tested against:
        * MySQL 5.0 and 5.5

    >>> tamper('MID(VERSION(), 1, 1)')
    'MID(VERSION() FROM 1 FOR 1)'
    """

    retVal = payload


    match = re.search(r"(?i)MID\((.+?)\s*,\s*(\d+)\s*\,\s*(\d+)\s*\)", payload or "")
    if match:
        retVal = retVal.replace(match.group(0), "MID(%s FROM %s FOR %s)" % (match.group(1), match.group(2), match.group(3)))

    return retVal
