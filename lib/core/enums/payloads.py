from enum import Enum
import os
import sys
sys.path.append(os.getcwd())
from utilis.colorago.colorago import Fore

class Payload(Enum):
    UNION_ALL_SELECT = f"'{Fore.WHITE}{'\033[2m'}{'\033[1m'}UNION all select query{"\033[0m"}{Fore.RESET}'"

