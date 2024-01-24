import re
import sys
import os
import warnings
sys.path.append(os.getcwd())
import src.core.setting.setting as settings

__tamper__ = "space2plus"

if not settings.TAMPER_SCRIPTS[__tamper__]:
    settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload, **kwargs):
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
    
# test = "hello world this is ali talking to you all!"
# print(f"Before tampering:{test}")
# print ()