import os
import sys
sys.path.append(os.getcwd())
from lib.core.tester.injectionmakeset import run_attack_make_set
from lib.core.parser.cmdline import attack


def main_exploit():
    if attack == "make_set":
        run_attack_make_set()
