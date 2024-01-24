import os
import sys
sys.path.append(os.getcwd())
from src.core.tester.injector._verboseresponses import Verbose
from src.core.enums.devstatus import DevStatus
from src.core.enums.priority import PRIORITY

__status__ = DevStatus.READY_FOR_PRODUCTION_AND_USE
__priority__ = PRIORITY.VERY_HIGH

def verbose_response():
    Verbose.verbose_response()