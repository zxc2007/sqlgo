import os
import sys
import time
sys.path.append(os.getcwd())
from utilis._regex.extractparam import replace_url_parameter
from lib.logger.log import logger
from lib.core.parser.cmdline import url as _url

def prompt_parameter(url=_url):
    _,param = replace_url_parameter(url,new_value=None)
    logger.info("testing if %s is injectable."%param)
    time.sleep(5)

