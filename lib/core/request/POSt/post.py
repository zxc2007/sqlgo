import socket
import os
import sys
import re

sys.path.append(os.getcwd())

from lib.core.request.inits.TCP._init import socket_init
from lib.logger.log import logger

class SubData:
    def __init__(self,host,port) -> None:
        self.host = host
        self.port = port
        
    def submit_data(self,url, data):
        host, path = self.parse_url(url)

        # Construct the POST request headers and body
        headers = f"POST {path} HTTP/1.1\r\nHost: {host}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(data)}\r\n\r\n"
        request = headers + data

        s = socket_init()

        s.connect((host, self.port if self.port is not None else 80))

        s.sendall(request.encode())

        response = s.recv(4096)
        # logger.info(response.decode())

        s.close()

    def parse_url(self,url):
        # Extract the host and path from the URL
        # Example: http://example.com/path -> ("example.com", "/path")
        url_parts = url.split("/", 3)
        host = url_parts[2]
        path = "/" + url_parts[3] if len(url_parts) > 3 else "/"
        return host, path
    



