# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tinkoff/invest/grpc/users.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from tinkoff.invest.grpc import common_pb2 as tinkoff_dot_invest_dot_grpc_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ftinkoff/invest/grpc/users.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a tinkoff/invest/grpc/common.proto\"\x14\n\x12GetAccountsRequest\"W\n\x13GetAccountsResponse\x12@\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32..tinkoff.public.invest.api.contract.v1.Account\"\xd7\x02\n\x07\x41\x63\x63ount\x12\n\n\x02id\x18\x01 \x01(\t\x12@\n\x04type\x18\x02 \x01(\x0e\x32\x32.tinkoff.public.invest.api.contract.v1.AccountType\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x44\n\x06status\x18\x04 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.AccountStatus\x12/\n\x0bopened_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x63losed_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12H\n\x0c\x61\x63\x63\x65ss_level\x18\x07 \x01(\x0e\x32\x32.tinkoff.public.invest.api.contract.v1.AccessLevel\"0\n\x1aGetMarginAttributesRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\"\xa8\x03\n\x1bGetMarginAttributesResponse\x12K\n\x10liquid_portfolio\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12J\n\x0fstarting_margin\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12I\n\x0eminimal_margin\x18\x03 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Q\n\x17\x66unds_sufficiency_level\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12R\n\x17\x61mount_of_missing_funds\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\"\x16\n\x14GetUserTariffRequest\"\xab\x01\n\x15GetUserTariffResponse\x12G\n\x0cunary_limits\x18\x01 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.UnaryLimit\x12I\n\rstream_limits\x18\x02 \x03(\x0b\x32\x32.tinkoff.public.invest.api.contract.v1.StreamLimit\"7\n\nUnaryLimit\x12\x18\n\x10limit_per_minute\x18\x01 \x01(\x05\x12\x0f\n\x07methods\x18\x02 \x03(\t\"-\n\x0bStreamLimit\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x0f\n\x07streams\x18\x02 \x03(\t\"\x10\n\x0eGetInfoRequest\"l\n\x0fGetInfoResponse\x12\x13\n\x0bprem_status\x18\x01 \x01(\x08\x12\x13\n\x0bqual_status\x18\x02 \x01(\x08\x12\x1f\n\x17qualified_for_work_with\x18\x03 \x03(\t\x12\x0e\n\x06tariff\x18\x04 \x01(\t*\x80\x01\n\x0b\x41\x63\x63ountType\x12\x1c\n\x18\x41\x43\x43OUNT_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x41\x43\x43OUNT_TYPE_TINKOFF\x10\x01\x12\x1c\n\x18\x41\x43\x43OUNT_TYPE_TINKOFF_IIS\x10\x02\x12\x1b\n\x17\x41\x43\x43OUNT_TYPE_INVEST_BOX\x10\x03*{\n\rAccountStatus\x12\x1e\n\x1a\x41\x43\x43OUNT_STATUS_UNSPECIFIED\x10\x00\x12\x16\n\x12\x41\x43\x43OUNT_STATUS_NEW\x10\x01\x12\x17\n\x13\x41\x43\x43OUNT_STATUS_OPEN\x10\x02\x12\x19\n\x15\x41\x43\x43OUNT_STATUS_CLOSED\x10\x03*\xa1\x01\n\x0b\x41\x63\x63\x65ssLevel\x12$\n ACCOUNT_ACCESS_LEVEL_UNSPECIFIED\x10\x00\x12$\n ACCOUNT_ACCESS_LEVEL_FULL_ACCESS\x10\x01\x12\"\n\x1e\x41\x43\x43OUNT_ACCESS_LEVEL_READ_ONLY\x10\x02\x12\"\n\x1e\x41\x43\x43OUNT_ACCESS_LEVEL_NO_ACCESS\x10\x03\x32\xbb\x04\n\x0cUsersService\x12\x84\x01\n\x0bGetAccounts\x12\x39.tinkoff.public.invest.api.contract.v1.GetAccountsRequest\x1a:.tinkoff.public.invest.api.contract.v1.GetAccountsResponse\x12\x9c\x01\n\x13GetMarginAttributes\x12\x41.tinkoff.public.invest.api.contract.v1.GetMarginAttributesRequest\x1a\x42.tinkoff.public.invest.api.contract.v1.GetMarginAttributesResponse\x12\x8a\x01\n\rGetUserTariff\x12;.tinkoff.public.invest.api.contract.v1.GetUserTariffRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetUserTariffResponse\x12x\n\x07GetInfo\x12\x35.tinkoff.public.invest.api.contract.v1.GetInfoRequest\x1a\x36.tinkoff.public.invest.api.contract.v1.GetInfoResponseBa\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_ACCOUNTTYPE = DESCRIPTOR.enum_types_by_name['AccountType']
AccountType = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTTYPE)
_ACCOUNTSTATUS = DESCRIPTOR.enum_types_by_name['AccountStatus']
AccountStatus = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTSTATUS)
_ACCESSLEVEL = DESCRIPTOR.enum_types_by_name['AccessLevel']
AccessLevel = enum_type_wrapper.EnumTypeWrapper(_ACCESSLEVEL)
ACCOUNT_TYPE_UNSPECIFIED = 0
ACCOUNT_TYPE_TINKOFF = 1
ACCOUNT_TYPE_TINKOFF_IIS = 2
ACCOUNT_TYPE_INVEST_BOX = 3
ACCOUNT_STATUS_UNSPECIFIED = 0
ACCOUNT_STATUS_NEW = 1
ACCOUNT_STATUS_OPEN = 2
ACCOUNT_STATUS_CLOSED = 3
ACCOUNT_ACCESS_LEVEL_UNSPECIFIED = 0
ACCOUNT_ACCESS_LEVEL_FULL_ACCESS = 1
ACCOUNT_ACCESS_LEVEL_READ_ONLY = 2
ACCOUNT_ACCESS_LEVEL_NO_ACCESS = 3


