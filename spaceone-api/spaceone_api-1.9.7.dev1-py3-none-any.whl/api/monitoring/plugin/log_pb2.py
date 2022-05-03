# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/monitoring/plugin/log.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(spaceone/api/monitoring/plugin/log.proto\x12\x1espaceone.api.monitoring.plugin\x1a\x1cgoogle/protobuf/struct.proto\"!\n\x04Sort\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\x08\"\xa6\x02\n\nLogRequest\x12(\n\x07options\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0bsecret_data\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12(\n\x08resource\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Value\x12\r\n\x05start\x18\x05 \x01(\t\x12\x0b\n\x03\x65nd\x18\x06 \x01(\t\x12\x32\n\x04sort\x18\x07 \x01(\x0b\x32$.spaceone.api.monitoring.plugin.Sort\x12\r\n\x05limit\x18\x08 \x01(\x05\x12\x0e\n\x06schema\x18\t \x01(\t\"8\n\x0cLogsDataInfo\x12(\n\x04logs\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.ListValue2k\n\x03Log\x12\x64\n\x04list\x12*.spaceone.api.monitoring.plugin.LogRequest\x1a,.spaceone.api.monitoring.plugin.LogsDataInfo\"\x00\x30\x01\x62\x06proto3')



_SORT = DESCRIPTOR.message_types_by_name['Sort']
_LOGREQUEST = DESCRIPTOR.message_types_by_name['LogRequest']
_LOGSDATAINFO = DESCRIPTOR.message_types_by_name['LogsDataInfo']
Sort = _reflection.GeneratedProtocolMessageType('Sort', (_message.Message,), {
  'DESCRIPTOR' : _SORT,
  '__module__' : 'spaceone.api.monitoring.plugin.log_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.monitoring.plugin.Sort)
  })
_sym_db.RegisterMessage(Sort)

LogRequest = _reflection.GeneratedProtocolMessageType('LogRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGREQUEST,
  '__module__' : 'spaceone.api.monitoring.plugin.log_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.monitoring.plugin.LogRequest)
  })
_sym_db.RegisterMessage(LogRequest)

LogsDataInfo = _reflection.GeneratedProtocolMessageType('LogsDataInfo', (_message.Message,), {
  'DESCRIPTOR' : _LOGSDATAINFO,
  '__module__' : 'spaceone.api.monitoring.plugin.log_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.monitoring.plugin.LogsDataInfo)
  })
_sym_db.RegisterMessage(LogsDataInfo)

_LOG = DESCRIPTOR.services_by_name['Log']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SORT._serialized_start=106
  _SORT._serialized_end=139
  _LOGREQUEST._serialized_start=142
  _LOGREQUEST._serialized_end=436
  _LOGSDATAINFO._serialized_start=438
  _LOGSDATAINFO._serialized_end=494
  _LOG._serialized_start=496
  _LOG._serialized_end=603
# @@protoc_insertion_point(module_scope)
