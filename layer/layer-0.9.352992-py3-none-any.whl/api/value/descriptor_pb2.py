# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/value/descriptor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layer.api import ids_pb2 as api_dot_ids__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x61pi/value/descriptor.proto\x12\x03\x61pi\x1a\rapi/ids.proto\"\xe1\x02\n\x11\x44\x65scriptorCommand\x12<\n\rstore_dataset\x18\x01 \x01(\x0b\x32#.api.DescriptorCommand.StoreDatasetH\x00\x1a\x82\x02\n\x0cStoreDataset\x12\x14\n\x0c\x64\x61taset_name\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_source_name\x18\x02 \x01(\t\x12%\n\x08\x62uild_id\x18\x03 \x01(\x0b\x32\x13.api.DatasetBuildId\x12I\n\x0epartition_info\x18\x04 \x01(\x0b\x32\x31.api.DescriptorCommand.StoreDataset.PartitionInfo\x1aP\n\rPartitionInfo\x12\x14\n\x0cpartition_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x18\n\x10storage_location\x18\x03 \x01(\tB\t\n\x07\x63ommandB\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_DESCRIPTORCOMMAND = DESCRIPTOR.message_types_by_name['DescriptorCommand']
_DESCRIPTORCOMMAND_STOREDATASET = _DESCRIPTORCOMMAND.nested_types_by_name['StoreDataset']
_DESCRIPTORCOMMAND_STOREDATASET_PARTITIONINFO = _DESCRIPTORCOMMAND_STOREDATASET.nested_types_by_name['PartitionInfo']
DescriptorCommand = _reflection.GeneratedProtocolMessageType('DescriptorCommand', (_message.Message,), {

  'StoreDataset' : _reflection.GeneratedProtocolMessageType('StoreDataset', (_message.Message,), {

    'PartitionInfo' : _reflection.GeneratedProtocolMessageType('PartitionInfo', (_message.Message,), {
      'DESCRIPTOR' : _DESCRIPTORCOMMAND_STOREDATASET_PARTITIONINFO,
      '__module__' : 'api.value.descriptor_pb2'
      # @@protoc_insertion_point(class_scope:api.DescriptorCommand.StoreDataset.PartitionInfo)
      })
    ,
    'DESCRIPTOR' : _DESCRIPTORCOMMAND_STOREDATASET,
    '__module__' : 'api.value.descriptor_pb2'
    # @@protoc_insertion_point(class_scope:api.DescriptorCommand.StoreDataset)
    })
  ,
  'DESCRIPTOR' : _DESCRIPTORCOMMAND,
  '__module__' : 'api.value.descriptor_pb2'
  # @@protoc_insertion_point(class_scope:api.DescriptorCommand)
  })
_sym_db.RegisterMessage(DescriptorCommand)
_sym_db.RegisterMessage(DescriptorCommand.StoreDataset)
_sym_db.RegisterMessage(DescriptorCommand.StoreDataset.PartitionInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _DESCRIPTORCOMMAND._serialized_start=51
  _DESCRIPTORCOMMAND._serialized_end=404
  _DESCRIPTORCOMMAND_STOREDATASET._serialized_start=135
  _DESCRIPTORCOMMAND_STOREDATASET._serialized_end=393
  _DESCRIPTORCOMMAND_STOREDATASET_PARTITIONINFO._serialized_start=313
  _DESCRIPTORCOMMAND_STOREDATASET_PARTITIONINFO._serialized_end=393
# @@protoc_insertion_point(module_scope)
