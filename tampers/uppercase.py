import re


def tamper(payload:str,**kwargs):
    _retval = None
    _pattern = re.compile(r"[a-z]")
    payload = re.sub(_pattern,lambda x: x.group().upper(),payload)
    _retval = payload
    return _retval


