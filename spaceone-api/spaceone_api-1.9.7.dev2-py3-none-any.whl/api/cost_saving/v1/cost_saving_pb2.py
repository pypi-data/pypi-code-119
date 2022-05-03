# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/cost_saving/v1/cost_saving.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-spaceone/api/cost_saving/v1/cost_saving.proto\x12\x1bspaceone.api.cost_saving.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\x8f\x02\n\rRecordRequest\x12\x15\n\rresource_type\x18\x01 \x01(\t\x12<\n\x0bsaving_mode\x18\x02 \x01(\x0e\x32\'.spaceone.api.cost_saving.v1.SavingMode\x12\x30\n\x0f\x63\x61lc_dimensions\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x16\n\x0esaving_service\x18\x04 \x01(\t\x12\x11\n\tsaving_by\x18\x05 \x01(\t\x12\x13\n\x0bregion_code\x18\x06 \x01(\t\x12\x12\n\nproject_id\x18\x07 \x01(\t\x12\x10\n\x08provider\x18\x08 \x01(\t\x12\x11\n\tdomain_id\x18\t \x01(\t\"\xb3\x02\n\nRecordInfo\x12\x11\n\trecord_id\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12<\n\x0bsaving_mode\x18\x03 \x01(\x0e\x32\'.spaceone.api.cost_saving.v1.SavingMode\x12\x30\n\x0f\x63\x61lc_dimensions\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08provider\x18\x05 \x01(\t\x12\x13\n\x0bregion_code\x18\x06 \x01(\t\x12\x12\n\nproject_id\x18\x07 \x01(\t\x12\x11\n\tdomain_id\x18\x08 \x01(\t\x12\x16\n\x0esaving_service\x18\t \x01(\t\x12\x11\n\tsaving_by\x18\n \x01(\t\x12\x12\n\ncreated_at\x18\x0b \x01(\t\"\xcd\x01\n\x0f\x43ostSavingQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x13\n\x0bregion_code\x18\x05 \x01(\t\x12\x12\n\nproject_id\x18\x06 \x01(\t\x12\x16\n\x0esaving_service\x18\x07 \x01(\t\x12\x11\n\tsaving_by\x18\x08 \x01(\t\x12\x11\n\tdomain_id\x18\n \x01(\t\"^\n\x13\x43ostSavingStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"\xf1\x02\n\x0e\x43ostSavingInfo\x12\x16\n\x0e\x63ost_saving_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ost_normal\x18\x02 \x01(\x02\x12\x13\n\x0b\x63ost_saving\x18\x03 \x01(\x02\x12\x15\n\rsaving_result\x18\x04 \x01(\x02\x12\x10\n\x08provider\x18\x05 \x01(\t\x12\x15\n\rresource_type\x18\x06 \x01(\t\x12\x13\n\x0bregion_code\x18\x07 \x01(\t\x12\x12\n\nproject_id\x18\x08 \x01(\t\x12\x11\n\tdomain_id\x18\t \x01(\t\x12\x16\n\x0esaving_service\x18\n \x01(\t\x12\x11\n\tsaving_by\x18\x0b \x01(\t\x12\x30\n\x0f\x63\x61lc_dimensions\x18\x0c \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x17\n\x0fsaving_begin_at\x18\r \x01(\t\x12\x17\n\x0fsaving_duration\x18\x0e \x01(\x05\x12\x12\n\ncreated_at\x18\x0f \x01(\t\"d\n\x0f\x43ostSavingsInfo\x12<\n\x07results\x18\x01 \x03(\x0b\x32+.spaceone.api.cost_saving.v1.CostSavingInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05*3\n\nSavingMode\x12\r\n\tMODE_NONE\x10\x00\x12\n\n\x06SAVING\x10\x01\x12\n\n\x06NORMAL\x10\x02\x32\xbb\x03\n\nCostSaving\x12}\n\x06record\x12*.spaceone.api.cost_saving.v1.RecordRequest\x1a\'.spaceone.api.cost_saving.v1.RecordInfo\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x16/cost-saving/v1/record\x12\xaf\x01\n\x04list\x12,.spaceone.api.cost_saving.v1.CostSavingQuery\x1a,.spaceone.api.cost_saving.v1.CostSavingsInfo\"K\x82\xd3\xe4\x93\x02\x45\x12\x1c/cost-saving/v1/cost-savingsZ%\"#/cost-saving/v1/cost-savings/search\x12|\n\x04stat\x12\x30.spaceone.api.cost_saving.v1.CostSavingStatQuery\x1a\x17.google.protobuf.Struct\")\x82\xd3\xe4\x93\x02#\"!/cost-saving/v1/cost-savings/statb\x06proto3')

