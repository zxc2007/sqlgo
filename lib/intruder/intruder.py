import os
import sys
import threading
import socket
sys.path.append(os.getcwd())
from lib.core.payloads.makesetsqlpayload import make_set_sql_payload
from lib.core.payloads.substringpayload import sub_string_sql_inj
from utilis._regex.extractparam import replace_url_parameter
from lib.core.request.POSt.post import SubData
from lib.core.request.GET.get import Get
from lib.logger.log import logger
from  lib.core.parser.cmdline import time_out
from lib.core.payloads.substringpayload import _sorted

class Intruder_substring(
    threading.Thread
):

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.payload = None
        self.result = []
        self.datasub = SubData(self.host,self.port)
        self.payload_url = None
        self.timeout = socket.setdefaulttimeout(time_out if time_out is not None else 10)


    def _send_payload_substring(self):
        if self.payload is None:
            rows = sub_string_sql_inj().split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows)
            self.payload = sorted_payload
            # print(self.payload)
        
        for payload in self.payload.split("\n"):
            req = self.datasub.submit_data(self.host,self.payload)
            self.result.append(self.datasub)
            logger.info("testing:%s"%payload)
    
    def _send_substring_payload_requests_lib(self):
        pass
    
    def run_substring(self):
        threads = [
            self._send_payload_substring(),
            self._send_substring_payload_requests_lib()
        ]
        for _ in threads:
            _thread = threading.Thread(target=_)
            _thread.start()
            _thread.join()
    
                


# obj = Intruder("http://testfire.net/index.jsp?content=business_deposit.htm",8080)
# obj.run_substring()
        
class MakeSet:

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.payload = None
        self.result = []
        self.datasub = SubData(self.host,self.port)
        self.payload_url = None
        self.timeout = socket.setdefaulttimeout(time_out if time_out is not None else 10)


    def _send_payload_make_set(self):
        if self.payload is None:
            rows = make_set_sql_payload().split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows)
            self.payload = sorted_payload
            # print(self.payload)
        
        for payload in self.payload.split("\n"):
            req = self.datasub.submit_data(self.host,self.payload)
            self.result.append(self.datasub)
            logger.info(f"testing {payload} ")
        


