import os
import sys
sys.path.append(os.getcwd())
from colorama import Fore,init

init(autoreset=True)

def reset_tested_payload(t_payload):
    return Fore.RED+t_payload+Fore.GREEN

# print(reset_tested_payload("wef")+"efe")
# python sqlgo.py -u http://testfire.net/index.jsp?content=business_deposit.htm --port 443 --level 5