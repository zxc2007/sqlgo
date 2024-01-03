import os
import sys
import re
sys.path.append(os.getcwd())
import lib.core.setting.setting as settings

def get_value_inside_boundaries(value):
  try:
    value = re.search(settings.VALUE_BOUNDARIES, value).group(1)
  except Exception as ex:
    pass
  return value