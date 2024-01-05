import re


def tamper(payload,**kwargs):
    _retval = None
    _pattern = re.compile(r"\s")
    payload = re.sub(_pattern,"/",payload)
    _retval = payload
    return _retval

    