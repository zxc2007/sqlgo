#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

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
import urllib3
try:
    import urllib.request
except:
    import urllib2 as urllib
import os
import sys
import traceback

import src.core.setting.setting as settings

def use_proxy(request, ignore_proxy=False, tor=False, tor_proxy=None, proxy=None):
    try:
        if ignore_proxy:
            proxy_manager = urllib3.ProxyManager({})
            return proxy_manager.urlopen(request, timeout=settings.TIMEOUT)
        elif tor:
            tor_proxy = {settings.TOR_HTTP_PROXY_SCHEME: tor_proxy}
            proxy_manager = urllib3.ProxyManager(**tor_proxy)
            return proxy_manager.urlopen(request, timeout=settings.TIMEOUT)
        else:
            http = urllib3.PoolManager()
            return http.request('GET', request.full_url, timeout=settings.TIMEOUT, headers=request.headers)
    except Exception as err_msg:
        traceback.print_exc()
        return str(err_msg)


# proxy_ip = "180.183.157.159"
# proxy_port = 8080

def set_proxy(ip,port):
    proxy_url = "http://%s:%d"%(ip,port)
    return proxy_url
# result_use_general_proxy = use_proxy(your_request_object, proxy=proxy_url)
# print("Result (Use General Proxy):", result_use_general_proxy)

