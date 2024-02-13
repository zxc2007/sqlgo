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
import sys
import tampers.base64
import tampers.printf2cho
import tampers.space2comment 
import tampers.space2plus
import tampers.space2space
import tampers.uppercase
import tampers.lowercase
import tampers.space2slash
import tampers.between
import tampers.binary
import tampers.chardoubleencode
import tampers.charencode
import tampers.charunicodeescape
from src.core.parser.cmdline import tamper as _tamper

def apply_tamper(payload):
    if _tamper == "base64":
        return tampers.base64.tamper(payload)
    elif _tamper == "printf2echo":
        return tampers.printf2cho.tamper(payload)
    elif _tamper == "space2comment":
        return tampers.space2comment.tamper(payload)
    elif _tamper == "space2plus":
        return tampers.space2plus.tamper(payload)
    elif _tamper == "space2space":
        return tampers.space2space.tamper(payload)
    elif _tamper == "uppercase":
        return tampers.uppercase.tamper(payload)
    elif _tamper == "lowercase":
        return tampers.lowercase.tamper(payload)
    elif _tamper == "space2slash":
        return tampers.space2slash.tamper(payload)
    elif _tamper == "between":
        return tampers.between.tamper(payload)
    elif _tamper == "binary":
        return tampers.binary.tamper(payload)
    elif _tamper == "chardoubleencode":
        return tampers.chardoubleencode.tamper(payload)
    elif _tamper == "charencode":
        return tampers.charencode.tamper(payload)
    elif _tamper == "charunicodeescape":
        return tampers.charunicodeescape.tamper(payload)
    elif _tamper is None:
        return payload
    else:
        return payload