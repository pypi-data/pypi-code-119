# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/spot_automation/plugin/interrupt.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3spaceone/api/spot_automation/plugin/interrupt.proto\x12#spaceone.api.spot_automation.plugin\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"N\n\x0cSetupRequest\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12,\n\x0bsecret_data\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"U\n\x17\x43onfirmInterruptRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12,\n\x0bsecret_data\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"K\n\rHandleRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12,\n\x0bsecret_data\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"O\n\nHandleInfo\x12\x1e\n\x16spot_group_resource_id\x18\x01 \x01(\t\x12\x13\n\x0bresource_id\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t2\xb5\x02\n\tInterrupt\x12T\n\x05setup\x12\x31.spaceone.api.spot_automation.plugin.SetupRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x61\n\x07\x63onfirm\x12<.spaceone.api.spot_automation.plugin.ConfirmInterruptRequest\x1a\x16.google.protobuf.Empty\"\x00\x12o\n\x06handle\x12\x32.spaceone.api.spot_automation.plugin.HandleRequest\x1a/.spaceone.api.spot_automation.plugin.HandleInfo\"\x00\x62\x06proto3')



_SETUPREQUEST = DESCRIPTOR.message_types_by_name['SetupRequest']
_CONFIRMINTERRUPTREQUEST = DESCRIPTOR.message_types_by_name['ConfirmInterruptRequest']
_HANDLEREQUEST = DESCRIPTOR.message_types_by_name['HandleRequest']
_HANDLEINFO = DESCRIPTOR.message_types_by_name['HandleInfo']
SetupRequest = _reflection.GeneratedProtocolMessageType('SetupRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETUPREQUEST,
  '__module__' : 'spaceone.api.spot_automation.plugin.interrupt_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.plugin.SetupRequest)
  })
_sym_db.RegisterMessage(SetupRequest)

ConfirmInterruptRequest = _reflection.GeneratedProtocolMessageType('ConfirmInterruptRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONFIRMINTERRUPTREQUEST,
  '__module__' : 'spaceone.api.spot_automation.plugin.interrupt_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.plugin.ConfirmInterruptRequest)
  })
_sym_db.RegisterMessage(ConfirmInterruptRequest)

HandleRequest = _reflection.GeneratedProtocolMessageType('HandleRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEREQUEST,
  '__module__' : 'spaceone.api.spot_automation.plugin.interrupt_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.plugin.HandleRequest)
  })
_sym_db.RegisterMessage(HandleRequest)

HandleInfo = _reflection.GeneratedProtocolMessageType('HandleInfo', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEINFO,
  '__module__' : 'spaceone.api.spot_automation.plugin.interrupt_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.plugin.HandleInfo)
  })
_sym_db.RegisterMessage(HandleInfo)

_INTERRUPT = DESCRIPTOR.services_by_name['Interrupt']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SETUPREQUEST._serialized_start=151
  _SETUPREQUEST._serialized_end=229
  _CONFIRMINTERRUPTREQUEST._serialized_start=231
  _CONFIRMINTERRUPTREQUEST._serialized_end=316
  _HANDLEREQUEST._serialized_start=318
  _HANDLEREQUEST._serialized_end=393
  _HANDLEINFO._serialized_start=395
  _HANDLEINFO._serialized_end=474
  _INTERRUPT._serialized_start=477
  _INTERRUPT._serialized_end=786
# @@protoc_insertion_point(module_scope)
