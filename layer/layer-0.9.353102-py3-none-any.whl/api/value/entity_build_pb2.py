# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/value/entity_build.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layer.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/value/entity_build.proto\x12\x03\x61pi\x1a\x17validate/validate.proto\"%\n\x0b\x45ntityBuild\x12\x16\n\x05value\x18\x01 \x01(\x05\x42\x07\xfa\x42\x04\x1a\x02(\x00\x42\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_ENTITYBUILD = DESCRIPTOR.message_types_by_name['EntityBuild']
EntityBuild = _reflection.GeneratedProtocolMessageType('EntityBuild', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYBUILD,
  '__module__' : 'api.value.entity_build_pb2'
  # @@protoc_insertion_point(class_scope:api.EntityBuild)
  })
_sym_db.RegisterMessage(EntityBuild)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _ENTITYBUILD.fields_by_name['value']._options = None
  _ENTITYBUILD.fields_by_name['value']._serialized_options = b'\372B\004\032\002(\000'
  _ENTITYBUILD._serialized_start=62
  _ENTITYBUILD._serialized_end=99
# @@protoc_insertion_point(module_scope)
