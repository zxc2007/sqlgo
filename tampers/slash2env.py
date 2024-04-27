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
import re

def tamper(payload,**kwargs):
    """
    Replaces / with ${PATH%%u*}

    >>> tamper("SELECT * FROM users WHERE id = /")
    'SELECT * FROM users WHERE id = ${PATH%%u*}'
    """
    retVal = payload
    if re.search(r"/",payload):
        return re.sub(r"/", "${PATH%%u*}", payload)

    return retVal

