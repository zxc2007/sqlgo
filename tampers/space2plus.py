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
import sys
import os
import warnings
import src.core.setting.setting as settings

__tamper__ = "space2plus"

if not settings.TAMPER_SCRIPTS[__tamper__]:
    settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload, **kwargs):
    """
    Replaces spaces with plus sign


    >>> tamper("hello world this is me talking to you all!")
    'hello+world+this+is+me+talking+to+you+all!'
    """
    warnings.filterwarnings("ignore",category=SyntaxWarning)
    _retval = None
    _pattern = re.compile(r"\s")
    settings.TAMPER_SCRIPTS[__tamper__] = True
    payload = re.sub(r"\s", "+", payload)
    if not re.search(r'\s',payload):
        _retval = payload
        return _retval
    
    for _ in payload:
        re.sub(r'\s','',payload)
    
    else:
        _retval = payload
        return _retval
    
