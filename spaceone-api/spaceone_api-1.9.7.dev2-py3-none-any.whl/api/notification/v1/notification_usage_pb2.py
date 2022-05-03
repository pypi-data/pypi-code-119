# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/notification/v1/notification_usage.proto
"""Generated protocol buffer code."""
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5spaceone/api/notification/v1/notification_usage.proto\x12\x1cspaceone.api.notification.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"l\n\x16NotificationUsageQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x13\n\x0bprotocol_id\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"w\n\x15NotificationUsageInfo\x12\x13\n\x0bprotocol_id\x18\x01 \x01(\t\x12\x12\n\nusage_date\x18\x02 \x01(\t\x12\x13\n\x0busage_month\x18\x03 \x01(\t\x12\r\n\x05\x63ount\x18\x04 \x01(\x05\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"s\n\x16NotificationUsagesInfo\x12\x44\n\x07results\x18\x01 \x03(\x0b\x32\x33.spaceone.api.notification.v1.NotificationUsageInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"e\n\x1aNotificationUsageStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\xf4\x02\n\x11NotificationUsage\x12\xcf\x01\n\x04list\x12\x34.spaceone.api.notification.v1.NotificationUsageQuery\x1a\x34.spaceone.api.notification.v1.NotificationUsagesInfo\"[\x82\xd3\xe4\x93\x02U\x12$/notification/v1/notification-usagesZ-\"+/notification/v1/notification-usages/search\x12\x8c\x01\n\x04stat\x12\x38.spaceone.api.notification.v1.NotificationUsageStatQuery\x1a\x17.google.protobuf.Struct\"1\x82\xd3\xe4\x93\x02+\")/notification/v1/notification-usages/statb\x06proto3')



_NOTIFICATIONUSAGEQUERY = DESCRIPTOR.message_types_by_name['NotificationUsageQuery']
_NOTIFICATIONUSAGEINFO = DESCRIPTOR.message_types_by_name['NotificationUsageInfo']
_NOTIFICATIONUSAGESINFO = DESCRIPTOR.message_types_by_name['NotificationUsagesInfo']
_NOTIFICATIONUSAGESTATQUERY = DESCRIPTOR.message_types_by_name['NotificationUsageStatQuery']
NotificationUsageQuery = _reflection.GeneratedProtocolMessageType('NotificationUsageQuery', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFICATIONUSAGEQUERY,
  '__module__' : 'spaceone.api.notification.v1.notification_usage_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.notification.v1.NotificationUsageQuery)
  })
_sym_db.RegisterMessage(NotificationUsageQuery)

NotificationUsageInfo = _reflection.GeneratedProtocolMessageType('NotificationUsageInfo', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFICATIONUSAGEINFO,
  '__module__' : 'spaceone.api.notification.v1.notification_usage_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.notification.v1.NotificationUsageInfo)
  })
_sym_db.RegisterMessage(NotificationUsageInfo)

NotificationUsagesInfo = _reflection.GeneratedProtocolMessageType('NotificationUsagesInfo', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFICATIONUSAGESINFO,
  '__module__' : 'spaceone.api.notification.v1.notification_usage_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.notification.v1.NotificationUsagesInfo)
  })
_sym_db.RegisterMessage(NotificationUsagesInfo)

NotificationUsageStatQuery = _reflection.GeneratedProtocolMessageType('NotificationUsageStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFICATIONUSAGESTATQUERY,
  '__module__' : 'spaceone.api.notification.v1.notification_usage_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.notification.v1.NotificationUsageStatQuery)
  })
_sym_db.RegisterMessage(NotificationUsageStatQuery)

_NOTIFICATIONUSAGE = DESCRIPTOR.services_by_name['NotificationUsage']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NOTIFICATIONUSAGE.methods_by_name['list']._options = None
  _NOTIFICATIONUSAGE.methods_by_name['list']._serialized_options = b'\202\323\344\223\002U\022$/notification/v1/notification-usagesZ-\"+/notification/v1/notification-usages/search'
  _NOTIFICATIONUSAGE.methods_by_name['stat']._options = None
  _NOTIFICATIONUSAGE.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002+\")/notification/v1/notification-usages/stat'
  _NOTIFICATIONUSAGEQUERY._serialized_start=181
  _NOTIFICATIONUSAGEQUERY._serialized_end=289
  _NOTIFICATIONUSAGEINFO._serialized_start=291
  _NOTIFICATIONUSAGEINFO._serialized_end=410
  _NOTIFICATIONUSAGESINFO._serialized_start=412
  _NOTIFICATIONUSAGESINFO._serialized_end=527
  _NOTIFICATIONUSAGESTATQUERY._serialized_start=529
  _NOTIFICATIONUSAGESTATQUERY._serialized_end=630
  _NOTIFICATIONUSAGE._serialized_start=633
  _NOTIFICATIONUSAGE._serialized_end=1005
# @@protoc_insertion_point(module_scope)
