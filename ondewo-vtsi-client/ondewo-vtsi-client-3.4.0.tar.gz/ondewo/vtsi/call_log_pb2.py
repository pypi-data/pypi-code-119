# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/vtsi/call_log.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ondewo.sip import sip_pb2 as ondewo_dot_sip_dot_sip__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ondewo/vtsi/call_log.proto',
  package='ondewo.vtsi',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aondewo/vtsi/call_log.proto\x12\x0bondewo.vtsi\x1a\x1bgoogle/protobuf/empty.proto\x1a\x14ondewo/sip/sip.proto\x1a\x1cgoogle/api/annotations.proto\"#\n\x11GetCallIdsRequest\x12\x0e\n\x06sip_id\x18\x01 \x01(\t\"6\n\x12GetCallIdsResponse\x12\x0e\n\x06sip_id\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61ll_ids\x18\x02 \x03(\t\"$\n\x11GetVoipLogRequest\x12\x0f\n\x07\x63\x61ll_id\x18\x01 \x01(\t\"g\n\x12GetVoipLogResponse\x12(\n\nactive_log\x18\x01 \x01(\x0b\x32\x14.ondewo.vtsi.VoipLog\x12\'\n\tdone_logs\x18\x02 \x03(\x0b\x32\x14.ondewo.vtsi.VoipLog\"\x98\x01\n\x07VoipLog\x12\x0f\n\x07\x63\x61ll_id\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\x01\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\x01\x12-\n\x0estatus_history\x18\x04 \x03(\x0b\x32\x15.ondewo.sip.SipStatus\x12\'\n\x08\x63ounters\x18\x05 \x01(\x0b\x32\x15.ondewo.vtsi.Counters\">\n\x08\x43ounters\x12\x19\n\x11\x66ifteen_s_counter\x18\x01 \x01(\x03\x12\x17\n\x0fsixty_s_counter\x18\x02 \x01(\x03\"\'\n\x14SaveCallLogsResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xb6\x02\n\x0cVoipCallLogs\x12\x8e\x01\n\nGetVoipLog\x12\x1e.ondewo.vtsi.GetVoipLogRequest\x1a\x1f.ondewo.vtsi.GetVoipLogResponse\"?\x82\xd3\xe4\x93\x02\x39\"4/v2/{session=projects/*/agent/sessions/*}:GetVoipLog:\x01*\x12\x94\x01\n\x14\x41\x63tivateSaveCallLogs\x12\x16.google.protobuf.Empty\x1a!.ondewo.vtsi.SaveCallLogsResponse\"A\x82\xd3\xe4\x93\x02;\"6/v2/{session=projects/*/agent/sessions/*}:SaveCallLogs:\x01*b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,ondewo_dot_sip_dot_sip__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETCALLIDSREQUEST = _descriptor.Descriptor(
  name='GetCallIdsRequest',
  full_name='ondewo.vtsi.GetCallIdsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sip_id', full_name='ondewo.vtsi.GetCallIdsRequest.sip_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=124,
  serialized_end=159,
)


_GETCALLIDSRESPONSE = _descriptor.Descriptor(
  name='GetCallIdsResponse',
  full_name='ondewo.vtsi.GetCallIdsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sip_id', full_name='ondewo.vtsi.GetCallIdsResponse.sip_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='call_ids', full_name='ondewo.vtsi.GetCallIdsResponse.call_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=161,
  serialized_end=215,
)


_GETVOIPLOGREQUEST = _descriptor.Descriptor(
  name='GetVoipLogRequest',
  full_name='ondewo.vtsi.GetVoipLogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_id', full_name='ondewo.vtsi.GetVoipLogRequest.call_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=217,
  serialized_end=253,
)


_GETVOIPLOGRESPONSE = _descriptor.Descriptor(
  name='GetVoipLogResponse',
  full_name='ondewo.vtsi.GetVoipLogResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='active_log', full_name='ondewo.vtsi.GetVoipLogResponse.active_log', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='done_logs', full_name='ondewo.vtsi.GetVoipLogResponse.done_logs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=255,
  serialized_end=358,
)


_VOIPLOG = _descriptor.Descriptor(
  name='VoipLog',
  full_name='ondewo.vtsi.VoipLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_id', full_name='ondewo.vtsi.VoipLog.call_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='ondewo.vtsi.VoipLog.start_time', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='ondewo.vtsi.VoipLog.end_time', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_history', full_name='ondewo.vtsi.VoipLog.status_history', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counters', full_name='ondewo.vtsi.VoipLog.counters', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=361,
  serialized_end=513,
)


_COUNTERS = _descriptor.Descriptor(
  name='Counters',
  full_name='ondewo.vtsi.Counters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fifteen_s_counter', full_name='ondewo.vtsi.Counters.fifteen_s_counter', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sixty_s_counter', full_name='ondewo.vtsi.Counters.sixty_s_counter', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=515,
  serialized_end=577,
)


