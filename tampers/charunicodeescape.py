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

import string


def tamper(payload, **kwargs):
    """
    Unicode-escapes non-encoded characters in a given payload (not processing already encoded) (e.g. SELECT -> \u0053\u0045\u004C\u0045\u0043\u0054)

    Notes:
        * Useful to bypass weak filtering and/or WAFs in JSON contexes

    >>> tamper('SELECT FIELD FROM TABLE')
    '\\\\u0053\\\\u0045\\\\u004C\\\\u0045\\\\u0043\\\\u0054\\\\u0020\\\\u0046\\\\u0049\\\\u0045\\\\u004C\\\\u0044\\\\u0020\\\\u0046\\\\u0052\\\\u004F\\\\u004D\\\\u0020\\\\u0054\\\\u0041\\\\u0042\\\\u004C\\\\u0045'
    """

    retVal = payload

    if payload:
        retVal = ""
        i = 0

        while i < len(payload):
            if payload[i] == '%' and (i < len(payload) - 2) and payload[i + 1:i + 2] in string.hexdigits and payload[i + 2:i + 3] in string.hexdigits:
                retVal += "\\u00%s" % payload[i + 1:i + 3]
                i += 3
            else:
                retVal += '\\u%.4X' % ord(payload[i])
                i += 1

    return retVal
