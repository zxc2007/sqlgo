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
    HTML encode (using code points) all non-alphanumeric characters (e.g. ' -> &#39;)

    >>> tamper("1' AND SLEEP(5)#")
    '1&#39;&#32;AND&#32;SLEEP&#40;5&#41;&#35;'
    >>> tamper("1&#39;&#32;AND&#32;SLEEP&#40;5&#41;&#35;")
    '1&#39;&#32;AND&#32;SLEEP&#40;5&#41;&#35;'
    """

    if payload:
        payload = re.sub(r"&#(\d+);", lambda match: chr(int(match.group(1))), payload)      # NOTE: https://github.com/sqlmapproject/sqlmap/issues/5203
        payload = re.sub(r"[^\w]", lambda match: "&#%d;" % ord(match.group(0)), payload)

    return payload