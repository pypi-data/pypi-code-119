# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/entity/organization_invite.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layer.api import ids_pb2 as api_dot_ids__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$api/entity/organization_invite.proto\x12\x03\x61pi\x1a\rapi/ids.proto\"\xc8\x01\n\x12OrganizationInvite\x12%\n\x02id\x18\x01 \x01(\x0b\x32\x19.api.OrganizationInviteId\x12\x31\n\x0forganization_id\x18\x02 \x01(\x0b\x32\x18.api.Auth0OrganizationId\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x1a\n\x05roles\x18\x04 \x03(\x0b\x32\x0b.api.RoleId\x12\x17\n\x0f\x61\x63tivation_link\x18\x05 \x01(\t\x12\x14\n\x0cinviter_name\x18\x06 \x01(\tB\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_ORGANIZATIONINVITE = DESCRIPTOR.message_types_by_name['OrganizationInvite']
OrganizationInvite = _reflection.GeneratedProtocolMessageType('OrganizationInvite', (_message.Message,), {
  'DESCRIPTOR' : _ORGANIZATIONINVITE,
  '__module__' : 'api.entity.organization_invite_pb2'
  # @@protoc_insertion_point(class_scope:api.OrganizationInvite)
  })
_sym_db.RegisterMessage(OrganizationInvite)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _ORGANIZATIONINVITE._serialized_start=61
  _ORGANIZATIONINVITE._serialized_end=261
# @@protoc_insertion_point(module_scope)
