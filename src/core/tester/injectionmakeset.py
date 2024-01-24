import os
import sys
sys.path.append(os.getcwd())
from src.core.request.POSt.post import SubData
from src.core.payloads.makesetsqlpayload import _sorted as make_set_payload
from src.core.parser.cmdline import url as _url
from src.core.parser.cmdline import port as _port
from src.core.parser.cmdline import attack



class Tester_make_set_sql:
    def __init__(self,data, url= _url,  port=_port) -> None:
        self.url = url
        self.data = data if data is not None else make_set_payload
        self.port = port
        self.sub = SubData(self.url, self.port)

    def test(self):
        self.sub.submit_data(self.url, self.data)



def run_attack_make_set():
    if attack == "make_set":
        test = Tester_make_set_sql(data=None)
        test.test()

# test = Tester(url="http://testfire.net/login.jsp",port=80,data=None)
# test.test()
