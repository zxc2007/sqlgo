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
from src.datastruc.attrdict import AttrDict



TAMPER_SCRIPTS = [
    "base64",
    "printf2echo",
    "space2comment",
    "space2plus",
    "space2space",
    "uppercase",
    "lowercase",
    "space2slash",
    "between",
    "binary",
    "chardoubleencode",
    "charencode",
    "charunicodeescape",
    "commentbeforeparanthese",
    "decenties",
    "equaltolike",
    "equaltorlike",
    "escapequotes",
    "hexentities",
    "greatests",
    "htmlencode",
    "ifnull2casewhenisnull"
    "ifnull2isnull",
    "informationschemacomment",
    "least",
    "ord2ascii",
    "overlongutf8",
    "overlongutf8more",
    "percentage",
    "schemasplit",
    "scientific",
    "sp_password",
    "space2dash",
    "space2morecomment",
    "space2mssqlhash",
    "space2randomblank",
    "substring2leftright",
    "symboliclogical",
    "unionalltounion",
    "unmagicquotes",
    "apostrophemask",
    "appnednullbyte",
    "bluecoat",
    "charunicodeencode",
    "commalesslimit",
    "commalessmid",
    "concat2concatws",
    "dunion",
    "halfversionedmorekeywords",
    "hex2char",
    "if2case",
    "misunion",
    "modsecurityversioned",
    "modsecurityzeroversioned",
    "versionedkeywords",
    "versionedmorekeywords",
    "space2morehash",
    "space2mssqlblank",
    "space2hash",
    "caret",
    "dollaratsigns",
    "reverse",
    "slash2env",
    "sleep2timeout"
]

arg = AttrDict()
config = AttrDict()
datas = AttrDict()
gen = AttrDict()