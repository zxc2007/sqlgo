import os
import sys
sys.path.append(os.getcwd())
from lib.core.tester.injector._verboseresponses import Verbose
from lib.core.enums.devstatus import DevStatus
from lib.core.enums.priority import PRIORITY

__status__ = DevStatus.READY_FOR_PRODUCTION_AND_USE
__priority__ = PRIORITY.VERY_HIGH

def verbose_response():
    Verbose.verbose_response()