import sys
import re


def data_to_std_out(text,no_int=True):
    _retval = None
    _text = sys.stdout.write(text)
    _retval = _text
    if no_int:
        _retval = re.sub(r"\d+","",str(_retval))
        return str(_retval if _retval is not None else "")
    
    return _retval

# print(data_to_std_out("h"))