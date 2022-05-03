# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/entity/model.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layer.api import ids_pb2 as api_dot_ids__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61pi/entity/model.proto\x12\x03\x61pi\x1a\rapi/ids.proto\"\xed\x03\n\x05Model\x12\x18\n\x02id\x18\x01 \x01(\x0b\x32\x0c.api.ModelId\x12/\n\x11\x63ompute_fabric_id\x18\x02 \x01(\x0b\x32\x14.api.ComputeFabricId\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12$\n\x06owners\x18\x07 \x01(\x0b\x32\x14.api.Model.OwnerList\x12(\n\x0bversion_ids\x18\x08 \x03(\x0b\x32\x13.api.ModelVersionId\x12+\n\x10\x64\x65\x66\x61ult_train_id\x18\x0b \x01(\x0b\x32\x11.api.ModelTrainId\x12\x14\n\x0c\x64\x61te_created\x18\x0c \x01(\x03\x12\"\n\rcreated_by_id\x18\r \x01(\x0b\x32\x0b.api.UserId\x12,\n\x0forganization_id\x18\x0e \x01(\x0b\x32\x13.api.OrganizationId\x12\"\n\nproject_id\x18\x0f \x01(\x0b\x32\x0e.api.ProjectId\x12\r\n\x05likes\x18\x10 \x01(\t\x12\x11\n\tdownloads\x18\x11 \x01(\t\x1aK\n\tOwnerList\x12\x1d\n\x08user_ids\x18\x01 \x03(\x0b\x32\x0b.api.UserId\x12\x1f\n\tgroup_ids\x18\x02 \x03(\x0b\x32\x0c.api.GroupIdB\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_MODEL = DESCRIPTOR.message_types_by_name['Model']
_MODEL_OWNERLIST = _MODEL.nested_types_by_name['OwnerList']
Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {

  'OwnerList' : _reflection.GeneratedProtocolMessageType('OwnerList', (_message.Message,), {
    'DESCRIPTOR' : _MODEL_OWNERLIST,
    '__module__' : 'api.entity.model_pb2'
    # @@protoc_insertion_point(class_scope:api.Model.OwnerList)
    })
  ,
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'api.entity.model_pb2'
  # @@protoc_insertion_point(class_scope:api.Model)
  })
_sym_db.RegisterMessage(Model)
_sym_db.RegisterMessage(Model.OwnerList)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _MODEL._serialized_start=47
  _MODEL._serialized_end=540
  _MODEL_OWNERLIST._serialized_start=465
  _MODEL_OWNERLIST._serialized_end=540
# @@protoc_insertion_point(module_scope)
