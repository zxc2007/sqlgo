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

import os
import sys
import random

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
import tampers.unmagicquotes
import tampers.apostrophemask
import tampers.appnednullbyte
import tampers.bluecoat
import tampers.charunicodeencode
import tampers.commalesslimit
import tampers.commalessmid
import tampers.concat2concatws
import tampers.dunion
import tampers.halfversionedmorekeywords
import tampers.hex2char
import tampers.if2case
import tampers.misunion
import tampers.modsecurityversioned
import tampers.modsecurityzeroversioned
import tampers.versionedkeywords
import tampers.versionedmorekeywords
import tampers.space2morehash
import tampers.space2mssqlblank
import tampers.space2hash
import tampers.caret
import tampers.dollaratsigns
import tampers.reverse
import tampers.slash2env
import tampers.sleep2timeout
from src.core.parser.cmdline import tamper as _tamper
from src.data import arg
from src.core.converts.bin import str_to_bin
from src.core.converts.hex import str_to_hex
from src.data import arg
from src.data import TAMPER_SCRIPTS

def applyTamper(payload,**kwargs):
    """
    Apply tamper script, if any tamper called from cmdline will be executed here.
    """
    if arg.randomTamper:
        arg.tamper = random.choice(TAMPER_SCRIPTS)
    if arg.tamper == "base64":
        return tampers.base64.tamper(payload)
    elif arg.tamper == "printf2echo":
        return tampers.printf2cho.tamper(payload)
    elif arg.tamper == "space2comment":
        return tampers.space2comment.tamper(payload)
    elif arg.tamper == "space2plus":
        return tampers.space2plus.tamper(payload)
    elif arg.tamper == "space2space":
        return tampers.space2space.tamper(payload)
    elif arg.tamper == "uppercase":
        return tampers.uppercase.tamper(payload)
    elif arg.tamper == "lowercase":
        return tampers.lowercase.tamper(payload)
    elif arg.tamper == "space2slash":
        return tampers.space2slash.tamper(payload)
    elif arg.tamper == "between":
        return tampers.between.tamper(payload)
    elif arg.tamper == "binary":
        return tampers.binary.tamper(payload)
    elif arg.tamper == "chardoubleencode":
        return tampers.chardoubleencode.tamper(payload)
    elif arg.tamper == "charencode":
        return tampers.charencode.tamper(payload)
    elif arg.tamper == "charunicodeescape":
        return tampers.charunicodeescape.tamper(payload)
    elif arg.tamper == "commentbeforeparanthese":
        return tampers.commentbeforeparanthese.tamper(payload)
    elif arg.tamper == "decenties":
        return tampers.decenties.tamper(payload)
    elif arg.tamper == "equaltolike":
        return tampers.equaltolike.tamper(payload)
    elif arg.tamper == "equaltorlike":
        return tampers.equaltorlike.tamper(payload)
    elif arg.tamper == "escapequotes":
        return tampers.escapequotes.tamper(payload)
    elif arg.tamper == "hexentities":
        return tampers.hexentities.tamper(payload)
    elif arg.tamper == "greatests":
        return tampers.greatests.tamper(payload)
    elif arg.tamper == "htmlencode":
        return tampers.htmlencode.tamper(payload)
    elif arg.tamper == "ifnull2casewhenisnull":
        return tampers.ifnull2casewhenisnull.tamper(payload)
    elif arg.tamper == "ifnull2isnull":
        return tampers.ifnull2isnull.tamper(payload)
    elif arg.tamper == "informationschemacomment":
        return tampers.informationschemacomment.tamper(payload)
    elif arg.tamper == "least":
        return tampers.least.tamper(payload)
    elif arg.tamper == "ord2ascii":
        return tampers.ord2ascii.tamper(payload)
    elif arg.tamper == "overlongutf8":
        return tampers.overlongutf8.tamper(payload)
    elif arg.tamper == "overlongutf8more":
        return tampers.overlongutf8more.tamper(payload)
    elif arg.tamper == "percentage":
        return tampers.percentage.tamper(payload)
    elif arg.tamper == "schemasplit":
        return tampers.schemasplit.tamper(payload)
    elif arg.tamper == "scientific":
        return tampers.scientific.tamper(payload)
    elif arg.tamper == "sp_password":
        return tampers.sp_password.tamper(payload)
    elif arg.tamper == "space2dash":
        return tampers.space2dash.tamper(payload)
    elif arg.tamper == "space2morecomment":
        return tampers.space2morecomment.tamper(payload)
    elif arg.tamper == "space2mssqlhash":
        return tampers.space2mssqlhash.tamper(payload)
    elif arg.tamper == "space2randomblank":
        return tampers.space2randomblank.tamper(payload)
    elif arg.tamper == "substring2leftright":
        return tampers.substring2leftright.tamper(payload)
    elif arg.tamper == "symboliclogical":
        return tampers.symboliclogical.tamper(payload)
    elif arg.tamper == "unionalltounion":
        return tampers.unionalltounion.tamper(payload)
    elif arg.tamper == "unmagicquotes":
        return tampers.unmagicquotes.tamper(payload)
    elif arg.tamper == "apostrophemask":
        return tampers.apostrophemask.tamper(payload)
    elif arg.tamper == "appnednullbyte":
        return tampers.appnednullbyte.tamper(payload)
    elif arg.tamper == "bluecoat":
        return tampers.bluecoat.tamper(payload)
    elif arg.tamper == "charunicodeencode" or arg.tamper == "charuencode":
        return tampers.charunicodeencode.tamper(payload)
    elif arg.tamper == "commalesslimit":
        return tampers.commalesslimit.tamper(payload)
    elif arg.tamper == "commalessmid":
        return tampers.commalessmid.tamper(payload)
    elif arg.tamper == "concat2concatws":
        return tampers.concat2concatws.tamper(payload)
    elif arg.tamper == "dunion":
        return tampers.dunion.tamper(payload)
    elif arg.tamper == "halfversionedmorekeywords":
        return tampers.halfversionedmorekeywords.tamper(payload)
    elif arg.tamper == "hex2char":
        return tampers.hex2char.tamper(payload)
    elif arg.tamper == "if2case":
        return tampers.if2case.tamper(payload)
    elif arg.tamper == "misunion":
        return tampers.misunion.tamper(payload)
    elif arg.tamper == "modsecurityversioned":
        return tampers.modsecurityversioned.tamper(payload)
    elif arg.tamper == "modsecurityzeroversioned":
        return tampers.modsecurityzeroversioned.tamper(payload)
    elif arg.tamper == "versionedkeywords":
        return tampers.versionedkeywords.tamper(payload)
    elif arg.tamper == "versionedmorekeywords":
        return tampers.versionedmorekeywords.tamper(payload)
    elif arg.tamper == "space2morehash":
        return tampers.space2morehash.tamper(payload)
    elif arg.tamper == "space2mssqlblank":
        return tampers.space2mssqlblank.tamper(payload)
    elif arg.tamper == "space2hash":
        return tampers.space2hash.tamper(payload)
    elif arg.tamper == "reverse":
        return tampers.reverse.tamper(payload)
    elif arg.tamper == "slash2env":
        return tampers.slash2env.tamper(payload)
    elif arg.tamper == "sleep2timeout":
        return tampers.sleep2timeout.tamper(payload)
    elif arg.tamper == "caret":
        return tampers.caret.tamper(payload)
    elif arg.tamper == "dollaratsigns":
        return tampers.dollaratsigns.tamper(payload)
    elif arg.binary:
        return str_to_bin(payload)
    elif arg.hexa:
        return str_to_hex(payload)
    elif arg.tamper is None:
        return payload
    else:
        return payload