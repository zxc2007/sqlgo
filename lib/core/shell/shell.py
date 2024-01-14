import subprocess
import os
import sys
import re  # Import the regular expression module
sys.path.append(os.getcwd())
from extra.logo import logo
from extra.options import OPTIONS
from extra.options import AVAIAIBLE_INFO
import thirdparty.requests as requests
from lib.core.tester.injector._requests import error_based_injection

def shell_handler():
    _url = None

    print(logo)
    print(OPTIONS)
    while True:
        command = input("sqlgo>>>")
        
        # Use regular expression to match "set url" and extract the URL
        match = re.match(r'^set\s+url\s+(.+)$', command)
        match_port = re.match(r'^set\s+port\s+(.+)$', command)
        match_payload = re.match(r'^set\s+payload\s+(.+)$', command)
        match_attack = re.match(r'^set\s+attack\s+(.+)$', command)

        run = command == "exploit" or  command == "run"
        
        if match:
            _url = match.group(1)
            print(f"[*] url has been set on :{_url}...")
        
        if match_port:
            _port = match_port.group(1)
            print("[*] port has been set to %d"%int(_port))
        
        if command == "run" or command == "exploit" and match:
            req = requests.get(_url)
            print(req.status_code)
        
        if command == "show":
            print(
                AVAIAIBLE_INFO%(_url if _url is not None else "url has not been set.",int(_port) if _port is not None else "port has not been set",None,None)
            )
        
        if command == "exit":
            raise SystemExit
        


# shell_handler()
