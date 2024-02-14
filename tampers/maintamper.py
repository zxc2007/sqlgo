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
import tampers.commentbeforeparanthese
import tampers.decenties
import tampers.equaltolike
import tampers.equaltorlike
import tampers.escapequotes
import tampers.greatests
import tampers.hexentities
import tampers.htmlencode
import tampers.ifnull2casewhenisnull
import tampers.ifnull2isnull
import tampers.informationschemacomment
import tampers.least
import tampers.ord2ascii
import tampers.overlongutf8
import tampers.overlongutf8more
import tampers.percentage
import tampers.schemasplit
import tampers.scientific
import tampers.sp_password
import tampers.space2dash
import tampers.space2morecomment
import tampers.space2mssqlhash
import tampers.space2randomblank
import tampers.substring2leftright
import tampers.symboliclogical
import tampers.unionalltounion
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
    elif _tamper == "commentbeforeparanthese":
        return tampers.commentbeforeparanthese.tamper(payload)
    elif _tamper == "decenties":
        return tampers.decenties.tamper(payload)
    elif _tamper == "equaltolike":
        return tampers.equaltolike.tamper(payload)
    elif _tamper == "equaltorlike":
        return tampers.equaltorlike.tamper(payload)
    elif _tamper == "escapequotes":
        return tampers.escapequotes.tamper(payload)
    elif _tamper == "hexentities":
        return tampers.hexentities.tamper(payload)
    elif _tamper == "greatests":
        return tampers.greatests.tamper(payload)
    elif _tamper == "htmlencode":
        return tampers.htmlencode.tamper(payload)
    elif _tamper == "ifnull2casewhenisnull":
        return tampers.ifnull2casewhenisnull.tamper(payload)
    elif _tamper == "ifnull2isnull":
        return tampers.ifnull2isnull.tamper(payload)
    elif _tamper == "informationschemacomment":
        return tampers.informationschemacomment.tamper(payload)
    elif _tamper == "least":
        return tampers.least.tamper(payload)
    elif _tamper == "ord2ascii":
        return tampers.ord2ascii.tamper(payload)
    elif _tamper == "overlongutf8":
        return tampers.overlongutf8.tamper(payload)
    elif _tamper == "overlongutf8more":
        return tampers.overlongutf8more.tamper(payload)
    elif _tamper == "percentage":
        return tampers.percentage.tamper(payload)
    elif _tamper == "schemasplit":
        return tampers.schemasplit.tamper(payload)
    elif _tamper == "scientific":
        return tampers.scientific.tamper(payload)
    elif _tamper == "sp_password":
        return tampers.sp_password.tamper(payload)
    elif _tamper == "space2dash":
        return tampers.space2dash.tamper(payload)
    elif _tamper == "space2morecomment":
        return tampers.space2morecomment.tamper(payload)
    elif _tamper == "space2mssqlhash":
        return tampers.space2mssqlhash.tamper(payload)
    elif _tamper == "space2randomblank":
        return tampers.space2randomblank.tamper(payload)
    elif _tamper == "substring2leftright":
        return tampers.substring2leftright.tamper(payload)
    elif _tamper == "symboliclogical":
        return tampers.symboliclogical.tamper(payload)
    elif _tamper == "unionalltounion":
        return tampers.unionalltounion.tamper(payload)
    elif _tamper is None:
        return payload
    else:
        return payload