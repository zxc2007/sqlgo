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
    Appends (Access) NULL byte character (%00) at the end of payload

    Requirement:
        * Microsoft Access

    Notes:
        * Useful to bypass weak web application firewalls when the back-end
          database management system is Microsoft Access - further uses are
          also possible

    Reference: http://projects.webappsec.org/w/page/13246949/Null-Byte-Injection

    >>> tamper('1 AND 1=1')
    '1 AND 1=1%00'
    """

    return "%s%%00" % payload if payload else payload