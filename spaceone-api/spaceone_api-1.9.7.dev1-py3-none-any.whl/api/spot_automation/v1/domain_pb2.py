# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/spot_automation/v1/domain.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,spaceone/api/spot_automation/v1/domain.proto\x12\x1fspaceone.api.spot_automation.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\"\n\rDomainRequest\x12\x11\n\tdomain_id\x18\x01 \x01(\t\"\xd6\x01\n\x0b\x44omainQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12G\n\x05state\x18\x02 \x01(\x0e\x32\x38.spaceone.api.spot_automation.v1.DomainQuery.DomainState\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"?\n\x0b\x44omainState\x12\x15\n\x11\x44OMAIN_STATE_NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\xa8\x01\n\nDomainInfo\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x46\n\x05state\x18\x02 \x01(\x0e\x32\x37.spaceone.api.spot_automation.v1.DomainInfo.DomainState\"?\n\x0b\x44omainState\x12\x15\n\x11\x44OMAIN_STATE_NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"`\n\x0b\x44omainsInfo\x12<\n\x07results\x18\x01 \x03(\x0b\x32+.spaceone.api.spot_automation.v1.DomainInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x32\xf8\x04\n\x06\x44omain\x12\x9c\x01\n\x06\x65nable\x12..spaceone.api.spot_automation.v1.DomainRequest\x1a+.spaceone.api.spot_automation.v1.DomainInfo\"5\x82\xd3\xe4\x93\x02/\x1a-/spot-automation/v1/domain/{domain_id}/enable\x12\x89\x01\n\x07\x64isable\x12..spaceone.api.spot_automation.v1.DomainRequest\x1a\x16.google.protobuf.Empty\"6\x82\xd3\xe4\x93\x02\x30\x1a./spot-automation/v1/domain/{domain_id}/disable\x12\x92\x01\n\x03get\x12..spaceone.api.spot_automation.v1.DomainRequest\x1a+.spaceone.api.spot_automation.v1.DomainInfo\".\x82\xd3\xe4\x93\x02(\x12&/spot-automation/v1/domain/{domain_id}\x12\xad\x01\n\x04list\x12,.spaceone.api.spot_automation.v1.DomainQuery\x1a,.spaceone.api.spot_automation.v1.DomainsInfo\"I\x82\xd3\xe4\x93\x02\x43\x12\x1b/spot-automation/v1/domainsZ$\"\"/spot-automation/v1/domains/searchb\x06proto3')



_DOMAINREQUEST = DESCRIPTOR.message_types_by_name['DomainRequest']
_DOMAINQUERY = DESCRIPTOR.message_types_by_name['DomainQuery']
_DOMAININFO = DESCRIPTOR.message_types_by_name['DomainInfo']
_DOMAINSINFO = DESCRIPTOR.message_types_by_name['DomainsInfo']
_DOMAINQUERY_DOMAINSTATE = _DOMAINQUERY.enum_types_by_name['DomainState']
_DOMAININFO_DOMAINSTATE = _DOMAININFO.enum_types_by_name['DomainState']
DomainRequest = _reflection.GeneratedProtocolMessageType('DomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINREQUEST,
  '__module__' : 'spaceone.api.spot_automation.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.v1.DomainRequest)
  })
_sym_db.RegisterMessage(DomainRequest)

DomainQuery = _reflection.GeneratedProtocolMessageType('DomainQuery', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINQUERY,
  '__module__' : 'spaceone.api.spot_automation.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.v1.DomainQuery)
  })
_sym_db.RegisterMessage(DomainQuery)

DomainInfo = _reflection.GeneratedProtocolMessageType('DomainInfo', (_message.Message,), {
  'DESCRIPTOR' : _DOMAININFO,
  '__module__' : 'spaceone.api.spot_automation.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.v1.DomainInfo)
  })
_sym_db.RegisterMessage(DomainInfo)

DomainsInfo = _reflection.GeneratedProtocolMessageType('DomainsInfo', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINSINFO,
  '__module__' : 'spaceone.api.spot_automation.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.spot_automation.v1.DomainsInfo)
  })
_sym_db.RegisterMessage(DomainsInfo)

_DOMAIN = DESCRIPTOR.services_by_name['Domain']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DOMAIN.methods_by_name['enable']._options = None
  _DOMAIN.methods_by_name['enable']._serialized_options = b'\202\323\344\223\002/\032-/spot-automation/v1/domain/{domain_id}/enable'
  _DOMAIN.methods_by_name['disable']._options = None
  _DOMAIN.methods_by_name['disable']._serialized_options = b'\202\323\344\223\0020\032./spot-automation/v1/domain/{domain_id}/disable'
  _DOMAIN.methods_by_name['get']._options = None
  _DOMAIN.methods_by_name['get']._serialized_options = b'\202\323\344\223\002(\022&/spot-automation/v1/domain/{domain_id}'
  _DOMAIN.methods_by_name['list']._options = None
  _DOMAIN.methods_by_name['list']._serialized_options = b'\202\323\344\223\002C\022\033/spot-automation/v1/domainsZ$\"\"/spot-automation/v1/domains/search'
  _DOMAINREQUEST._serialized_start=174
  _DOMAINREQUEST._serialized_end=208
  _DOMAINQUERY._serialized_start=211
  _DOMAINQUERY._serialized_end=425
  _DOMAINQUERY_DOMAINSTATE._serialized_start=362
  _DOMAINQUERY_DOMAINSTATE._serialized_end=425
  _DOMAININFO._serialized_start=428
  _DOMAININFO._serialized_end=596
  _DOMAININFO_DOMAINSTATE._serialized_start=362
  _DOMAININFO_DOMAINSTATE._serialized_end=425
  _DOMAINSINFO._serialized_start=598
  _DOMAINSINFO._serialized_end=694
  _DOMAIN._serialized_start=697
  _DOMAIN._serialized_end=1329
# @@protoc_insertion_point(module_scope)
