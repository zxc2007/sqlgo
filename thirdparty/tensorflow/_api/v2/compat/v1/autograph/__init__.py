# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator2/generator/generator.py script.
"""Public API for tf._api.v2.autograph namespace
"""

import sys as _sys

from tensorflow._api.v2.compat.v1.autograph import experimental
from tensorflow.python.autograph.impl.api import to_code_v1 as to_code # line: 850
from tensorflow.python.autograph.impl.api import to_graph_v1 as to_graph # line: 779
from tensorflow.python.autograph.utils.ag_logging import set_verbosity # line: 36
from tensorflow.python.autograph.utils.ag_logging import trace # line: 87

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "autograph", public_apis=None, deprecation=False,
      has_lite=False)
