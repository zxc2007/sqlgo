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
from colorama import Fore,init

init(autoreset=True)

def reset_tested_payload(t_payload):
    return Fore.RED+t_payload+Fore.GREEN

# print(reset_tested_payload("wef")+"efe")
# python sqlgo.py -u http://testfire.net/index.jsp?content=business_deposit.htm --port 443 --level 5