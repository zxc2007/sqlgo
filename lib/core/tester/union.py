import os
import sys
import re
sys.path.append(os.getcwd())
from lib.core.payloads.unionpayload import union_payload
from lib.core.request.POSt.post import subber
from lib.logger.log import logger
from utilis._regex.extractparam import replace_url_parameter


def union():
    for payload in union_payload().split("\n"):
        _infomsg = None
        msg = None
        subber.submit_data(payload)
        logger.info(subber.response)

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
def union_man():
    for payload in union_payload().split("\n"):
        rep = (replace_url_parameter(url="http://testfire.net/index.jsp?content=business_deposit.htm",new_value=payload))
        print(rep[0])
    

