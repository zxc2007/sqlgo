from enum import Enum
import os
import sys
sys.path.append(os.getcwd())
from utilis.colorago.colorago import Fore

class Payload(Enum):
    UNION_ALL_SELECT = f"'{Fore.WHITE}{'\033[2m'}{'\033[1m'}UNION all select MYSQL query{"\033[0m"}{Fore.RESET}'"
    MAKE_SET = f"'{Fore.WHITE}{'\033[2m'}{'\033[1m'}MAKE SET MYSQL query{"\033[0m"}{Fore.RESET}'"
    SUBSTRING = f"'{Fore.WHITE}{'\033[2m'}{'\033[1m'}SUBSTRING MYSQL query{"\033[0m"}{Fore.RESET}'"
    TIME_BASED = f"'{Fore.WHITE}{'\033[2m'}{'\033[1m'}TIME BASED MYSQL query{"\033[0m"}{Fore.RESET}'"

