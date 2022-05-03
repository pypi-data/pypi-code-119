# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/entity/run_filter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layer.api.entity import run_pb2 as api_dot_entity_dot_run__pb2
from layer.api import ids_pb2 as api_dot_ids__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from layer.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61pi/entity/run_filter.proto\x12\x03\x61pi\x1a\x14\x61pi/entity/run.proto\x1a\rapi/ids.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\"\x9c\x04\n\tRunFilter\x12;\n\x11\x63reated_by_filter\x18\x01 \x01(\x0b\x32\x1e.api.RunFilter.CreatedByFilterH\x00\x12\x34\n\rstatus_filter\x18\x02 \x01(\x0b\x32\x1b.api.RunFilter.StatusFilterH\x00\x12?\n\x13project_name_filter\x18\x03 \x01(\x0b\x32 .api.RunFilter.ProjectNameFilterH\x00\x12.\n\nage_filter\x18\x04 \x01(\x0b\x32\x18.api.RunFilter.AgeFilterH\x00\x1a<\n\x0f\x43reatedByFilter\x12)\n\ncreated_by\x18\x01 \x01(\x0b\x32\x0b.api.UserIdB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x1a\x41\n\x0cStatusFilter\x12\x31\n\x0crun_statuses\x18\x01 \x03(\x0e\x32\x0f.api.Run.StatusB\n\xfa\x42\x07\x92\x01\x04\x08\x01\x18\x01\x1a\x32\n\x11ProjectNameFilter\x12\x1d\n\x0cproject_name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x1al\n\tAgeFilter\x12.\n\nafter_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x62\x65\x66ore_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\n\x06\x66ilterB\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_RUNFILTER = DESCRIPTOR.message_types_by_name['RunFilter']
_RUNFILTER_CREATEDBYFILTER = _RUNFILTER.nested_types_by_name['CreatedByFilter']
_RUNFILTER_STATUSFILTER = _RUNFILTER.nested_types_by_name['StatusFilter']
_RUNFILTER_PROJECTNAMEFILTER = _RUNFILTER.nested_types_by_name['ProjectNameFilter']
_RUNFILTER_AGEFILTER = _RUNFILTER.nested_types_by_name['AgeFilter']
RunFilter = _reflection.GeneratedProtocolMessageType('RunFilter', (_message.Message,), {

  'CreatedByFilter' : _reflection.GeneratedProtocolMessageType('CreatedByFilter', (_message.Message,), {
    'DESCRIPTOR' : _RUNFILTER_CREATEDBYFILTER,
    '__module__' : 'api.entity.run_filter_pb2'
    # @@protoc_insertion_point(class_scope:api.RunFilter.CreatedByFilter)
    })
  ,

  'StatusFilter' : _reflection.GeneratedProtocolMessageType('StatusFilter', (_message.Message,), {
    'DESCRIPTOR' : _RUNFILTER_STATUSFILTER,
    '__module__' : 'api.entity.run_filter_pb2'
    # @@protoc_insertion_point(class_scope:api.RunFilter.StatusFilter)
    })
  ,

  'ProjectNameFilter' : _reflection.GeneratedProtocolMessageType('ProjectNameFilter', (_message.Message,), {
    'DESCRIPTOR' : _RUNFILTER_PROJECTNAMEFILTER,
    '__module__' : 'api.entity.run_filter_pb2'
    # @@protoc_insertion_point(class_scope:api.RunFilter.ProjectNameFilter)
    })
  ,

  'AgeFilter' : _reflection.GeneratedProtocolMessageType('AgeFilter', (_message.Message,), {
    'DESCRIPTOR' : _RUNFILTER_AGEFILTER,
    '__module__' : 'api.entity.run_filter_pb2'
    # @@protoc_insertion_point(class_scope:api.RunFilter.AgeFilter)
    })
  ,
  'DESCRIPTOR' : _RUNFILTER,
  '__module__' : 'api.entity.run_filter_pb2'
  # @@protoc_insertion_point(class_scope:api.RunFilter)
  })
_sym_db.RegisterMessage(RunFilter)
_sym_db.RegisterMessage(RunFilter.CreatedByFilter)
_sym_db.RegisterMessage(RunFilter.StatusFilter)
_sym_db.RegisterMessage(RunFilter.ProjectNameFilter)
_sym_db.RegisterMessage(RunFilter.AgeFilter)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _RUNFILTER_CREATEDBYFILTER.fields_by_name['created_by']._options = None
  _RUNFILTER_CREATEDBYFILTER.fields_by_name['created_by']._serialized_options = b'\372B\005\212\001\002\020\001'
  _RUNFILTER_STATUSFILTER.fields_by_name['run_statuses']._options = None
  _RUNFILTER_STATUSFILTER.fields_by_name['run_statuses']._serialized_options = b'\372B\007\222\001\004\010\001\030\001'
  _RUNFILTER_PROJECTNAMEFILTER.fields_by_name['project_name']._options = None
  _RUNFILTER_PROJECTNAMEFILTER.fields_by_name['project_name']._serialized_options = b'\372B\004r\002\020\001'
  _RUNFILTER._serialized_start=132
  _RUNFILTER._serialized_end=672
  _RUNFILTER_CREATEDBYFILTER._serialized_start=373
  _RUNFILTER_CREATEDBYFILTER._serialized_end=433
  _RUNFILTER_STATUSFILTER._serialized_start=435
  _RUNFILTER_STATUSFILTER._serialized_end=500
  _RUNFILTER_PROJECTNAMEFILTER._serialized_start=502
  _RUNFILTER_PROJECTNAMEFILTER._serialized_end=552
  _RUNFILTER_AGEFILTER._serialized_start=554
  _RUNFILTER_AGEFILTER._serialized_end=662
# @@protoc_insertion_point(module_scope)
