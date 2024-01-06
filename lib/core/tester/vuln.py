import os
import sys
sys.path.append(os.getcwd())
from lib.core.common.errors import errors
from bs4 import BeautifulSoup
import thirdparty.requests

def vulnerable(response):
    if type(response) == None:
        for err in errors:
            if err in response.content.decode().lower():
                    return True
            return False
