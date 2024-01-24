import os
import sys
sys.path.append(os.getcwd())
from thirdparty_.colorama import Fore,init

init(autoreset=True)

def reset_tested_payload(t_payload):
    return Fore.RED+t_payload+Fore.GREEN

# print(reset_tested_payload("wef")+"efe")