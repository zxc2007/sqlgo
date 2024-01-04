import os
import sys
sys.path.append(os.getcwd())
import tamper.base64
import tamper.printf2cho
import tamper.space2comment 
import tamper.space2plus
import tamper.space2space
from lib.core.parser.cmdline import tamper as _tamper

def apply_tamper(payload):
    if _tamper == "base64":
        return tamper.base64.tamper(payload)
    elif _tamper == "printf2echo":
        return tamper.printf2cho.tamper(payload)
    elif _tamper == "space2comment":
        return tamper.space2comment.tamper(payload)
    elif _tamper == "space2plus":
        return tamper.space2plus.tamper(payload)
    elif _tamper == "space2space":
        return tamper.space2space.tamper(payload)
    elif _tamper is None:
        return payload
    else:
        return payload