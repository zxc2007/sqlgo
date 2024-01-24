import urllib.parse
import os
import sys
sys.path.append(os.getcwd())
from src.core.enums.devstatus import DevStatus
from src.core.enums.priority import PRIORITY

__status__ = DevStatus.READY_FOR_PRODUCTION_AND_USE
__priority__ = PRIORITY.VERY_HIGH
def get_url_part(url):
    # Find the URL part (scheme:[//host[:port]][/]path)
    o = urllib.parse.urlparse(url)
    url_part = o.scheme + "://" + o.netloc + o.path

    return url_part