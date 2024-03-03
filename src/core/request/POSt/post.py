#!/usr/bin/env python
"""
# SQLGO License - Version 1.1

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
import socket
import os
import sys
import time


from src.core.request.inits.TCP._init import socket_init
from src.logger.log import logger
from src.core.Exceptions.exceptions import SQLgoWrongUrlException
from src.data import arg

class SubData:
    def __init__(self, host=arg.url, port=arg.port,timeout=arg.time_out):
        self.host = host
        self.port = port
        self.response = None  
        self._timeout = timeout
        socket.setdefaulttimeout(self._timeout if isinstance(self._timeout,int) else 5)

    def submit_data(self, data="X"):
        host, path = self.parse_url(self.host)

        # Construct the POST request headers and body
        headers = "POST %s HTTP/1.1\r\nHost: %s\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: %d\r\n\r\n"%(path,host,len(data))
        request = headers + data

        s = socket_init()

        s.connect((host, self.port if self.port is not None else 80))

        s.sendall(request.encode())

        response = b""
        for _ in range(10):
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
