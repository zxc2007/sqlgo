# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator2/generator/generator.py script.
"""Public API for tf._api.v2.nest namespace
"""

import sys as _sys

from tensorflow.python.util.nest import assert_same_structure # line: 301
from tensorflow.python.util.nest import flatten # line: 201
from tensorflow.python.util.nest import is_nested # line: 166
from tensorflow.python.util.nest import map_structure # line: 545
from tensorflow.python.util.nest import pack_sequence_as # line: 426

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "nest", public_apis=None, deprecation=False,
      has_lite=False)