_GETACCOUNTSREQUEST = DESCRIPTOR.message_types_by_name['GetAccountsRequest']
_GETACCOUNTSRESPONSE = DESCRIPTOR.message_types_by_name['GetAccountsResponse']
_ACCOUNT = DESCRIPTOR.message_types_by_name['Account']
_GETMARGINATTRIBUTESREQUEST = DESCRIPTOR.message_types_by_name['GetMarginAttributesRequest']
_GETMARGINATTRIBUTESRESPONSE = DESCRIPTOR.message_types_by_name['GetMarginAttributesResponse']
_GETUSERTARIFFREQUEST = DESCRIPTOR.message_types_by_name['GetUserTariffRequest']
_GETUSERTARIFFRESPONSE = DESCRIPTOR.message_types_by_name['GetUserTariffResponse']
_UNARYLIMIT = DESCRIPTOR.message_types_by_name['UnaryLimit']
_STREAMLIMIT = DESCRIPTOR.message_types_by_name['StreamLimit']
_GETINFOREQUEST = DESCRIPTOR.message_types_by_name['GetInfoRequest']
_GETINFORESPONSE = DESCRIPTOR.message_types_by_name['GetInfoResponse']
GetAccountsRequest = _reflection.GeneratedProtocolMessageType('GetAccountsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTSREQUEST,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetAccountsRequest)
  })
_sym_db.RegisterMessage(GetAccountsRequest)

GetAccountsResponse = _reflection.GeneratedProtocolMessageType('GetAccountsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTSRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetAccountsResponse)
  })
_sym_db.RegisterMessage(GetAccountsResponse)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.Account)
  })
_sym_db.RegisterMessage(Account)

GetMarginAttributesRequest = _reflection.GeneratedProtocolMessageType('GetMarginAttributesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMARGINATTRIBUTESREQUEST,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetMarginAttributesRequest)
  })
_sym_db.RegisterMessage(GetMarginAttributesRequest)

GetMarginAttributesResponse = _reflection.GeneratedProtocolMessageType('GetMarginAttributesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMARGINATTRIBUTESRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetMarginAttributesResponse)
  })
_sym_db.RegisterMessage(GetMarginAttributesResponse)

GetUserTariffRequest = _reflection.GeneratedProtocolMessageType('GetUserTariffRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERTARIFFREQUEST,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetUserTariffRequest)
  })
_sym_db.RegisterMessage(GetUserTariffRequest)

GetUserTariffResponse = _reflection.GeneratedProtocolMessageType('GetUserTariffResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERTARIFFRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetUserTariffResponse)
  })
_sym_db.RegisterMessage(GetUserTariffResponse)

UnaryLimit = _reflection.GeneratedProtocolMessageType('UnaryLimit', (_message.Message,), {
  'DESCRIPTOR' : _UNARYLIMIT,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.UnaryLimit)
  })
_sym_db.RegisterMessage(UnaryLimit)

StreamLimit = _reflection.GeneratedProtocolMessageType('StreamLimit', (_message.Message,), {
  'DESCRIPTOR' : _STREAMLIMIT,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.StreamLimit)
  })
_sym_db.RegisterMessage(StreamLimit)

GetInfoRequest = _reflection.GeneratedProtocolMessageType('GetInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINFOREQUEST,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetInfoRequest)
  })
_sym_db.RegisterMessage(GetInfoRequest)

GetInfoResponse = _reflection.GeneratedProtocolMessageType('GetInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETINFORESPONSE,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetInfoResponse)
  })
_sym_db.RegisterMessage(GetInfoResponse)

_USERSSERVICE = DESCRIPTOR.services_by_name['UsersService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _ACCOUNTTYPE._serialized_start=1506
  _ACCOUNTTYPE._serialized_end=1634
  _ACCOUNTSTATUS._serialized_start=1636
  _ACCOUNTSTATUS._serialized_end=1759
  _ACCESSLEVEL._serialized_start=1762
  _ACCESSLEVEL._serialized_end=1923
  _GETACCOUNTSREQUEST._serialized_start=141
  _GETACCOUNTSREQUEST._serialized_end=161
  _GETACCOUNTSRESPONSE._serialized_start=163
  _GETACCOUNTSRESPONSE._serialized_end=250
  _ACCOUNT._serialized_start=253
  _ACCOUNT._serialized_end=596
  _GETMARGINATTRIBUTESREQUEST._serialized_start=598
  _GETMARGINATTRIBUTESREQUEST._serialized_end=646
  _GETMARGINATTRIBUTESRESPONSE._serialized_start=649
  _GETMARGINATTRIBUTESRESPONSE._serialized_end=1073
  _GETUSERTARIFFREQUEST._serialized_start=1075
  _GETUSERTARIFFREQUEST._serialized_end=1097
  _GETUSERTARIFFRESPONSE._serialized_start=1100
  _GETUSERTARIFFRESPONSE._serialized_end=1271
  _UNARYLIMIT._serialized_start=1273
  _UNARYLIMIT._serialized_end=1328
  _STREAMLIMIT._serialized_start=1330
  _STREAMLIMIT._serialized_end=1375
  _GETINFOREQUEST._serialized_start=1377
  _GETINFOREQUEST._serialized_end=1393
  _GETINFORESPONSE._serialized_start=1395
  _GETINFORESPONSE._serialized_end=1503
  _USERSSERVICE._serialized_start=1926
  _USERSSERVICE._serialized_end=2497
# @@protoc_insertion_point(module_scope)
