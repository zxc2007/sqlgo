import os
import sys
sys.path.append(os.getcwd())
from lib.core.payloads.substringpayload import _sorted as substring_payload
from lib.core.parser.cmdline import url as _url
from lib.core.parser.cmdline import port as _port
from lib.core.parser.cmdline import attack
from lib.core.request.POSt.post import SubData

class SubstringTester:
    def __init__(self,data, url= _url,  port=_port) -> None:
        self.url = url
        self.data = data if data is not None else substring_payload
        self.port = port
        self.sub = SubData(self.url, self.port)

    def test(self):
        self.sub.submit_data(self.url, self.data)



def run_substring():
    if attack == "sub_string":
        test = SubstringTester(data=None)
        test.test()

# test = SubstringTester(url="http://testfire.net/login.jsp",port=80,data=None)
# test.test()