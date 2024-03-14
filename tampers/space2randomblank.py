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

import random



def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces space character (' ') with a random blank character from a valid set of alternate characters

    Tested against:
        * Microsoft SQL Server 2005
        * MySQL 4, 5.0 and 5.5
        * Oracle 10g
        * PostgreSQL 8.3, 8.4, 9.0

    Notes:
        * Useful to bypass several web application firewalls

    >>> random.seed(0)
    >>> tamper('SELECT id FROM users')
    'SELECT%0Did%0CFROM%0Ausers'
    """

    # ASCII table:
    #   TAB     09      horizontal TAB
    #   LF      0A      new line
    #   FF      0C      new page
    #   CR      0D      carriage return
    blanks = ("%09", "%0A", "%0C", "%0D")
    retVal = payload

    if payload:
        retVal = ""
        quote, doublequote, firstspace = False, False, False

        for i in range(len(payload)):
            if not firstspace:
                if payload[i].isspace():
                    firstspace = True
                    retVal += random.choice(blanks)
                    continue

            elif payload[i] == '\'':
                quote = not quote

            elif payload[i] == '"':
                doublequote = not doublequote

            elif payload[i] == ' ' and not doublequote and not quote:
                retVal += random.choice(blanks)
                continue

            retVal += payload[i]

    return retVal