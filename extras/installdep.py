#!/usr/bin/env python
"""
# SQLGO License - Version 1.3

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
from src.core.parser.cmdline import install_dep

def install_dependent():
    if install_dep:
        try:
            os.system("pip install -r requirements.txt")
        
        except os.error:
            try:
                
                os.system("pip3 install -r requirements.txt")
            
            except os.error:
                try:
                    os.system("python -m install -r requirements.txt")
                
                except:
                    os.system("python3 -m install -r requirements.txt")


