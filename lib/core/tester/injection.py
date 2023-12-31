import os
import sys
sys.path.append(os.getcwd())
from lib.core.request.POSt.post import SubData
from lib.core.payloads.makesetsqlpayload import _sorted as make_set_payload



class Tester_make_set_sql:
    def __init__(self, url, data, port) -> None:
        self.url = url
        self.data = data if data is not None else make_set_payload
        self.port = port
        self.sub = SubData(self.url, self.port)

    def test(self):
        self.sub.submit_data(self.url, self.data)

# test = Tester(url="http://testfire.net/login.jsp",port=80,data=None)
# test.test()
    