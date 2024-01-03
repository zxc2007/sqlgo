import urllib3
import urllib.request
import os
import sys
import traceback

sys.path.append(os.getcwd())
import lib.core.setting.setting as settings

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

your_request_object = urllib.request.Request("http://testfire.net/index.jsp?content=business_deposit.htm")

# proxy_ip = "180.183.157.159"
# proxy_port = 8080

def set_proxy(ip,port):
    proxy_url = f"http://{ip}:{port}"
    return proxy_url
# result_use_general_proxy = use_proxy(your_request_object, proxy=proxy_url)
# print("Result (Use General Proxy):", result_use_general_proxy)

