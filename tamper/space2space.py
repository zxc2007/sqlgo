import sys
import os
import re
sys.path.append(os.getcwd())
import lib.core.setting.setting as settings

def tamper(payload,**kwargs):
    _payload = re.sub(r"\s", "      ", payload)
    return _payload

