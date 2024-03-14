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
    Replaces all occurrences of operator equal ('=') with 'LIKE' counterpart

    Tested against:
        * Microsoft SQL Server 2005
        * MySQL 4, 5.0 and 5.5

    Notes:
        * Useful to bypass weak and bespoke web application firewalls that
          filter the equal character ('=')
        * The LIKE operator is SQL standard. Hence, this tamper script
          should work against all (?) databases

    >>> tamper('SELECT * FROM users WHERE id=1')
    'SELECT * FROM users WHERE id LIKE 1'
    """

    retVal = payload

    if payload:
        retVal = re.sub(r"\s*=\s*", " LIKE ", retVal)

    return retVal