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
import warnings
import src.core.setting.setting as  settings
from src.core._Warnings.warnings_ import PythonInterpreterWarning
print(settings.PYTHON_VERSION)

def check_version():
    if settings.PYTHON_VERSION < 3:
        warnings.warn("Python 2 is no longer supported.",category=PythonInterpreterWarning)
        raise SystemExit
    


