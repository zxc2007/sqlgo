import os
import sys
sys.path.append(os.getcwd())


def IsListLike(value):
    return isinstance(value,(set,tuple,list))
