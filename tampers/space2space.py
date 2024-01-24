import sys
import os
import re
sys.path.append(os.getcwd())
import src.core.setting.setting as settings

def tamper(payload,**kwargs):
    _payload = re.sub(r"\s", "      ", payload)
    return _payload

