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
    Splits FROM schema identifiers (e.g. 'testdb.users') with whitespace (e.g. 'testdb 9.e.users')

    Requirement:
        * MySQL

    Notes:
        * Reference: https://media.blackhat.com/us-13/US-13-Salgado-SQLi-Optimization-and-Obfuscation-Techniques-Slides.pdf

    >>> tamper('SELECT id FROM testdb.users')
    'SELECT id FROM testdb 9.e.users'
    """

    return re.sub(r"(?i)( FROM \w+)\.(\w+)", r"\g<1> 9.e.\g<2>", payload) if payload else payload