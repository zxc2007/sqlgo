# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/tpu/tpu_embedding_configuration.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.protobuf.tpu import optimization_parameters_pb2 as tensorflow_dot_core_dot_protobuf_dot_tpu_dot_optimization__parameters__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>tensorflow/core/protobuf/tpu/tpu_embedding_configuration.proto\x12\x0etensorflow.tpu\x1a:tensorflow/core/protobuf/tpu/optimization_parameters.proto\"\x93\x08\n\x19TPUEmbeddingConfiguration\x12S\n\x10table_descriptor\x18\x01 \x03(\x0b\x32\x39.tensorflow.tpu.TPUEmbeddingConfiguration.TableDescriptor\x12<\n\x04mode\x18\x02 \x01(\x0e\x32..tensorflow.tpu.TPUEmbeddingConfiguration.Mode\x12\"\n\x1a\x62\x61tch_size_per_tensor_core\x18\x03 \x01(\x05\x12\x11\n\tnum_hosts\x18\x04 \x01(\x05\x12\x18\n\x10num_tensor_cores\x18\x05 \x01(\x05\x12U\n\x11sharding_strategy\x18\x06 \x01(\x0e\x32:.tensorflow.tpu.TPUEmbeddingConfiguration.ShardingStrategy\x12+\n#pipeline_execution_with_tensor_core\x18\x07 \x01(\x08\x12\x1e\n\x16profile_data_directory\x18\t \x01(\t\x12W\n\x12\x66\x65\x61ture_descriptor\x18\n \x03(\x0b\x32;.tensorflow.tpu.TPUEmbeddingConfiguration.FeatureDescriptor\x12M\n\rspmd_sharding\x18\x0b \x01(\x0b\x32\x36.tensorflow.tpu.TPUEmbeddingConfiguration.SpmdSharding\x1a\xaa\x01\n\x0fTableDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0fvocabulary_size\x18\x02 \x01(\x03\x12\x11\n\tdimension\x18\x03 \x01(\x05\x12\x14\n\x0cnum_features\x18\x04 \x01(\x05\x12G\n\x17optimization_parameters\x18\x05 \x01(\x0b\x32&.tensorflow.tpu.OptimizationParameters\x1aH\n\x11\x46\x65\x61tureDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08table_id\x18\x02 \x01(\x05\x12\x13\n\x0binput_shape\x18\x03 \x03(\x05\x1a>\n\x0cSpmdSharding\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x1d\n\x15num_cores_per_replica\x18\x02 \x01(\x05\"L\n\x04Mode\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\r\n\tINFERENCE\x10\x01\x12\x0c\n\x08TRAINING\x10\x02\x12\x16\n\x12\x42\x41\x43KWARD_PASS_ONLY\x10\x03\",\n\x10ShardingStrategy\x12\x0f\n\x0b\x44IV_DEFAULT\x10\x00\x12\x07\n\x03MOD\x10\x01J\x04\x08\x08\x10\tR\routput_layout\"\x13\n\x11TPUEmbeddingErrorb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow.core.protobuf.tpu.tpu_embedding_configuration_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TPUEMBEDDINGCONFIGURATION._serialized_start=143
  _TPUEMBEDDINGCONFIGURATION._serialized_end=1186
  _TPUEMBEDDINGCONFIGURATION_TABLEDESCRIPTOR._serialized_start=733
  _TPUEMBEDDINGCONFIGURATION_TABLEDESCRIPTOR._serialized_end=903
  _TPUEMBEDDINGCONFIGURATION_FEATUREDESCRIPTOR._serialized_start=905
  _TPUEMBEDDINGCONFIGURATION_FEATUREDESCRIPTOR._serialized_end=977
  _TPUEMBEDDINGCONFIGURATION_SPMDSHARDING._serialized_start=979
  _TPUEMBEDDINGCONFIGURATION_SPMDSHARDING._serialized_end=1041
  _TPUEMBEDDINGCONFIGURATION_MODE._serialized_start=1043
  _TPUEMBEDDINGCONFIGURATION_MODE._serialized_end=1119
  _TPUEMBEDDINGCONFIGURATION_SHARDINGSTRATEGY._serialized_start=1121
  _TPUEMBEDDINGCONFIGURATION_SHARDINGSTRATEGY._serialized_end=1165
  _TPUEMBEDDINGERROR._serialized_start=1188
  _TPUEMBEDDINGERROR._serialized_end=1207
# @@protoc_insertion_point(module_scope)
