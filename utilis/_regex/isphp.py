import re
import os
import sys
sys.path.append(os.getcwd())
from src.core.parser.cmdline import url as _url
from src.logger.log import logger

def _isphp(url=_url):
    return bool(re.search(r"\.php", url))

def isphp():
    if _isphp() is True:
        logger.info("target:%s backend is designed with php.this site might be vulnerable to XSS(cross site scripting)"%_url)
        return True
    