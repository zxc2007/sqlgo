#!/usr/bin/env python
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

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    HTML encode in decimal (using code points) all characters (e.g. ' -> &#39;)

    >>> tamper("1' AND SLEEP(5)#")
    '&#49;&#39;&#32;&#65;&#78;&#68;&#32;&#83;&#76;&#69;&#69;&#80;&#40;&#53;&#41;&#35;'
    """

    retVal = payload

    if payload:
        retVal = ""
        i = 0

        while i < len(payload):
            retVal += "&#%s;" % ord(payload[i])
            i += 1

    return retVal