_SAVECALLLOGSRESPONSE = _descriptor.Descriptor(
  name='SaveCallLogsResponse',
  full_name='ondewo.vtsi.SaveCallLogsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='ondewo.vtsi.SaveCallLogsResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=579,
  serialized_end=618,
)

_GETVOIPLOGRESPONSE.fields_by_name['active_log'].message_type = _VOIPLOG
_GETVOIPLOGRESPONSE.fields_by_name['done_logs'].message_type = _VOIPLOG
_VOIPLOG.fields_by_name['status_history'].message_type = ondewo_dot_sip_dot_sip__pb2._SIPSTATUS
_VOIPLOG.fields_by_name['counters'].message_type = _COUNTERS
DESCRIPTOR.message_types_by_name['GetCallIdsRequest'] = _GETCALLIDSREQUEST
DESCRIPTOR.message_types_by_name['GetCallIdsResponse'] = _GETCALLIDSRESPONSE
DESCRIPTOR.message_types_by_name['GetVoipLogRequest'] = _GETVOIPLOGREQUEST
DESCRIPTOR.message_types_by_name['GetVoipLogResponse'] = _GETVOIPLOGRESPONSE
DESCRIPTOR.message_types_by_name['VoipLog'] = _VOIPLOG
DESCRIPTOR.message_types_by_name['Counters'] = _COUNTERS
DESCRIPTOR.message_types_by_name['SaveCallLogsResponse'] = _SAVECALLLOGSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCallIdsRequest = _reflection.GeneratedProtocolMessageType('GetCallIdsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCALLIDSREQUEST,
  '__module__' : 'ondewo.vtsi.call_log_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetCallIdsRequest)
  })
_sym_db.RegisterMessage(GetCallIdsRequest)

GetCallIdsResponse = _reflection.GeneratedProtocolMessageType('GetCallIdsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCALLIDSRESPONSE,
  '__module__' : 'ondewo.vtsi.call_log_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetCallIdsResponse)
  })
_sym_db.RegisterMessage(GetCallIdsResponse)

GetVoipLogRequest = _reflection.GeneratedProtocolMessageType('GetVoipLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVOIPLOGREQUEST,
  '__module__' : 'ondewo.vtsi.call_log_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetVoipLogRequest)
  })
_sym_db.RegisterMessage(GetVoipLogRequest)

GetVoipLogResponse = _reflection.GeneratedProtocolMessageType('GetVoipLogResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVOIPLOGRESPONSE,
  '__module__' : 'ondewo.vtsi.call_log_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.GetVoipLogResponse)
  })
_sym_db.RegisterMessage(GetVoipLogResponse)

VoipLog = _reflection.GeneratedProtocolMessageType('VoipLog', (_message.Message,), {
  'DESCRIPTOR' : _VOIPLOG,
  '__module__' : 'ondewo.vtsi.call_log_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.VoipLog)
  })
_sym_db.RegisterMessage(VoipLog)

Counters = _reflection.GeneratedProtocolMessageType('Counters', (_message.Message,), {
  'DESCRIPTOR' : _COUNTERS,
  '__module__' : 'ondewo.vtsi.call_log_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.Counters)
  })
_sym_db.RegisterMessage(Counters)

SaveCallLogsResponse = _reflection.GeneratedProtocolMessageType('SaveCallLogsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAVECALLLOGSRESPONSE,
  '__module__' : 'ondewo.vtsi.call_log_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.vtsi.SaveCallLogsResponse)
  })
_sym_db.RegisterMessage(SaveCallLogsResponse)



_VOIPCALLLOGS = _descriptor.ServiceDescriptor(
  name='VoipCallLogs',
  full_name='ondewo.vtsi.VoipCallLogs',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=621,
  serialized_end=931,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetVoipLog',
    full_name='ondewo.vtsi.VoipCallLogs.GetVoipLog',
    index=0,
    containing_service=None,
    input_type=_GETVOIPLOGREQUEST,
    output_type=_GETVOIPLOGRESPONSE,
    serialized_options=b'\202\323\344\223\0029\"4/v2/{session=projects/*/agent/sessions/*}:GetVoipLog:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ActivateSaveCallLogs',
    full_name='ondewo.vtsi.VoipCallLogs.ActivateSaveCallLogs',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_SAVECALLLOGSRESPONSE,
    serialized_options=b'\202\323\344\223\002;\"6/v2/{session=projects/*/agent/sessions/*}:SaveCallLogs:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VOIPCALLLOGS)

DESCRIPTOR.services_by_name['VoipCallLogs'] = _VOIPCALLLOGS

# @@protoc_insertion_point(module_scope)
