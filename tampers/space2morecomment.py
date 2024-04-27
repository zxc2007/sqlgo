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
def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces (MySQL) instances of space character (' ') with comments '/**_**/'

    Tested against:
        * MySQL 5.0 and 5.5

    Notes:
        * Useful to bypass weak and bespoke web application firewalls

    >>> tamper('SELECT id FROM users')
    'SELECT/**_**/id/**_**/FROM/**_**/users'
    """

    retVal = payload

    if payload and isinstance(payload,str):
        retVal = ""
        quote, doublequote, firstspace = False, False, False

        for i in range(len(payload)):
            if not firstspace:
                if payload[i].isspace():
                    firstspace = True
                    retVal += "/**_**/"
                    continue

            elif payload[i] == '\'':
                quote = not quote

            elif payload[i] == '"':
                doublequote = not doublequote

            elif payload[i] == " " and not doublequote and not quote:
                retVal += "/**_**/"
                continue

            retVal += payload[i]

    return retVal