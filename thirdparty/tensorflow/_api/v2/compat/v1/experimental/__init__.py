# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator2/generator/generator.py script.
"""Public API for tf._api.v2.experimental namespace
"""

import sys as _sys

from tensorflow._api.v2.compat.v1.experimental import extension_type
from tensorflow.python.data.ops.optional_ops import Optional # line: 31
from tensorflow.python.eager.context import async_clear_error # line: 2836
from tensorflow.python.eager.context import async_scope # line: 2772
from tensorflow.python.eager.context import function_executor_type # line: 2621
from tensorflow.python.framework.dtypes import float8_e4m3fn # line: 465
from tensorflow.python.framework.dtypes import float8_e5m2 # line: 456
from tensorflow.python.framework.dtypes import int4 # line: 471
from tensorflow.python.framework.dtypes import uint4 # line: 477
from tensorflow.python.framework.extension_type import BatchableExtensionType # line: 831
from tensorflow.python.framework.extension_type import ExtensionType # line: 99
from tensorflow.python.framework.extension_type import ExtensionTypeBatchEncoder # line: 651
from tensorflow.python.framework.extension_type import ExtensionTypeSpec # line: 419
from tensorflow.python.framework.load_library import register_filesystem_plugin # line: 199
from tensorflow.python.framework.strict_mode import enable_strict_mode # line: 22
from tensorflow.python.ops.control_flow_v2_toggles import output_all_intermediates # line: 73
from tensorflow.python.ops.ragged.dynamic_ragged_shape import DynamicRaggedShape # line: 167
from tensorflow.python.ops.ragged.row_partition import RowPartition # line: 56
from tensorflow.python.ops.structured.structured_tensor import StructuredTensor # line: 53
from tensorflow.python.util.dispatch import dispatch_for_api # line: 334
from tensorflow.python.util.dispatch import dispatch_for_binary_elementwise_apis # line: 878
from tensorflow.python.util.dispatch import dispatch_for_binary_elementwise_assert_apis # line: 936
from tensorflow.python.util.dispatch import dispatch_for_unary_elementwise_apis # line: 811
from tensorflow.python.util.dispatch import unregister_dispatch_for # line: 553

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "experimental", public_apis=None, deprecation=False,
      has_lite=False)
