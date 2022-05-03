# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: strmprivacy/api/streams/v1/streams_v1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from strmprivacy.api.entities.v1 import entities_v1_pb2 as strmprivacy_dot_api_dot_entities_dot_v1_dot_entities__v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+strmprivacy/api/streams/v1/streams_v1.proto\x12\x1astrmprivacy.api.streams.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a-strmprivacy/api/entities/v1/entities_v1.proto\";\n\x12ListStreamsRequest\x12\x12\n\nbilling_id\x18\x01 \x01(\t\x12\x11\n\trecursive\x18\x02 \x01(\x08\"O\n\x13ListStreamsResponse\x12\x38\n\x07streams\x18\x01 \x03(\x0b\x32\'.strmprivacy.api.entities.v1.StreamTree\"0\n\x1aListExtendedStreamsRequest\x12\x12\n\nclient_ids\x18\x01 \x03(\t\"d\n\x1bListExtendedStreamsResponse\x12\x45\n\x10\x65xtended_streams\x18\x01 \x03(\x0b\x32+.strmprivacy.api.entities.v1.ExtendedStream\"g\n\x13\x44\x65leteStreamRequest\x12\x38\n\x03ref\x18\x01 \x01(\x0b\x32&.strmprivacy.api.entities.v1.StreamRefB\x03\xe0\x41\x02\x12\x16\n\trecursive\x18\x02 \x01(\x08\x42\x03\xe0\x41\x02\"\x16\n\x14\x44\x65leteStreamResponse\"O\n\x13\x43reateStreamRequest\x12\x38\n\x06stream\x18\x01 \x01(\x0b\x32#.strmprivacy.api.entities.v1.StreamB\x03\xe0\x41\x02\"K\n\x14\x43reateStreamResponse\x12\x33\n\x06stream\x18\x01 \x01(\x0b\x32#.strmprivacy.api.entities.v1.Stream\"d\n\x10GetStreamRequest\x12\x38\n\x03ref\x18\x01 \x01(\x0b\x32&.strmprivacy.api.entities.v1.StreamRefB\x03\xe0\x41\x02\x12\x16\n\trecursive\x18\x02 \x01(\x08\x42\x03\xe0\x41\x02\"Q\n\x11GetStreamResponse\x12<\n\x0bstream_tree\x18\x01 \x01(\x0b\x32\'.strmprivacy.api.entities.v1.StreamTree2\xd9\x04\n\x0eStreamsService\x12n\n\x0bListStreams\x12..strmprivacy.api.streams.v1.ListStreamsRequest\x1a/.strmprivacy.api.streams.v1.ListStreamsResponse\x12\x86\x01\n\x13ListExtendedStreams\x12\x36.strmprivacy.api.streams.v1.ListExtendedStreamsRequest\x1a\x37.strmprivacy.api.streams.v1.ListExtendedStreamsResponse\x12h\n\tGetStream\x12,.strmprivacy.api.streams.v1.GetStreamRequest\x1a-.strmprivacy.api.streams.v1.GetStreamResponse\x12q\n\x0c\x44\x65leteStream\x12/.strmprivacy.api.streams.v1.DeleteStreamRequest\x1a\x30.strmprivacy.api.streams.v1.DeleteStreamResponse\x12q\n\x0c\x43reateStream\x12/.strmprivacy.api.streams.v1.CreateStreamRequest\x1a\x30.strmprivacy.api.streams.v1.CreateStreamResponseBf\n\x1dio.strmprivacy.api.streams.v1P\x01ZCgithub.com/strmprivacy/api-definitions-go/v2/api/streams/v1;streamsb\x06proto3')



_LISTSTREAMSREQUEST = DESCRIPTOR.message_types_by_name['ListStreamsRequest']
_LISTSTREAMSRESPONSE = DESCRIPTOR.message_types_by_name['ListStreamsResponse']
_LISTEXTENDEDSTREAMSREQUEST = DESCRIPTOR.message_types_by_name['ListExtendedStreamsRequest']
_LISTEXTENDEDSTREAMSRESPONSE = DESCRIPTOR.message_types_by_name['ListExtendedStreamsResponse']
_DELETESTREAMREQUEST = DESCRIPTOR.message_types_by_name['DeleteStreamRequest']
_DELETESTREAMRESPONSE = DESCRIPTOR.message_types_by_name['DeleteStreamResponse']
_CREATESTREAMREQUEST = DESCRIPTOR.message_types_by_name['CreateStreamRequest']
_CREATESTREAMRESPONSE = DESCRIPTOR.message_types_by_name['CreateStreamResponse']
_GETSTREAMREQUEST = DESCRIPTOR.message_types_by_name['GetStreamRequest']
_GETSTREAMRESPONSE = DESCRIPTOR.message_types_by_name['GetStreamResponse']
ListStreamsRequest = _reflection.GeneratedProtocolMessageType('ListStreamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSTREAMSREQUEST,
  '__module__' : 'strmprivacy.api.streams.v1.streams_v1_pb2'
  # @@protoc_insertion_point(class_scope:strmprivacy.api.streams.v1.ListStreamsRequest)
  })
_sym_db.RegisterMessage(ListStreamsRequest)

ListStreamsResponse = _reflection.GeneratedProtocolMessageType('ListStreamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSTREAMSRESPONSE,
  '__module__' : 'strmprivacy.api.streams.v1.streams_v1_pb2'
  # @@protoc_insertion_point(class_scope:strmprivacy.api.streams.v1.ListStreamsResponse)
  })
_sym_db.RegisterMessage(ListStreamsResponse)

