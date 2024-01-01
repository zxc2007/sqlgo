import os
import sys
import re
import random
import string
sys.path.append(os.getcwd())
from lib.core.payloads.substringpayload import sub_string_sql_inj as payload
from lib.core.request.POSt.post import subber
from lib.logger.log import logger
from lib.core.enums.payloads import Payload
from lib.datastruc.keygendict import Keygendict

def substring():
    _caps = Keygendict()
    _dmdg = None
    for _payload in payload().split("\n"):
        subber.submit_data(_payload)
        logger.info("testing%s"%Payload.SUBSTRING.value)
        logger.debug(subber.response)
        _caps.add_cap(key=f"Debug response:{random.randint(0,100)}{random.choice(string.ascii_letters)}",value=subber.response)
        if re.search(r"\bid",subber.response) or re.search(r"\wid",subber.response):
            _dmdg = "Found id for some values in html response."
            logger.debug(_dmdg)
            _caps.add_cap(key=f"IDcap{random.choice(string.ascii_letters)}{random.randint(0,100)}")
