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
import os
import sys
import src.core.setting.setting as settings
from src.core.converts.base64 import b64encode

def tamper(payload,**kwargs):
    """
    Converts payload to base64

    >>> tamper("hello world")
    b'aGVsbG8gd29ybGQ='
    """
    if isinstance(payload,bytes):
        _payload = b64encode(payload)
        return _payload
    payload = payload.encode()
    _payload = b64encode(payload)
    return _payload
