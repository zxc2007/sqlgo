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
import re
import os
import sys
import src.core.setting.setting as settings
settings.WHITESPACES

__tamper__ = "space2comment"

if not settings.TAMPER_SCRIPTS[__tamper__]:
    settings.TAMPER_SCRIPTS[__tamper__] = True


def tamper(payload):
    _retval = None
    settings.TAMPER_SCRIPTS[__tamper__] = True
    modified_payload = re.sub(r"\s", "--", payload)
    _retval = modified_payload
    return _retval
