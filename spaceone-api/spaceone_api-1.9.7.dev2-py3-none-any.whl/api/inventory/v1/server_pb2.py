# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/inventory/v1/server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&spaceone/api/inventory/v1/server.proto\x12\x19spaceone.api.inventory.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"=\n\x0fServerReference\x12\x13\n\x0bresource_id\x18\x01 \x01(\t\x12\x15\n\rexternal_link\x18\x02 \x01(\t\"\xbe\x01\n\tServerNIC\x12\x14\n\x0c\x64\x65vice_index\x18\x01 \x01(\x05\x12\x0e\n\x06\x64\x65vice\x18\x02 \x01(\t\x12\x10\n\x08nic_type\x18\x03 \x01(\t\x12\x14\n\x0cip_addresses\x18\x04 \x03(\t\x12\x0c\n\x04\x63idr\x18\x05 \x01(\t\x12\x13\n\x0bmac_address\x18\x06 \x01(\t\x12\x19\n\x11public_ip_address\x18\x07 \x01(\t\x12%\n\x04tags\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\"z\n\nServerDisk\x12\x14\n\x0c\x64\x65vice_index\x18\x01 \x01(\x05\x12\x0e\n\x06\x64\x65vice\x18\x02 \x01(\t\x12\x11\n\tdisk_type\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\x02\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xdf\x04\n\x13\x43reateServerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x12primary_ip_address\x18\x02 \x01(\t\x12\x38\n\x07os_type\x18\x03 \x01(\x0e\x32\'.spaceone.api.inventory.v1.ServerOSType\x12\x0f\n\x07\x61\x63\x63ount\x18\x04 \x01(\t\x12\x15\n\rinstance_type\x18\x05 \x01(\t\x12\x13\n\x0blaunched_at\x18\x06 \x01(\t\x12\x10\n\x08provider\x18\x07 \x01(\t\x12\x1b\n\x13\x63loud_service_group\x18\x08 \x01(\t\x12\x1a\n\x12\x63loud_service_type\x18\t \x01(\t\x12\x13\n\x0bregion_code\x18\n \x01(\t\x12%\n\x04\x64\x61ta\x18\x15 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08metadata\x18\x16 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x32\n\x04nics\x18\x17 \x03(\x0b\x32$.spaceone.api.inventory.v1.ServerNIC\x12\x34\n\x05\x64isks\x18\x18 \x03(\x0b\x32%.spaceone.api.inventory.v1.ServerDisk\x12=\n\treference\x18\x19 \x01(\x0b\x32*.spaceone.api.inventory.v1.ServerReference\x12%\n\x04tags\x18\x1a \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nproject_id\x18\x1f \x01(\t\x12\x11\n\tdomain_id\x18  \x01(\t\"\xa3\x05\n\x13UpdateServerRequest\x12\x11\n\tserver_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1a\n\x12primary_ip_address\x18\x03 \x01(\t\x12\x38\n\x07os_type\x18\x04 \x01(\x0e\x32\'.spaceone.api.inventory.v1.ServerOSType\x12\x0f\n\x07\x61\x63\x63ount\x18\x05 \x01(\t\x12\x15\n\rinstance_type\x18\x06 \x01(\t\x12\x13\n\x0blaunched_at\x18\x07 \x01(\t\x12\x10\n\x08provider\x18\x08 \x01(\t\x12\x1b\n\x13\x63loud_service_group\x18\t \x01(\t\x12\x1a\n\x12\x63loud_service_type\x18\n \x01(\t\x12\x13\n\x0bregion_code\x18\x0b \x01(\t\x12%\n\x04\x64\x61ta\x18\x15 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08metadata\x18\x16 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x32\n\x04nics\x18\x17 \x03(\x0b\x32$.spaceone.api.inventory.v1.ServerNIC\x12\x34\n\x05\x64isks\x18\x18 \x03(\x0b\x32%.spaceone.api.inventory.v1.ServerDisk\x12=\n\treference\x18\x19 \x01(\x0b\x32*.spaceone.api.inventory.v1.ServerReference\x12%\n\x04tags\x18\x1a \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nproject_id\x18\x1f \x01(\t\x12\x11\n\tdomain_id\x18  \x01(\t\x12\x16\n\x0erelease_region\x18! \x01(\x08\x12\x17\n\x0frelease_project\x18\" \x01(\x08\"J\n\x14PinServerDataRequest\x12\x11\n\tserver_id\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"5\n\rServerRequest\x12\x11\n\tserver_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"F\n\x10GetServerRequest\x12\x11\n\tserver_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\xb9\x03\n\x0bServerQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x11\n\tserver_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12\x1a\n\x12primary_ip_address\x18\x05 \x01(\t\x12\x14\n\x0cip_addresses\x18\x06 \x01(\t\x12\x38\n\x07os_type\x18\x07 \x01(\x0e\x32\'.spaceone.api.inventory.v1.ServerOSType\x12\x0f\n\x07\x61\x63\x63ount\x18\x08 \x01(\t\x12\x15\n\rinstance_type\x18\t \x01(\t\x12\x10\n\x08provider\x18\n \x01(\t\x12\x1b\n\x13\x63loud_service_group\x18\x0b \x01(\t\x12\x1a\n\x12\x63loud_service_type\x18\x0c \x01(\t\x12\x13\n\x0bregion_code\x18\r \x01(\t\x12\x19\n\x11resource_group_id\x18\x15 \x01(\t\x12\x12\n\nproject_id\x18\x16 \x01(\t\x12\x18\n\x10project_group_id\x18\x17 \x01(\t\x12\x11\n\tdomain_id\x18\x18 \x01(\t\"\xfc\x05\n\nServerInfo\x12\x11\n\tserver_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\x12\x1a\n\x12primary_ip_address\x18\x04 \x01(\t\x12\x14\n\x0cip_addresses\x18\x05 \x03(\t\x12\x38\n\x07os_type\x18\x06 \x01(\x0e\x32\'.spaceone.api.inventory.v1.ServerOSType\x12\x0f\n\x07\x61\x63\x63ount\x18\x07 \x01(\t\x12\x15\n\rinstance_type\x18\x08 \x01(\t\x12\x10\n\x08provider\x18\t \x01(\t\x12\x1b\n\x13\x63loud_service_group\x18\n \x01(\t\x12\x1a\n\x12\x63loud_service_type\x18\x0b \x01(\t\x12\x13\n\x0bregion_code\x18\x0c \x01(\t\x12%\n\x04\x64\x61ta\x18\x15 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08metadata\x18\x16 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x32\n\x04nics\x18\x17 \x03(\x0b\x32$.spaceone.api.inventory.v1.ServerNIC\x12\x34\n\x05\x64isks\x18\x18 \x03(\x0b\x32%.spaceone.api.inventory.v1.ServerDisk\x12=\n\treference\x18\x19 \x01(\x0b\x32*.spaceone.api.inventory.v1.ServerReference\x12%\n\x04tags\x18\x1a \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x30\n\x0f\x63ollection_info\x18\x1b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nproject_id\x18\x1f \x01(\t\x12\x11\n\tdomain_id\x18  \x01(\t\x12\x12\n\ncreated_at\x18) \x01(\t\x12\x12\n\nupdated_at\x18* \x01(\t\x12\x12\n\ndeleted_at\x18+ \x01(\t\x12\x13\n\x0blaunched_at\x18, \x01(\t\"Z\n\x0bServersInfo\x12\x36\n\x07results\x18\x01 \x03(\x0b\x32%.spaceone.api.inventory.v1.ServerInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"u\n\x0fServerStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x19\n\x11resource_group_id\x18\x03 \x01(\t*8\n\x0cServerOSType\x12\x10\n\x0cOS_TYPE_NONE\x10\x00\x12\t\n\x05LINUX\x10\x01\x12\x0b\n\x07WINDOWS\x10\x02\x32\xb1\x07\n\x06Server\x12~\n\x06\x63reate\x12..spaceone.api.inventory.v1.CreateServerRequest\x1a%.spaceone.api.inventory.v1.ServerInfo\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/inventory/v1/servers\x12\x89\x01\n\x06update\x12..spaceone.api.inventory.v1.UpdateServerRequest\x1a%.spaceone.api.inventory.v1.ServerInfo\"(\x82\xd3\xe4\x93\x02\"\x1a /inventory/v1/server/{server_id}\x12\x95\x01\n\x08pin_data\x12/.spaceone.api.inventory.v1.PinServerDataRequest\x1a%.spaceone.api.inventory.v1.ServerInfo\"1\x82\xd3\xe4\x93\x02+\x1a)/inventory/v1/server/{server_id}/pin-data\x12t\n\x06\x64\x65lete\x12(.spaceone.api.inventory.v1.ServerRequest\x1a\x16.google.protobuf.Empty\"(\x82\xd3\xe4\x93\x02\"* /inventory/v1/server/{server_id}\x12\x83\x01\n\x03get\x12+.spaceone.api.inventory.v1.GetServerRequest\x1a%.spaceone.api.inventory.v1.ServerInfo\"(\x82\xd3\xe4\x93\x02\"\x12 /inventory/v1/server/{server_id}\x12\x95\x01\n\x04list\x12&.spaceone.api.inventory.v1.ServerQuery\x1a&.spaceone.api.inventory.v1.ServersInfo\"=\x82\xd3\xe4\x93\x02\x37\x12\x15/inventory/v1/serversZ\x1e\"\x1c/inventory/v1/servers/search\x12o\n\x04stat\x12*.spaceone.api.inventory.v1.ServerStatQuery\x1a\x17.google.protobuf.Struct\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/inventory/v1/servers/statb\x06proto3')

