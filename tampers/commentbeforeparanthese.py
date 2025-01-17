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
    Prepends (inline) comment before parentheses (e.g. ( -> /**/()

    Tested against:
        * Microsoft SQL Server
        * MySQL
        * Oracle
        * PostgreSQL

    Notes:
        * Useful to bypass web application firewalls that block usage
          of function calls

    >>> tamper('SELECT ABS(1)')
    'SELECT ABS/**/(1)'
    """

    retVal = payload

    if payload:
        retVal = re.sub(r"\b(\w+)\(", r"\g<1>/**/(", retVal)

    return retVal
