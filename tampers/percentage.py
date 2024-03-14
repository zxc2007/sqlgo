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

import os
import string




def tamper(payload, **kwargs):
    """
    Adds a percentage sign ('%') infront of each character (e.g. SELECT -> %S%E%L%E%C%T)

    Requirement:
        * ASP

    Tested against:
        * Microsoft SQL Server 2000, 2005
        * MySQL 5.1.56, 5.5.11
        * PostgreSQL 9.0

    Notes:
        * Useful to bypass weak and bespoke web application firewalls

    >>> tamper('SELECT FIELD FROM TABLE')
    '%S%E%L%E%C%T %F%I%E%L%D %F%R%O%M %T%A%B%L%E'
    """

    if payload:
        retVal = ""
        i = 0

        while i < len(payload):
            if payload[i] == '%' and (i < len(payload) - 2) and payload[i + 1:i + 2] in string.hexdigits and payload[i + 2:i + 3] in string.hexdigits:
                retVal += payload[i:i + 3]
                i += 3
            elif payload[i] != ' ':
                retVal += '%%%s' % payload[i]
                i += 1
            else:
                retVal += payload[i]
                i += 1

    return retVal