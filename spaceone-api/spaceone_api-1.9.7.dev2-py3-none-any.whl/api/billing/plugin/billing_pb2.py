# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/billing/plugin/billing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)spaceone/api/billing/plugin/billing.proto\x12\x1bspaceone.api.billing.plugin\x1a\x1cgoogle/protobuf/struct.proto\"\xeb\x01\n\x12\x42illingDataRequest\x12(\n\x07options\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0bsecret_data\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0b\x61ggregation\x18\x04 \x03(\t\x12\r\n\x05start\x18\x05 \x01(\t\x12\x0b\n\x03\x65nd\x18\x06 \x01(\t\x12\x13\n\x0bgranularity\x18\x07 \x01(\t\x12\x0e\n\x06schema\x18\t \x01(\t\";\n\x0b\x42illingData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0c\n\x04\x63ost\x18\x02 \x01(\x01\x12\x10\n\x08\x63urrency\x18\x03 \x01(\t\"r\n\x0b\x42illingInfo\x12\x15\n\rresource_type\x18\x01 \x01(\t\x12>\n\x0c\x62illing_data\x18\x02 \x03(\x0b\x32(.spaceone.api.billing.plugin.BillingData\x12\x0c\n\x04name\x18\x03 \x01(\t\"k\n\x19PluginBillingDataResponse\x12\x39\n\x07results\x18\x01 \x03(\x0b\x32(.spaceone.api.billing.plugin.BillingInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x32\x80\x01\n\x07\x42illing\x12u\n\x08get_data\x12/.spaceone.api.billing.plugin.BillingDataRequest\x1a\x36.spaceone.api.billing.plugin.PluginBillingDataResponse\"\x00\x62\x06proto3')



_BILLINGDATAREQUEST = DESCRIPTOR.message_types_by_name['BillingDataRequest']
_BILLINGDATA = DESCRIPTOR.message_types_by_name['BillingData']
_BILLINGINFO = DESCRIPTOR.message_types_by_name['BillingInfo']
_PLUGINBILLINGDATARESPONSE = DESCRIPTOR.message_types_by_name['PluginBillingDataResponse']
BillingDataRequest = _reflection.GeneratedProtocolMessageType('BillingDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGDATAREQUEST,
  '__module__' : 'spaceone.api.billing.plugin.billing_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.billing.plugin.BillingDataRequest)
  })
_sym_db.RegisterMessage(BillingDataRequest)

BillingData = _reflection.GeneratedProtocolMessageType('BillingData', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGDATA,
  '__module__' : 'spaceone.api.billing.plugin.billing_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.billing.plugin.BillingData)
  })
_sym_db.RegisterMessage(BillingData)

BillingInfo = _reflection.GeneratedProtocolMessageType('BillingInfo', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGINFO,
  '__module__' : 'spaceone.api.billing.plugin.billing_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.billing.plugin.BillingInfo)
  })
_sym_db.RegisterMessage(BillingInfo)

PluginBillingDataResponse = _reflection.GeneratedProtocolMessageType('PluginBillingDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINBILLINGDATARESPONSE,
  '__module__' : 'spaceone.api.billing.plugin.billing_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.billing.plugin.PluginBillingDataResponse)
  })
_sym_db.RegisterMessage(PluginBillingDataResponse)

_BILLING = DESCRIPTOR.services_by_name['Billing']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BILLINGDATAREQUEST._serialized_start=105
  _BILLINGDATAREQUEST._serialized_end=340
  _BILLINGDATA._serialized_start=342
  _BILLINGDATA._serialized_end=401
  _BILLINGINFO._serialized_start=403
  _BILLINGINFO._serialized_end=517
  _PLUGINBILLINGDATARESPONSE._serialized_start=519
  _PLUGINBILLINGDATARESPONSE._serialized_end=626
  _BILLING._serialized_start=629
  _BILLING._serialized_end=757
# @@protoc_insertion_point(module_scope)
