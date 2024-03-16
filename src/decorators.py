#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
import functools
import hashlib
import threading
import os
import sys
from src.datastruc.datastruct import OrderedDict
from src.datastruc.injectdict import LRUDict
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