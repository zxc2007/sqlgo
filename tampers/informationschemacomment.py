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



def tamper(payload, **kwargs):
    """
    Add an inline comment (/**/) to the end of all occurrences of (MySQL) "information_schema" identifier

    >>> tamper('SELECT table_name FROM INFORMATION_SCHEMA.TABLES')
    'SELECT table_name FROM INFORMATION_SCHEMA/**/.TABLES'
    """

    retVal = payload

    if payload:
        retVal = re.sub(r"(?i)(information_schema)\.", r"\g<1>/**/.", payload)

    return retVal