_SAVINGMODE = DESCRIPTOR.enum_types_by_name['SavingMode']
SavingMode = enum_type_wrapper.EnumTypeWrapper(_SAVINGMODE)
MODE_NONE = 0
SAVING = 1
NORMAL = 2


_RECORDREQUEST = DESCRIPTOR.message_types_by_name['RecordRequest']
_RECORDINFO = DESCRIPTOR.message_types_by_name['RecordInfo']
_COSTSAVINGQUERY = DESCRIPTOR.message_types_by_name['CostSavingQuery']
_COSTSAVINGSTATQUERY = DESCRIPTOR.message_types_by_name['CostSavingStatQuery']
_COSTSAVINGINFO = DESCRIPTOR.message_types_by_name['CostSavingInfo']
_COSTSAVINGSINFO = DESCRIPTOR.message_types_by_name['CostSavingsInfo']
RecordRequest = _reflection.GeneratedProtocolMessageType('RecordRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECORDREQUEST,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.RecordRequest)
  })
_sym_db.RegisterMessage(RecordRequest)

RecordInfo = _reflection.GeneratedProtocolMessageType('RecordInfo', (_message.Message,), {
  'DESCRIPTOR' : _RECORDINFO,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.RecordInfo)
  })
_sym_db.RegisterMessage(RecordInfo)

CostSavingQuery = _reflection.GeneratedProtocolMessageType('CostSavingQuery', (_message.Message,), {
  'DESCRIPTOR' : _COSTSAVINGQUERY,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.CostSavingQuery)
  })
_sym_db.RegisterMessage(CostSavingQuery)

CostSavingStatQuery = _reflection.GeneratedProtocolMessageType('CostSavingStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _COSTSAVINGSTATQUERY,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.CostSavingStatQuery)
  })
_sym_db.RegisterMessage(CostSavingStatQuery)

CostSavingInfo = _reflection.GeneratedProtocolMessageType('CostSavingInfo', (_message.Message,), {
  'DESCRIPTOR' : _COSTSAVINGINFO,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.CostSavingInfo)
  })
_sym_db.RegisterMessage(CostSavingInfo)

CostSavingsInfo = _reflection.GeneratedProtocolMessageType('CostSavingsInfo', (_message.Message,), {
  'DESCRIPTOR' : _COSTSAVINGSINFO,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.CostSavingsInfo)
  })
_sym_db.RegisterMessage(CostSavingsInfo)

_COSTSAVING = DESCRIPTOR.services_by_name['CostSaving']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COSTSAVING.methods_by_name['record']._options = None
  _COSTSAVING.methods_by_name['record']._serialized_options = b'\202\323\344\223\002\030\"\026/cost-saving/v1/record'
  _COSTSAVING.methods_by_name['list']._options = None
  _COSTSAVING.methods_by_name['list']._serialized_options = b'\202\323\344\223\002E\022\034/cost-saving/v1/cost-savingsZ%\"#/cost-saving/v1/cost-savings/search'
  _COSTSAVING.methods_by_name['stat']._options = None
  _COSTSAVING.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002#\"!/cost-saving/v1/cost-savings/stat'
  _SAVINGMODE._serialized_start=1534
  _SAVINGMODE._serialized_end=1585
  _RECORDREQUEST._serialized_start=173
  _RECORDREQUEST._serialized_end=444
  _RECORDINFO._serialized_start=447
  _RECORDINFO._serialized_end=754
  _COSTSAVINGQUERY._serialized_start=757
  _COSTSAVINGQUERY._serialized_end=962
  _COSTSAVINGSTATQUERY._serialized_start=964
  _COSTSAVINGSTATQUERY._serialized_end=1058
  _COSTSAVINGINFO._serialized_start=1061
  _COSTSAVINGINFO._serialized_end=1430
  _COSTSAVINGSINFO._serialized_start=1432
  _COSTSAVINGSINFO._serialized_end=1532
  _COSTSAVING._serialized_start=1588
  _COSTSAVING._serialized_end=2031
# @@protoc_insertion_point(module_scope)
