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



def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Converts all (non-alphanum) characters in a given payload to overlong UTF8 (not processing already encoded) (e.g. ' -> %C0%A7)

    Reference:
        * https://www.acunetix.com/vulnerabilities/unicode-transformation-issues/
        * https://www.thecodingforums.com/threads/newbie-question-about-character-encoding-what-does-0xc0-0x8a-have-in-common-with-0xe0-0x80-0x8a.170201/

    >>> tamper('SELECT FIELD FROM TABLE WHERE 2>1')
    'SELECT%C0%A0FIELD%C0%A0FROM%C0%A0TABLE%C0%A0WHERE%C0%A02%C0%BE1'
    """

    retVal = payload

    if payload:
        retVal = ""
        i = 0

        while i < len(payload):
            if payload[i] == '%' and (i < len(payload) - 2) and payload[i + 1:i + 2] in string.hexdigits and payload[i + 2:i + 3] in string.hexdigits:
                retVal += payload[i:i + 3]
                i += 3
            else:
                if payload[i] not in (string.ascii_letters + string.digits):
                    retVal += "%%%.2X%%%.2X" % (0xc0 + (ord(payload[i]) >> 6), 0x80 + (ord(payload[i]) & 0x3f))
                else:
                    retVal += payload[i]
                i += 1

    return retVal