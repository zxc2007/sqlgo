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
import sys
import os
import src.core.setting.setting as settings

__tamper__ = "printf2echo"

settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  """
  Replaces printf with echo
  >>> tamper("str=$(printf '%d' '$char')")


  
  'str=$(echo -n $char | od -An -tuC | xargs)'
  """
  def printf_to_echo(payload):
    if "printf" in payload:
      payload = payload.replace("str=$(printf" + settings.WHITESPACES[0] + "'%d'" + settings.WHITESPACES[0] + "\"'$char'\")", "str=$(echo" + settings.WHITESPACES[0] + "-n" + settings.WHITESPACES[0] + "$char" + settings.WHITESPACES[0] + "|" + settings.WHITESPACES[0] + "od" + settings.WHITESPACES[0] + "-An" + settings.WHITESPACES[0] + "-tuC" + settings.WHITESPACES[0] + "|" + settings.WHITESPACES[0] + "xargs)")
    return payload

  return printf_to_echo(payload)
    