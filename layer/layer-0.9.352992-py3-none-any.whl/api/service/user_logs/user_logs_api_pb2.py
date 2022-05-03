# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/service/user_logs/user_logs_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layer.api.entity import user_log_line_pb2 as api_dot_entity_dot_user__log__line__pb2
from layer.api import ids_pb2 as api_dot_ids__pb2
from layer.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)api/service/user_logs/user_logs_api.proto\x12\x03\x61pi\x1a\x1e\x61pi/entity/user_log_line.proto\x1a\rapi/ids.proto\x1a\x17validate/validate.proto\"]\n\x19GetPipelineRunLogsRequest\x12$\n\x06run_id\x18\x01 \x01(\x0b\x32\n.api.RunIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x1a\n\x12\x63ontinuation_token\x18\x02 \x01(\t\"]\n\x1aGetPipelineRunLogsResponse\x12#\n\tlog_lines\x18\x01 \x03(\x0b\x32\x10.api.UserLogLine\x12\x1a\n\x12\x63ontinuation_token\x18\x02 \x01(\t\"J\n\"GetPipelineRunLogsStreamingRequest\x12$\n\x06run_id\x18\x01 \x01(\x0b\x32\n.api.RunIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"J\n#GetPipelineRunLogsStreamingResponse\x12#\n\tlog_lines\x18\x01 \x03(\x0b\x32\x10.api.UserLogLine2\xd8\x01\n\x0bUserLogsAPI\x12U\n\x12GetPipelineRunLogs\x12\x1e.api.GetPipelineRunLogsRequest\x1a\x1f.api.GetPipelineRunLogsResponse\x12r\n\x1bGetPipelineRunLogsStreaming\x12\'.api.GetPipelineRunLogsStreamingRequest\x1a(.api.GetPipelineRunLogsStreamingResponse0\x01\x42#\n\rcom.layer.apiB\x10UserLogsApiProtoP\x01\x62\x06proto3')



_GETPIPELINERUNLOGSREQUEST = DESCRIPTOR.message_types_by_name['GetPipelineRunLogsRequest']
_GETPIPELINERUNLOGSRESPONSE = DESCRIPTOR.message_types_by_name['GetPipelineRunLogsResponse']
_GETPIPELINERUNLOGSSTREAMINGREQUEST = DESCRIPTOR.message_types_by_name['GetPipelineRunLogsStreamingRequest']
_GETPIPELINERUNLOGSSTREAMINGRESPONSE = DESCRIPTOR.message_types_by_name['GetPipelineRunLogsStreamingResponse']
GetPipelineRunLogsRequest = _reflection.GeneratedProtocolMessageType('GetPipelineRunLogsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPIPELINERUNLOGSREQUEST,
  '__module__' : 'api.service.user_logs.user_logs_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetPipelineRunLogsRequest)
  })
_sym_db.RegisterMessage(GetPipelineRunLogsRequest)

GetPipelineRunLogsResponse = _reflection.GeneratedProtocolMessageType('GetPipelineRunLogsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPIPELINERUNLOGSRESPONSE,
  '__module__' : 'api.service.user_logs.user_logs_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetPipelineRunLogsResponse)
  })
_sym_db.RegisterMessage(GetPipelineRunLogsResponse)

GetPipelineRunLogsStreamingRequest = _reflection.GeneratedProtocolMessageType('GetPipelineRunLogsStreamingRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPIPELINERUNLOGSSTREAMINGREQUEST,
  '__module__' : 'api.service.user_logs.user_logs_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetPipelineRunLogsStreamingRequest)
  })
_sym_db.RegisterMessage(GetPipelineRunLogsStreamingRequest)

GetPipelineRunLogsStreamingResponse = _reflection.GeneratedProtocolMessageType('GetPipelineRunLogsStreamingResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPIPELINERUNLOGSSTREAMINGRESPONSE,
  '__module__' : 'api.service.user_logs.user_logs_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetPipelineRunLogsStreamingResponse)
  })
_sym_db.RegisterMessage(GetPipelineRunLogsStreamingResponse)

_USERLOGSAPI = DESCRIPTOR.services_by_name['UserLogsAPI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiB\020UserLogsApiProtoP\001'
  _GETPIPELINERUNLOGSREQUEST.fields_by_name['run_id']._options = None
  _GETPIPELINERUNLOGSREQUEST.fields_by_name['run_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETPIPELINERUNLOGSSTREAMINGREQUEST.fields_by_name['run_id']._options = None
  _GETPIPELINERUNLOGSSTREAMINGREQUEST.fields_by_name['run_id']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GETPIPELINERUNLOGSREQUEST._serialized_start=122
  _GETPIPELINERUNLOGSREQUEST._serialized_end=215
  _GETPIPELINERUNLOGSRESPONSE._serialized_start=217
  _GETPIPELINERUNLOGSRESPONSE._serialized_end=310
  _GETPIPELINERUNLOGSSTREAMINGREQUEST._serialized_start=312
  _GETPIPELINERUNLOGSSTREAMINGREQUEST._serialized_end=386
  _GETPIPELINERUNLOGSSTREAMINGRESPONSE._serialized_start=388
  _GETPIPELINERUNLOGSSTREAMINGRESPONSE._serialized_end=462
  _USERLOGSAPI._serialized_start=465
  _USERLOGSAPI._serialized_end=681
# @@protoc_insertion_point(module_scope)
