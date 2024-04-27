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
from sqlmap.lib.core.convert import getOrds
from sqlmap.plugins.generic.syntax import Syntax as GenericSyntax

class Syntax(GenericSyntax):
    @staticmethod
    def escape(expression, quote=True):
        """
        >>> Syntax.escape("SELECT 'abcdefgh' FROM foobar") == "SELECT CHR(97)||CHR(98)||CHR(99)||CHR(100)||CHR(101)||CHR(102)||CHR(103)||CHR(104) FROM foobar"
        True
        >>> Syntax.escape(u"SELECT 'abcd\xebfgh' FROM foobar") == "SELECT CHR(97)||CHR(98)||CHR(99)||CHR(100)||NCHR(235)||CHR(102)||CHR(103)||CHR(104) FROM foobar"
        True
        """

        def escaper(value):
            return "||".join("%s(%d)" % ("CHR" if _ < 128 else "NCHR", _) for _ in getOrds(value))

        return Syntax._escape(expression, quote, escaper)
