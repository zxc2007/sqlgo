# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator2/generator/generator.py script.
"""Public API for tf._api.v2.data.experimental.service namespace
"""

import sys as _sys

from tensorflow.python.data.experimental.ops.data_service_ops import CrossTrainerCache # line: 117
from tensorflow.python.data.experimental.ops.data_service_ops import ShardingPolicy # line: 46
from tensorflow.python.data.experimental.ops.data_service_ops import distribute # line: 531
from tensorflow.python.data.experimental.ops.data_service_ops import from_dataset_id # line: 1045
from tensorflow.python.data.experimental.ops.data_service_ops import register_dataset # line: 839
from tensorflow.python.data.experimental.service.server_lib import DispatcherConfig # line: 44
from tensorflow.python.data.experimental.service.server_lib import WorkerConfig # line: 292

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "data.experimental.service", public_apis=None, deprecation=False,
      has_lite=False)
