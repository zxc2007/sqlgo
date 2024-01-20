# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator2/generator/generator.py script.
"""Public API for tf._api.v2.summary namespace
"""

import sys as _sys

from tensorflow.python.ops.summary_ops_v2 import all_v2_summary_ops # line: 656
from tensorflow.python.ops.summary_ops_v2 import initialize # line: 468
from tensorflow.python.proto_exports import Event # line: 28
from tensorflow.python.proto_exports import SessionLog # line: 47
from tensorflow.python.proto_exports import Summary # line: 50
from tensorflow.python.proto_exports import SummaryDescription # line: 53
from tensorflow.python.proto_exports import TaggedRunMetadata # line: 59
from tensorflow.python.summary.summary import audio # line: 350
from tensorflow.python.summary.summary import get_summary_description # line: 768
from tensorflow.python.summary.summary import histogram # line: 258
from tensorflow.python.summary.summary import image # line: 142
from tensorflow.python.summary.summary import merge # line: 616
from tensorflow.python.summary.summary import merge_all # line: 698
from tensorflow.python.summary.summary import scalar # line: 61
from tensorflow.python.summary.summary import tensor_summary # line: 560
from tensorflow.python.summary.summary import text # line: 471
from tensorflow.python.summary.writer.writer import FileWriter # line: 278
from tensorflow.python.summary.writer.writer_cache import FileWriterCache # line: 24

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "summary", public_apis=None, deprecation=False,
      has_lite=False)
