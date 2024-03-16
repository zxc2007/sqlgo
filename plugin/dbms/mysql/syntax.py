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
import binascii

from sqlmap.lib.core.convert import getBytes
from sqlmap.lib.core.convert import getOrds
from sqlmap.lib.core.convert import getUnicode
from sqlmap.plugins.generic.syntax import Syntax as GenericSyntax

class Syntax(GenericSyntax):
    @staticmethod
    def escape(expression, quote=True):
        """
        >>> Syntax.escape("SELECT 'abcdefgh' FROM foobar") == "SELECT 0x6162636465666768 FROM foobar"
        True
        >>> Syntax.escape(u"SELECT 'abcd\xebfgh' FROM foobar") == "SELECT CONVERT(0x61626364c3ab666768 USING utf8) FROM foobar"
        True
        """

        def escaper(value):
            if all(_ < 128 for _ in getOrds(value)):
                return "0x%s" % getUnicode(binascii.hexlify(getBytes(value)))
            else:
                return "CONVERT(0x%s USING utf8)" % getUnicode(binascii.hexlify(getBytes(value, "utf8")))

        return Syntax._escape(expression, quote, escaper)