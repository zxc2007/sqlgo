import re


def tamper(payload:str,**kwargs):
    _retval = None
    _pattern = re.compile(r"[A-Z]")
    payload = re.sub(_pattern,lambda x: x.group().lower(),payload)
    _retval = payload
    return _retval


