# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/value/date.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layer.api.value import year_month_pb2 as api_dot_value_dot_year__month__pb2
from layer.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61pi/value/date.proto\x12\x03\x61pi\x1a\x1a\x61pi/value/year_month.proto\x1a\x17validate/validate.proto\"B\n\x04\x44\x61te\x12\"\n\nyear_month\x18\x01 \x01(\x0b\x32\x0e.api.YearMonth\x12\x16\n\x03\x64\x61y\x18\x02 \x01(\x05\x42\t\xfa\x42\x06\x1a\x04\x18\x1f(\x01\x42\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_DATE = DESCRIPTOR.message_types_by_name['Date']
Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), {
  'DESCRIPTOR' : _DATE,
  '__module__' : 'api.value.date_pb2'
  # @@protoc_insertion_point(class_scope:api.Date)
  })
_sym_db.RegisterMessage(Date)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _DATE.fields_by_name['day']._options = None
  _DATE.fields_by_name['day']._serialized_options = b'\372B\006\032\004\030\037(\001'
  _DATE._serialized_start=82
  _DATE._serialized_end=148
# @@protoc_insertion_point(module_scope)
