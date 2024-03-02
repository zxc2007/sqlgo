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

import os
import re

def tamper(payload, **kwargs):
    """
    Replaces instances of UNION with -.1UNION

    Requirement:
        * MySQL

    Notes:
        * Reference: https://raw.githubusercontent.com/y0unge/Notes/master/SQL%20Injection%20WAF%20Bypassing%20shortcut.pdf

    >>> tamper('1 UNION ALL SELECT')
    '1-.1UNION ALL SELECT'
    >>> tamper('1" UNION ALL SELECT')
    '1"-.1UNION ALL SELECT'
    """

    return re.sub(r"(?i)\s+(UNION )", r"-.1\g<1>", payload) if payload else payload