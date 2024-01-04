import re
import os
import sys
sys.path.append(os.getcwd())
import lib.core.setting.setting as settings
settings.WHITESPACES

__tamper__ = "space2comment"

if not settings.TAMPER_SCRIPTS[__tamper__]:
    settings.TAMPER_SCRIPTS[__tamper__] = True


def tamper(payload:str):
    _retval = None
    settings.TAMPER_SCRIPTS[__tamper__] = True
    modified_payload = re.sub(r"\s", "--", payload)
    _retval = modified_payload
    return _retval
