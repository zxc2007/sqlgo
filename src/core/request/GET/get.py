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
import sys
import time
from src.data import arg
class Get:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self.start = time.time()

    def _header_prep(self):
        header = "GET / HTTP/1.1\r\nHost: %s\r\n\r\n"%self.host
        return header

    def _connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        return s

    def _send(self):
        s = self._connect()
        header = self._header_prep()
        s.sendall(header.encode())
        s.close()

    def _response(self):
        _response = b""
        s = self._connect()
        chunk = s.recv(4096)
        if not chunk:
            pass
        _response += chunk
        s.close()
        return _response

    def get_send(self):
        self._send()
        response = self._response()
        print(response.decode())
    
    def using_requests(self):
        try:
            import requests
            res = requests.get(self.host,verify=False if arg.warningDisable else True)
        except ImportError:
            sys.exit("[!]requests library is not installed,exiting...")