_SERVEROSTYPE = DESCRIPTOR.enum_types_by_name['ServerOSType']
ServerOSType = enum_type_wrapper.EnumTypeWrapper(_SERVEROSTYPE)
OS_TYPE_NONE = 0
LINUX = 1
WINDOWS = 2


_SERVERREFERENCE = DESCRIPTOR.message_types_by_name['ServerReference']
_SERVERNIC = DESCRIPTOR.message_types_by_name['ServerNIC']
_SERVERDISK = DESCRIPTOR.message_types_by_name['ServerDisk']
_CREATESERVERREQUEST = DESCRIPTOR.message_types_by_name['CreateServerRequest']
_UPDATESERVERREQUEST = DESCRIPTOR.message_types_by_name['UpdateServerRequest']
_PINSERVERDATAREQUEST = DESCRIPTOR.message_types_by_name['PinServerDataRequest']
_SERVERREQUEST = DESCRIPTOR.message_types_by_name['ServerRequest']
_GETSERVERREQUEST = DESCRIPTOR.message_types_by_name['GetServerRequest']
_SERVERQUERY = DESCRIPTOR.message_types_by_name['ServerQuery']
_SERVERINFO = DESCRIPTOR.message_types_by_name['ServerInfo']
_SERVERSINFO = DESCRIPTOR.message_types_by_name['ServersInfo']
_SERVERSTATQUERY = DESCRIPTOR.message_types_by_name['ServerStatQuery']
ServerReference = _reflection.GeneratedProtocolMessageType('ServerReference', (_message.Message,), {
  'DESCRIPTOR' : _SERVERREFERENCE,
  '__module__' : 'spaceone.api.inventory.v1.server_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.ServerReference)
  })
