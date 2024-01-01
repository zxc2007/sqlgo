import os
import sys
import re
sys.path.append(os.getcwd())
from lib.core.payloads.unionpayload import union_payload
from lib.core.request.POSt.post import subber
from lib.logger.log import logger
from utilis._regex.extractparam import replace_url_parameter
from lib.core.parser.cmdline import url
from lib.core.enums.payloads import Payload


def union():
    for payload in union_payload().split("\n"):
        _infomsg = None
        msg = None
        _testmsg = None
        subber.submit_data(payload)
        logger.debug(subber.response)
        _testmsg = "testing: %s"%Payload.UNION_ALL_SELECT.value
        logger.info(_testmsg)

        if re.search(r"ORDER BY [^ ]+\Z",subber.response):
            msg = "ORDER BY"
            msg += "founded in the response"
            logger.debug(msg)
            _infomsg = "Some ORDER BY statement weaknesses leaked in the response"
            logger.info(_infomsg)
        
        elif re.search("SELECT * [^ ]+\Z",subber.response):
            msg = "SELECT *"
            msg += "founded in the response"
            logger.debug(msg)
            _infomsg = "Some possible SELECT statement leaks in the response"
            logger.info(_infomsg)
        
        elif re.search(r"\bid",subber.response):
            _pattern = re.search(r"\bid",subber.response)
            index = _pattern.end()
            words_after = re.findall(r"\b\w+\b", subber.response[index:index+100])
            logger.info(words_after)
def union_man():
    for payload in union_payload().split("\n"):
        rep = (replace_url_parameter(url=url,new_value=payload))
        logger.info(rep[0])
    

