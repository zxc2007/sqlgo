# Copyright 2022 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Keras models API."""


from keras.src.engine.functional import Functional
from keras.src.engine.sequential import Sequential
from keras.src.engine.training import Model

# Private symbols that are used in tests.
# TODO(b/221261361): Clean up private symbols usage and remove these imports.
from keras.src.models.cloning import _clone_functional_model
from keras.src.models.cloning import _clone_layer
from keras.src.models.cloning import _clone_layers_and_model_config
from keras.src.models.cloning import _clone_sequential_model
from keras.src.models.cloning import clone_and_build_model
from keras.src.models.cloning import clone_model
from keras.src.models.cloning import share_weights
from keras.src.models.sharpness_aware_minimization import SharpnessAwareMinimization
from keras.src.saving.legacy.model_config import model_from_config
from keras.src.saving.legacy.model_config import model_from_json
from keras.src.saving.legacy.model_config import model_from_yaml
from keras.src.saving.saving_api import load_model
from keras.src.saving.saving_api import save_model