_sym_db.RegisterMessage(ServerReference)

ServerNIC = _reflection.GeneratedProtocolMessageType('ServerNIC', (_message.Message,), {
  'DESCRIPTOR' : _SERVERNIC,
  '__module__' : 'spaceone.api.inventory.v1.server_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.ServerNIC)
  })
_sym_db.RegisterMessage(ServerNIC)

ServerDisk = _reflection.GeneratedProtocolMessageType('ServerDisk', (_message.Message,), {
  'DESCRIPTOR' : _SERVERDISK,
  '__module__' : 'spaceone.api.inventory.v1.server_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.ServerDisk)
  })
_sym_db.RegisterMessage(ServerDisk)

CreateServerRequest = _reflection.GeneratedProtocolMessageType('CreateServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVERREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.server_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.CreateServerRequest)
  })
_sym_db.RegisterMessage(CreateServerRequest)

UpdateServerRequest = _reflection.GeneratedProtocolMessageType('UpdateServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESERVERREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.server_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.UpdateServerRequest)
  })
_sym_db.RegisterMessage(UpdateServerRequest)

PinServerDataRequest = _reflection.GeneratedProtocolMessageType('PinServerDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINSERVERDATAREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.server_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.PinServerDataRequest)
  })
_sym_db.RegisterMessage(PinServerDataRequest)

ServerRequest = _reflection.GeneratedProtocolMessageType('ServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.server_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.ServerRequest)
  })
_sym_db.RegisterMessage(ServerRequest)

