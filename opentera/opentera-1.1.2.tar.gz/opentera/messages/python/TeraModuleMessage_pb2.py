# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TeraModuleMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TeraModuleMessage.proto',
  package='opentera.protobuf',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17TeraModuleMessage.proto\x12\x11opentera.protobuf\x1a\x19google/protobuf/any.proto\"\xc6\x01\n\x11TeraModuleMessage\x12\x39\n\x04head\x18\x01 \x01(\x0b\x32+.opentera.protobuf.TeraModuleMessage.Header\x12\"\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any\x1aR\n\x06Header\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x0c\n\x04time\x18\x02 \x01(\x01\x12\x0b\n\x03seq\x18\x03 \x01(\r\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x65st\x18\x05 \x01(\tb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_TERAMODULEMESSAGE_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='opentera.protobuf.TeraModuleMessage.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='opentera.protobuf.TeraModuleMessage.Header.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='opentera.protobuf.TeraModuleMessage.Header.time', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seq', full_name='opentera.protobuf.TeraModuleMessage.Header.seq', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='opentera.protobuf.TeraModuleMessage.Header.source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dest', full_name='opentera.protobuf.TeraModuleMessage.Header.dest', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=272,
)

_TERAMODULEMESSAGE = _descriptor.Descriptor(
  name='TeraModuleMessage',
  full_name='opentera.protobuf.TeraModuleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='opentera.protobuf.TeraModuleMessage.head', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='opentera.protobuf.TeraModuleMessage.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TERAMODULEMESSAGE_HEADER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=272,
)

_TERAMODULEMESSAGE_HEADER.containing_type = _TERAMODULEMESSAGE
_TERAMODULEMESSAGE.fields_by_name['head'].message_type = _TERAMODULEMESSAGE_HEADER
_TERAMODULEMESSAGE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['TeraModuleMessage'] = _TERAMODULEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TeraModuleMessage = _reflection.GeneratedProtocolMessageType('TeraModuleMessage', (_message.Message,), {

  'Header' : _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
    'DESCRIPTOR' : _TERAMODULEMESSAGE_HEADER,
    '__module__' : 'TeraModuleMessage_pb2'
    # @@protoc_insertion_point(class_scope:opentera.protobuf.TeraModuleMessage.Header)
    })
  ,
  'DESCRIPTOR' : _TERAMODULEMESSAGE,
  '__module__' : 'TeraModuleMessage_pb2'
  # @@protoc_insertion_point(class_scope:opentera.protobuf.TeraModuleMessage)
  })
_sym_db.RegisterMessage(TeraModuleMessage)
_sym_db.RegisterMessage(TeraModuleMessage.Header)


# @@protoc_insertion_point(module_scope)
