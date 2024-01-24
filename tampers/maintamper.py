import os
import sys
sys.path.append(os.getcwd())
import tampers.base64
import tampers.printf2cho
import tampers.space2comment 
import tampers.space2plus
import tampers.space2space
import tampers.uppercase
import tampers.lowercase
import tampers.space2slash
from src.core.parser.cmdline import tamper as _tamper

def apply_tamper(payload):
    if _tamper == "base64":
        return tampers.base64.tamper(payload)
    elif _tamper == "printf2echo":
        return tampers.printf2cho.tamper(payload)
    elif _tamper == "space2comment":
        return tampers.space2comment.tamper(payload)
    elif _tamper == "space2plus":
        return tampers.space2plus.tamper(payload)
    elif _tamper == "space2space":
        return tampers.space2space.tamper(payload)
    elif _tamper == "uppercase":
        return tampers.uppercase.tamper(payload)
    elif _tamper == "lowercase":
        return tampers.lowercase.tamper(payload)
    elif _tamper == "space2slash":
        return tampers.space2slash.tamper(payload)
    elif _tamper is None:
        return payload
    else:
        return payload