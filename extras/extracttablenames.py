#!/usr/bin/env python
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
import os
import sys

def read_common_tables():
    """
    >>> _ = read_common_tables()

    >>> for i in _:
        ... for j in i:
            ... print(j)
    """
    cwd = os.getcwd()
    targetdir = cwd+"/data/txt/common-tables.txt"
    with open(targetdir, 'r') as f:
        payload = f.read() 
        rows = payload.split("\n") 
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows) 
        yield sorted_payload.split("\n")

