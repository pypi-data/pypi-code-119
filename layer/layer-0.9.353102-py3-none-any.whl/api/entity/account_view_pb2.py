# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/entity/account_view.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layer.api import ids_pb2 as api_dot_ids__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pi/entity/account_view.proto\x12\x03\x61pi\x1a\rapi/ids.proto\"M\n\x0b\x41\x63\x63ountView\x12\x1a\n\x02id\x18\x01 \x01(\x0b\x32\x0e.api.AccountId\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\tB\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_ACCOUNTVIEW = DESCRIPTOR.message_types_by_name['AccountView']
AccountView = _reflection.GeneratedProtocolMessageType('AccountView', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTVIEW,
  '__module__' : 'api.entity.account_view_pb2'
  # @@protoc_insertion_point(class_scope:api.AccountView)
  })
_sym_db.RegisterMessage(AccountView)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _ACCOUNTVIEW._serialized_start=53
  _ACCOUNTVIEW._serialized_end=130
# @@protoc_insertion_point(module_scope)
