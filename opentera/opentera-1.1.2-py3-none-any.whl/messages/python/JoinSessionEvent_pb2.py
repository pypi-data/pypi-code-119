# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: JoinSessionEvent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='JoinSessionEvent.proto',
  package='opentera.protobuf',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16JoinSessionEvent.proto\x12\x11opentera.protobuf\"\xed\x01\n\x10JoinSessionEvent\x12\x13\n\x0bsession_url\x18\x01 \x01(\t\x12\x1c\n\x14session_creator_name\x18\x02 \x01(\t\x12\x14\n\x0csession_uuid\x18\x03 \x01(\t\x12\x1c\n\x14session_participants\x18\x04 \x03(\t\x12\x15\n\rsession_users\x18\x05 \x03(\t\x12\x17\n\x0fsession_devices\x18\x06 \x03(\t\x12\x10\n\x08join_msg\x18\x07 \x01(\t\x12\x1a\n\x12session_parameters\x18\x08 \x01(\t\x12\x14\n\x0cservice_uuid\x18\t \x01(\tb\x06proto3'
)




_JOINSESSIONEVENT = _descriptor.Descriptor(
  name='JoinSessionEvent',
  full_name='opentera.protobuf.JoinSessionEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_url', full_name='opentera.protobuf.JoinSessionEvent.session_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_creator_name', full_name='opentera.protobuf.JoinSessionEvent.session_creator_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_uuid', full_name='opentera.protobuf.JoinSessionEvent.session_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_participants', full_name='opentera.protobuf.JoinSessionEvent.session_participants', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_users', full_name='opentera.protobuf.JoinSessionEvent.session_users', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_devices', full_name='opentera.protobuf.JoinSessionEvent.session_devices', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='join_msg', full_name='opentera.protobuf.JoinSessionEvent.join_msg', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_parameters', full_name='opentera.protobuf.JoinSessionEvent.session_parameters', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_uuid', full_name='opentera.protobuf.JoinSessionEvent.service_uuid', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=46,
  serialized_end=283,
)

DESCRIPTOR.message_types_by_name['JoinSessionEvent'] = _JOINSESSIONEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JoinSessionEvent = _reflection.GeneratedProtocolMessageType('JoinSessionEvent', (_message.Message,), {
  'DESCRIPTOR' : _JOINSESSIONEVENT,
  '__module__' : 'JoinSessionEvent_pb2'
  # @@protoc_insertion_point(class_scope:opentera.protobuf.JoinSessionEvent)
  })
_sym_db.RegisterMessage(JoinSessionEvent)


# @@protoc_insertion_point(module_scope)
