import os
import sys
import warnings
sys.path.append(os.getcwd())
import lib.core.setting.setting as  settings
from lib.core._Warnings.warnings_ import PythonInterpreterWarning
print(settings.PYTHON_VERSION)

def check_version():
    if settings.PYTHON_VERSION < 3:
        warnings.warn("Python 2 is no longer supported.",category=PythonInterpreterWarning)
        raise SystemExit
    