ListExtendedStreamsRequest = _reflection.GeneratedProtocolMessageType('ListExtendedStreamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTEXTENDEDSTREAMSREQUEST,
  '__module__' : 'strmprivacy.api.streams.v1.streams_v1_pb2'
  # @@protoc_insertion_point(class_scope:strmprivacy.api.streams.v1.ListExtendedStreamsRequest)
  })
_sym_db.RegisterMessage(ListExtendedStreamsRequest)

ListExtendedStreamsResponse = _reflection.GeneratedProtocolMessageType('ListExtendedStreamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTEXTENDEDSTREAMSRESPONSE,
  '__module__' : 'strmprivacy.api.streams.v1.streams_v1_pb2'
  # @@protoc_insertion_point(class_scope:strmprivacy.api.streams.v1.ListExtendedStreamsResponse)
  })
_sym_db.RegisterMessage(ListExtendedStreamsResponse)

DeleteStreamRequest = _reflection.GeneratedProtocolMessageType('DeleteStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESTREAMREQUEST,
  '__module__' : 'strmprivacy.api.streams.v1.streams_v1_pb2'
  # @@protoc_insertion_point(class_scope:strmprivacy.api.streams.v1.DeleteStreamRequest)
  })
_sym_db.RegisterMessage(DeleteStreamRequest)

DeleteStreamResponse = _reflection.GeneratedProtocolMessageType('DeleteStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETESTREAMRESPONSE,
  '__module__' : 'strmprivacy.api.streams.v1.streams_v1_pb2'
  # @@protoc_insertion_point(class_scope:strmprivacy.api.streams.v1.DeleteStreamResponse)
  })
_sym_db.RegisterMessage(DeleteStreamResponse)

CreateStreamRequest = _reflection.GeneratedProtocolMessageType('CreateStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESTREAMREQUEST,
  '__module__' : 'strmprivacy.api.streams.v1.streams_v1_pb2'
  # @@protoc_insertion_point(class_scope:strmprivacy.api.streams.v1.CreateStreamRequest)
  })
_sym_db.RegisterMessage(CreateStreamRequest)

CreateStreamResponse = _reflection.GeneratedProtocolMessageType('CreateStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESTREAMRESPONSE,
  '__module__' : 'strmprivacy.api.streams.v1.streams_v1_pb2'
  # @@protoc_insertion_point(class_scope:strmprivacy.api.streams.v1.CreateStreamResponse)
  })
_sym_db.RegisterMessage(CreateStreamResponse)

GetStreamRequest = _reflection.GeneratedProtocolMessageType('GetStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTREAMREQUEST,
  '__module__' : 'strmprivacy.api.streams.v1.streams_v1_pb2'
  # @@protoc_insertion_point(class_scope:strmprivacy.api.streams.v1.GetStreamRequest)
  })
_sym_db.RegisterMessage(GetStreamRequest)

GetStreamResponse = _reflection.GeneratedProtocolMessageType('GetStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTREAMRESPONSE,
  '__module__' : 'strmprivacy.api.streams.v1.streams_v1_pb2'
  # @@protoc_insertion_point(class_scope:strmprivacy.api.streams.v1.GetStreamResponse)
  })
_sym_db.RegisterMessage(GetStreamResponse)

_STREAMSSERVICE = DESCRIPTOR.services_by_name['StreamsService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035io.strmprivacy.api.streams.v1P\001ZCgithub.com/strmprivacy/api-definitions-go/v2/api/streams/v1;streams'
  _DELETESTREAMREQUEST.fields_by_name['ref']._options = None
  _DELETESTREAMREQUEST.fields_by_name['ref']._serialized_options = b'\340A\002'
  _DELETESTREAMREQUEST.fields_by_name['recursive']._options = None
  _DELETESTREAMREQUEST.fields_by_name['recursive']._serialized_options = b'\340A\002'
  _CREATESTREAMREQUEST.fields_by_name['stream']._options = None
  _CREATESTREAMREQUEST.fields_by_name['stream']._serialized_options = b'\340A\002'
  _GETSTREAMREQUEST.fields_by_name['ref']._options = None
  _GETSTREAMREQUEST.fields_by_name['ref']._serialized_options = b'\340A\002'
  _GETSTREAMREQUEST.fields_by_name['recursive']._options = None
  _GETSTREAMREQUEST.fields_by_name['recursive']._serialized_options = b'\340A\002'
  _LISTSTREAMSREQUEST._serialized_start=155
  _LISTSTREAMSREQUEST._serialized_end=214
  _LISTSTREAMSRESPONSE._serialized_start=216
  _LISTSTREAMSRESPONSE._serialized_end=295
  _LISTEXTENDEDSTREAMSREQUEST._serialized_start=297
  _LISTEXTENDEDSTREAMSREQUEST._serialized_end=345
  _LISTEXTENDEDSTREAMSRESPONSE._serialized_start=347
  _LISTEXTENDEDSTREAMSRESPONSE._serialized_end=447
  _DELETESTREAMREQUEST._serialized_start=449
  _DELETESTREAMREQUEST._serialized_end=552
  _DELETESTREAMRESPONSE._serialized_start=554
  _DELETESTREAMRESPONSE._serialized_end=576
  _CREATESTREAMREQUEST._serialized_start=578
  _CREATESTREAMREQUEST._serialized_end=657
  _CREATESTREAMRESPONSE._serialized_start=659
  _CREATESTREAMRESPONSE._serialized_end=734
  _GETSTREAMREQUEST._serialized_start=736
  _GETSTREAMREQUEST._serialized_end=836
  _GETSTREAMRESPONSE._serialized_start=838
  _GETSTREAMRESPONSE._serialized_end=919
  _STREAMSSERVICE._serialized_start=922
  _STREAMSSERVICE._serialized_end=1523
# @@protoc_insertion_point(module_scope)
