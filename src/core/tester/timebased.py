import os
import sys
import re
import random
import string
sys.path.append(os.getcwd())
from src.core.payloads.timebased import time_based_payload
from src.core.request.POSt.post import subber
from utilis._regex.extractparam import replace_url_parameter
from src.logger.log import logger
from src.datastruc.keygendict import Keygendict

def time_based():
    _dmsg = None
    _caps = Keygendict()
    _demerite = 0

    for payload in time_based_payload().split("\n"):
        subber.submit_data(payload)
        _caps.add_cap(key=f"Debug response:{random.randint(0,100)}{random.choice(string.ascii_letters)}",value=subber.response)
        if re.search(r"HAVING[^ ]+\Z",subber.response):
            _dmsg = "Found HAVING for some values in html response."
            _caps.add_cap(key=f"HAVINGcap{random.choice(string.ascii_letters)}{random.randint(0,100)}")
            _demerite +=1
            logger.debug(_dmsg)
        
        elif re.search(r"SELECT[^ ]+\Z",subber.response):
            _dmsg = "Found SELECT for some values in html response."
            _caps.add_cap(key=f"SELECTcap{random.choice(string.ascii_letters)}{random.randint(0,100)}")
            logger.debug(_dmsg)
            _demerite +=1