GetServerRequest = _reflection.GeneratedProtocolMessageType('GetServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.server_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.GetServerRequest)
  })
_sym_db.RegisterMessage(GetServerRequest)

ServerQuery = _reflection.GeneratedProtocolMessageType('ServerQuery', (_message.Message,), {
  'DESCRIPTOR' : _SERVERQUERY,
  '__module__' : 'spaceone.api.inventory.v1.server_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.ServerQuery)
  })
_sym_db.RegisterMessage(ServerQuery)

ServerInfo = _reflection.GeneratedProtocolMessageType('ServerInfo', (_message.Message,), {
  'DESCRIPTOR' : _SERVERINFO,
  '__module__' : 'spaceone.api.inventory.v1.server_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.ServerInfo)
  })
_sym_db.RegisterMessage(ServerInfo)

ServersInfo = _reflection.GeneratedProtocolMessageType('ServersInfo', (_message.Message,), {
  'DESCRIPTOR' : _SERVERSINFO,
  '__module__' : 'spaceone.api.inventory.v1.server_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.ServersInfo)
  })
_sym_db.RegisterMessage(ServersInfo)

ServerStatQuery = _reflection.GeneratedProtocolMessageType('ServerStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _SERVERSTATQUERY,
  '__module__' : 'spaceone.api.inventory.v1.server_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.ServerStatQuery)
  })
_sym_db.RegisterMessage(ServerStatQuery)

_SERVER = DESCRIPTOR.services_by_name['Server']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SERVER.methods_by_name['create']._options = None
  _SERVER.methods_by_name['create']._serialized_options = b'\202\323\344\223\002\027\"\025/inventory/v1/servers'
  _SERVER.methods_by_name['update']._options = None
  _SERVER.methods_by_name['update']._serialized_options = b'\202\323\344\223\002\"\032 /inventory/v1/server/{server_id}'
  _SERVER.methods_by_name['pin_data']._options = None
  _SERVER.methods_by_name['pin_data']._serialized_options = b'\202\323\344\223\002+\032)/inventory/v1/server/{server_id}/pin-data'
  _SERVER.methods_by_name['delete']._options = None
  _SERVER.methods_by_name['delete']._serialized_options = b'\202\323\344\223\002\"* /inventory/v1/server/{server_id}'
  _SERVER.methods_by_name['get']._options = None
  _SERVER.methods_by_name['get']._serialized_options = b'\202\323\344\223\002\"\022 /inventory/v1/server/{server_id}'
  _SERVER.methods_by_name['list']._options = None
  _SERVER.methods_by_name['list']._serialized_options = b'\202\323\344\223\0027\022\025/inventory/v1/serversZ\036\"\034/inventory/v1/servers/search'
  _SERVER.methods_by_name['stat']._options = None
  _SERVER.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002\034\"\032/inventory/v1/servers/stat'
  _SERVEROSTYPE._serialized_start=3485
  _SERVEROSTYPE._serialized_end=3541
  _SERVERREFERENCE._serialized_start=192
  _SERVERREFERENCE._serialized_end=253
  _SERVERNIC._serialized_start=256
  _SERVERNIC._serialized_end=446
  _SERVERDISK._serialized_start=448
  _SERVERDISK._serialized_end=570
  _CREATESERVERREQUEST._serialized_start=573
  _CREATESERVERREQUEST._serialized_end=1180
  _UPDATESERVERREQUEST._serialized_start=1183
  _UPDATESERVERREQUEST._serialized_end=1858
  _PINSERVERDATAREQUEST._serialized_start=1860
  _PINSERVERDATAREQUEST._serialized_end=1934
  _SERVERREQUEST._serialized_start=1936
  _SERVERREQUEST._serialized_end=1989
  _GETSERVERREQUEST._serialized_start=1991
  _GETSERVERREQUEST._serialized_end=2061
  _SERVERQUERY._serialized_start=2064
  _SERVERQUERY._serialized_end=2505
  _SERVERINFO._serialized_start=2508
  _SERVERINFO._serialized_end=3272
  _SERVERSINFO._serialized_start=3274
  _SERVERSINFO._serialized_end=3364
  _SERVERSTATQUERY._serialized_start=3366
  _SERVERSTATQUERY._serialized_end=3483
  _SERVER._serialized_start=3544
  _SERVER._serialized_end=4489
# @@protoc_insertion_point(module_scope)
