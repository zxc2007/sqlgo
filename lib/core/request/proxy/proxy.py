import urllib3
import urllib.request
import os
import sys
sys.path.append(os.getcwd())
import lib.core.setting.setting as settings
def use_proxy(request, ignore_proxy=False, tor=False, tor_proxy=None, proxy=None):
    try:
        if ignore_proxy:
            proxy_manager = urllib3.ProxyManager({})
            return proxy_manager.urlopen(request, timeout=settings.TIMEOUT)
        elif tor:
            tor_proxy = {settings.TOR_HTTP_PROXY_SCHEME: tor_proxy}
            proxy_manager = urllib3.ProxyManager(tor_proxy)
            return proxy_manager.urlopen(request, timeout=settings.TIMEOUT)
        else:
            request.set_proxy(proxy, settings.SCHEME)
            return urllib.request.urlopen(request, timeout=settings.TIMEOUT)
    except Exception as err_msg:
        return str(err_msg)
import urllib.request
import os
import sys


sys.path.append(os.getcwd())

# Import your settings module (assuming it is located at lib.core.setting.setting)
import lib.core.setting.setting as settings

# # Your HTTP request object (replace this with your actual request)
# your_request_object = urllib.request.Request("http://testfire.net/index.jsp?content=business_deposit.htm")

# # Usage Example: Use General Proxy with IP: 180.183.157.159, Port: 8080
# # Usage Example: Use General Proxy with IP: 180.183.157.159, Port: 8080
# proxy_ip = "180.183.157.159"
# proxy_port = 8080
# proxy_url = f"{proxy_ip}:{proxy_port}"
# result_use_general_proxy = use_proxy(your_request_object, proxy=proxy_url)
# print("Result (Use General Proxy):", result_use_general_proxy)