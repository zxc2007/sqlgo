import os
import sys
sys.path.append(os.getcwd())
from src.core.common.errors import errors
from bs4 import BeautifulSoup

def vulnerable(response):
    if type(response) == None:
        for err in errors:
            if err in response.content.decode().lower():
                    return True
            return False
