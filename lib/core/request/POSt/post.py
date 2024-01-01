import socket
import os
import sys
import time

sys.path.append(os.getcwd())

from lib.core.request.inits.TCP._init import socket_init
from lib.logger.log import logger
from lib.core.Exceptions.exceptions import SQLgoWrongUrlException
from lib.core.parser.cmdline import url as _url
from lib.core.parser.cmdline import port as _port
from lib.core.parser.cmdline import time_out

class SubData:
    def __init__(self, host=_url, port=_port,timeout=time_out) -> None:
        self.host = host
        self.port = port
        self.response = None  
        self._timeout = timeout
        socket.setdefaulttimeout(self._timeout if isinstance(self._timeout,int) else 10)

    def submit_data(self, data="X"):
        host, path = self.parse_url(self.host)

        # Construct the POST request headers and body
        headers = f"POST {path} HTTP/1.1\r\nHost: {host}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(data)}\r\n\r\n"
        request = headers + data

        s = socket_init()

        s.connect((host, self.port if self.port is not None else 80))

        s.sendall(request.encode())

        response = b""
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            response += chunk

        s.close()
        
        self.response = response.decode()  # Store the response as an attribute
        return self.response

    def parse_url(self, url):
        url = self.host
        # Extract the host and path from the URL
        # Example: http://example.com/path -> ("example.com", "/path")
        try:
            url_parts = url.split("/", 3)
            host = url_parts[2]
            path = "/" + url_parts[3] if len(url_parts) > 3 else "/"
            return host, path

        except IndexError:
            raise SQLgoWrongUrlException

subber = SubData()
