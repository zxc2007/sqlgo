import os
import sys
sys.path.append(os.getcwd())
from lib.core.tester.injector._verboseresponses import Verbose


def verbose_response():
    Verbose.verbose_response()