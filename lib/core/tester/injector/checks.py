import re
import os
import sys
sys.path.append(os.getcwd())
import urllib.parse
from lib.core.enums.devstatus import DevStatus
from lib.core.enums.priority import PRIORITY

__status__ = DevStatus.READY_FOR_PRODUCTION_AND_USE
__priority__ = PRIORITY.NORMAL
def newline_fixation(payload):
    payload = urllib.parse.unquote(payload)
    if "\n" in payload:
        #_ = payload.find("\n") + 1
        #payload = _urllib.parse.quote(payload[:_]) + payload[_:]
        payload = payload.replace("\n","%0a")
    if "\r" in payload:
        #_ = payload.find("\r\n") + 1
        #payload = _urllib.parse.quote(payload[:_]) + payload[_:]
        payload = payload.replace("\r","%0d")
    return payload