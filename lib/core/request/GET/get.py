import socket 
import os
import sys

sys.path.append(os.getcwd())
from lib.core.request.inits.TCP._init import socket_init
from lib.logger.log import logger

class Get:
    def __init__(self,host,port) -> None:
        self.host = host
        self.port = port
        self._socket = None

    def _header_prep(self):
        header = f"GET / HTTP/1.1\r\nHost: {self.host}\r\n\r\n"
        return header
    
    def _tcp(self):
        s = socket_init()
        return s
    
    def _connect(self):
        s = self._tcp()
        s.connect((self.host, self.port))
        return s
    
    def _send(self,data=""):
        s = self._connect()
        s.sendall(self._header_prep().encode())
        s.close()
    
    def _response(self):
        _response = b""
        while True:
            chunk = self._connect().recv(4096)
            if not chunk:
                break
            _response += chunk

    def get_send(self):
        self._send()
        self._response()


obj = Get("scanme.org",22)
obj.get_send()

        


    

