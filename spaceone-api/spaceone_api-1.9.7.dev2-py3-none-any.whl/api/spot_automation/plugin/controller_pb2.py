# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/spot_automation/plugin/controller.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4spaceone/api/spot_automation/plugin/controller.proto\x12#spaceone.api.spot_automation.plugin\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"7\n\x0bInitRequest\x12(\n\x07options\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"g\n\rVerifyRequest\x12(\n\x07options\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0bsecret_data\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"7\n\nPluginInfo\x12)\n\x08metadata\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"5\n\x0cResponseInfo\x12%\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"v\n\x0cPatchRequest\x12,\n\x0bsecret_data\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12(\n\x07\x63ommand\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct2\xc2\x02\n\nController\x12k\n\x04init\x12\x30.spaceone.api.spot_automation.plugin.InitRequest\x1a/.spaceone.api.spot_automation.plugin.PluginInfo\"\x00\x12V\n\x06verify\x12\x32.spaceone.api.spot_automation.plugin.VerifyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12o\n\x05patch\x12\x31.spaceone.api.spot_automation.plugin.PatchRequest\x1a\x31.spaceone.api.spot_automation.plugin.ResponseInfo\"\x00\x62\x06proto3')



_INITREQUEST = DESCRIPTOR.message_types_by_name['InitRequest']
_VERIFYREQUEST = DESCRIPTOR.message_types_by_name['VerifyRequest']
_PLUGININFO = DESCRIPTOR.message_types_by_name['PluginInfo']
_RESPONSEINFO = DESCRIPTOR.message_types_by_name['ResponseInfo']
_PATCHREQUEST = DESCRIPTOR.message_types_by_name['PatchRequest']
InitRequest = _reflection.GeneratedProtocolMessageType('InitRequest', (_message.Message,), {
  'DESCRIPTOR' : _INITREQUEST,
  '__module__' : 'spaceone.api.spot_automation.plugin.controller_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.plugin.InitRequest)
  })
_sym_db.RegisterMessage(InitRequest)

VerifyRequest = _reflection.GeneratedProtocolMessageType('VerifyRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYREQUEST,
  '__module__' : 'spaceone.api.spot_automation.plugin.controller_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.plugin.VerifyRequest)
  })
_sym_db.RegisterMessage(VerifyRequest)

PluginInfo = _reflection.GeneratedProtocolMessageType('PluginInfo', (_message.Message,), {
  'DESCRIPTOR' : _PLUGININFO,
  '__module__' : 'spaceone.api.spot_automation.plugin.controller_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.plugin.PluginInfo)
  })
_sym_db.RegisterMessage(PluginInfo)

ResponseInfo = _reflection.GeneratedProtocolMessageType('ResponseInfo', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEINFO,
  '__module__' : 'spaceone.api.spot_automation.plugin.controller_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.plugin.ResponseInfo)
  })
_sym_db.RegisterMessage(ResponseInfo)

PatchRequest = _reflection.GeneratedProtocolMessageType('PatchRequest', (_message.Message,), {
  'DESCRIPTOR' : _PATCHREQUEST,
  '__module__' : 'spaceone.api.spot_automation.plugin.controller_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.plugin.PatchRequest)
  })
_sym_db.RegisterMessage(PatchRequest)

_CONTROLLER = DESCRIPTOR.services_by_name['Controller']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INITREQUEST._serialized_start=152
  _INITREQUEST._serialized_end=207
  _VERIFYREQUEST._serialized_start=209
  _VERIFYREQUEST._serialized_end=312
  _PLUGININFO._serialized_start=314
  _PLUGININFO._serialized_end=369
  _RESPONSEINFO._serialized_start=371
  _RESPONSEINFO._serialized_end=424
  _PATCHREQUEST._serialized_start=426
  _PATCHREQUEST._serialized_end=544
  _CONTROLLER._serialized_start=547
  _CONTROLLER._serialized_end=869
# @@protoc_insertion_point(module_scope)
