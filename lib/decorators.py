import functools
import hashlib
import threading
import os
import sys
sys.path.append(os.getcwd())
from lib.datastruc.datastruct import OrderedDict
from lib.datastruc.injectdict import LRUDict
_cache = {}
_cache_lock = threading.Lock()
_method_locks = {}

def cachedmethod(f):
    """
    Method with a cached content

    >>> __ = cachedmethod(lambda _: _)
    >>> __(1)
    1
    >>> __(1)
    1
    >>> __ = cachedmethod(lambda *args, **kwargs: args[0])
    >>> __(2)
    2
    >>> __ = cachedmethod(lambda *args, **kwargs: next(iter(kwargs.values())))
    >>> __(foobar=3)
    3

    Reference: http://code.activestate.com/recipes/325205-cache-decorator-in-python-24/
    """

    _cache[f] = LRUDict(capacity=256)

    @functools.wraps(f)
    def _f(*args, **kwargs):
        try:
            key = int(hashlib.md5("|".join(str(_) for _ in (f, args, kwargs)).encode("utf-8")).hexdigest(), 16) & 0x7fffffffffffffff
        except ValueError:  # https://github.com/sqlmapproject/sqlmap/issues/4281 (NOTE: non-standard Python behavior where hexdigest returns binary value)
            result = f(*args, **kwargs)
        else:
            try:
                with _cache_lock:
                    result = _cache[f][key]
            except KeyError:
                result = f(*args, **kwargs)

                with _cache_lock:
                    _cache[f][key] = result

        return result

    return _f