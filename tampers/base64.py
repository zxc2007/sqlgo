import os
import sys
sys.path.append(os.getcwd())
import src.core.setting.setting as settings
from src.core.converts.base64 import b64encode

def tamper(payload:str,**kwargs):
    if isinstance(payload,bytes):
        _payload = b64encode(payload)
        return _payload
    payload = payload.encode()
    _payload = b64encode(payload)
    return _payload

# print(tamper("hello world"))