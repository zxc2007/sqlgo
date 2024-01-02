from enum import Enum
import os
import sys
sys.path.append(os.getcwd())
from utilis.colorago.colorago import Fore

class Payload(Enum):
    UNION_ALL_SELECT = f"'{Fore.WHITE}\033[2m\033[1mUNION all select MYSQL query\033[0m{Fore.RESET}'"
    MAKE_SET = f"'{Fore.WHITE}\033[2m\033[1mMAKE SET MYSQL query\033[0m{Fore.RESET}'"
    SUBSTRING = f"'{Fore.WHITE}\033[2m\033[1mSUBSTRING MYSQL query\033[0m{Fore.RESET}'"
    TIME_BASED = f"'{Fore.WHITE}\033[2m\033[1mTIME BASED MYSQL query\033[0m{Fore.RESET}'"
    ERROR_BASED = f"'{Fore.WHITE}\033[2m\033[1mERROR BASED MYSQL query\033[0m{Fore.RESET}'"


