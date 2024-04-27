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
    HTML encode in hexadecimal (using code points) all characters (e.g. ' -> &#x31;)

    >>> tamper("1' AND SLEEP(5)#")
    '&#x31;&#x27;&#x20;&#x41;&#x4e;&#x44;&#x20;&#x53;&#x4c;&#x45;&#x45;&#x50;&#x28;&#x35;&#x29;&#x23;'
    """

    retVal = payload

    if payload:
        retVal = ""
        i = 0

        while i < len(payload):
            retVal += "&#x%s;" % format(ord(payload[i]), "x")
            i += 1

    return retVal