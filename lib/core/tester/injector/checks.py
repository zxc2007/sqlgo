import re
import urllib.parse
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