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

from src.core.request.inits.TCP._init import socket_init
from src.logger.log import logger
try:
    from urllib.parse import urlparse
except:
    from urlparse import urlparse

from src.data import arg
try:

    import requests

except:
    import third.requester as requests

def test_connection(url=arg.url, port=arg.port):
    logger.warning("Testing connection to the target URL: %s"%url)
    req = requests.get(url)
    _ = req.status_code if hasattr(req, "status_code") else 200
    logger.debug("current status code of the response code is:|%s|"%_)

    # Extract host and path from the URL
    parsed_url = urlparse(url)
    host = parsed_url.netloc
    path = parsed_url.path or "/"

    try:
        sock = socket_init()
        
        sock.settimeout(5)

        sock.connect((host, port))

        request = "GET %s HTTP/1.1\r\nHost: %s\r\n\r\n"%(path,host)

        sock.sendall(request.encode())

        response = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk

        logger.info("Connection established with the target.")

        sock.close()
        logger.debug("Closing the test connection socket...")
        
    except socket.error as e:
        logger.debug("Got error%s while testing peer connection"%str(e))


        