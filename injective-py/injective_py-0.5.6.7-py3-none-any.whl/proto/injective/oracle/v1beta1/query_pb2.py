# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/oracle/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2
from injective.oracle.v1beta1 import genesis_pb2 as injective_dot_oracle_dot_v1beta1_dot_genesis__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/oracle/v1beta1/query.proto',
  package='injective.oracle.v1beta1',
  syntax='proto3',
  serialized_options=b'ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$injective/oracle/v1beta1/query.proto\x12\x18injective.oracle.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a%injective/oracle/v1beta1/oracle.proto\x1a&injective/oracle/v1beta1/genesis.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x14\n\x12QueryParamsRequest\"M\n\x13QueryParamsResponse\x12\x36\n\x06params\x18\x01 \x01(\x0b\x32 .injective.oracle.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\"\x1a\n\x18QueryBandRelayersRequest\"-\n\x19QueryBandRelayersResponse\x12\x10\n\x08relayers\x18\x01 \x03(\t\"\x1d\n\x1bQueryBandPriceStatesRequest\"^\n\x1cQueryBandPriceStatesResponse\x12>\n\x0cprice_states\x18\x01 \x03(\x0b\x32(.injective.oracle.v1beta1.BandPriceState\" \n\x1eQueryBandIBCPriceStatesRequest\"a\n\x1fQueryBandIBCPriceStatesResponse\x12>\n\x0cprice_states\x18\x01 \x03(\x0b\x32(.injective.oracle.v1beta1.BandPriceState\"\"\n QueryPriceFeedPriceStatesRequest\"c\n!QueryPriceFeedPriceStatesResponse\x12>\n\x0cprice_states\x18\x01 \x03(\x0b\x32(.injective.oracle.v1beta1.PriceFeedState\"!\n\x1fQueryCoinbasePriceStatesRequest\"f\n QueryCoinbasePriceStatesResponse\x12\x42\n\x0cprice_states\x18\x01 \x03(\x0b\x32,.injective.oracle.v1beta1.CoinbasePriceState\"\x19\n\x17QueryModuleStateRequest\"Q\n\x18QueryModuleStateResponse\x12\x35\n\x05state\x18\x01 \x01(\x0b\x32&.injective.oracle.v1beta1.GenesisState2\x82\n\n\x05Query\x12\x8f\x01\n\x06Params\x12,.injective.oracle.v1beta1.QueryParamsRequest\x1a-.injective.oracle.v1beta1.QueryParamsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /injective/oracle/v1beta1/params\x12\xa8\x01\n\x0c\x42\x61ndRelayers\x12\x32.injective.oracle.v1beta1.QueryBandRelayersRequest\x1a\x33.injective.oracle.v1beta1.QueryBandRelayersResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/injective/oracle/v1beta1/band_relayers\x12\xb5\x01\n\x0f\x42\x61ndPriceStates\x12\x35.injective.oracle.v1beta1.QueryBandPriceStatesRequest\x1a\x36.injective.oracle.v1beta1.QueryBandPriceStatesResponse\"3\x82\xd3\xe4\x93\x02-\x12+/injective/oracle/v1beta1/band_price_states\x12\xc2\x01\n\x12\x42\x61ndIBCPriceStates\x12\x38.injective.oracle.v1beta1.QueryBandIBCPriceStatesRequest\x1a\x39.injective.oracle.v1beta1.QueryBandIBCPriceStatesResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//injective/oracle/v1beta1/band_ibc_price_states\x12\xc9\x01\n\x14PriceFeedPriceStates\x12:.injective.oracle.v1beta1.QueryPriceFeedPriceStatesRequest\x1a;.injective.oracle.v1beta1.QueryPriceFeedPriceStatesResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/injective/oracle/v1beta1/pricefeed_price_states\x12\xc5\x01\n\x13\x43oinbasePriceStates\x12\x39.injective.oracle.v1beta1.QueryCoinbasePriceStatesRequest\x1a:.injective.oracle.v1beta1.QueryCoinbasePriceStatesResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//injective/oracle/v1beta1/coinbase_price_states\x12\xaa\x01\n\x11OracleModuleState\x12\x31.injective.oracle.v1beta1.QueryModuleStateRequest\x1a\x32.injective.oracle.v1beta1.QueryModuleStateResponse\".\x82\xd3\xe4\x93\x02(\x12&/injective/oracle/v1beta1/module_stateBNZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/typesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,injective_dot_oracle_dot_v1beta1_dot_oracle__pb2.DESCRIPTOR,injective_dot_oracle_dot_v1beta1_dot_genesis__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_QUERYPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryParamsRequest',
  full_name='injective.oracle.v1beta1.QueryParamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=249,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryParamsResponse',
  full_name='injective.oracle.v1beta1.QueryParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='injective.oracle.v1beta1.QueryParamsResponse.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=328,
)


_QUERYBANDRELAYERSREQUEST = _descriptor.Descriptor(
  name='QueryBandRelayersRequest',
  full_name='injective.oracle.v1beta1.QueryBandRelayersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=330,
  serialized_end=356,
)


_QUERYBANDRELAYERSRESPONSE = _descriptor.Descriptor(
  name='QueryBandRelayersResponse',
  full_name='injective.oracle.v1beta1.QueryBandRelayersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='relayers', full_name='injective.oracle.v1beta1.QueryBandRelayersResponse.relayers', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=403,
)


_QUERYBANDPRICESTATESREQUEST = _descriptor.Descriptor(
  name='QueryBandPriceStatesRequest',
  full_name='injective.oracle.v1beta1.QueryBandPriceStatesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=434,
)


_QUERYBANDPRICESTATESRESPONSE = _descriptor.Descriptor(
  name='QueryBandPriceStatesResponse',
  full_name='injective.oracle.v1beta1.QueryBandPriceStatesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='price_states', full_name='injective.oracle.v1beta1.QueryBandPriceStatesResponse.price_states', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=530,
)


_QUERYBANDIBCPRICESTATESREQUEST = _descriptor.Descriptor(
  name='QueryBandIBCPriceStatesRequest',
  full_name='injective.oracle.v1beta1.QueryBandIBCPriceStatesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=564,
)


_QUERYBANDIBCPRICESTATESRESPONSE = _descriptor.Descriptor(
  name='QueryBandIBCPriceStatesResponse',
  full_name='injective.oracle.v1beta1.QueryBandIBCPriceStatesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='price_states', full_name='injective.oracle.v1beta1.QueryBandIBCPriceStatesResponse.price_states', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=566,
  serialized_end=663,
)


_QUERYPRICEFEEDPRICESTATESREQUEST = _descriptor.Descriptor(
  name='QueryPriceFeedPriceStatesRequest',
  full_name='injective.oracle.v1beta1.QueryPriceFeedPriceStatesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=665,
  serialized_end=699,
)


_QUERYPRICEFEEDPRICESTATESRESPONSE = _descriptor.Descriptor(
  name='QueryPriceFeedPriceStatesResponse',
  full_name='injective.oracle.v1beta1.QueryPriceFeedPriceStatesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='price_states', full_name='injective.oracle.v1beta1.QueryPriceFeedPriceStatesResponse.price_states', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=701,
  serialized_end=800,
)


_QUERYCOINBASEPRICESTATESREQUEST = _descriptor.Descriptor(
  name='QueryCoinbasePriceStatesRequest',
  full_name='injective.oracle.v1beta1.QueryCoinbasePriceStatesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=802,
  serialized_end=835,
)


_QUERYCOINBASEPRICESTATESRESPONSE = _descriptor.Descriptor(
  name='QueryCoinbasePriceStatesResponse',
  full_name='injective.oracle.v1beta1.QueryCoinbasePriceStatesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='price_states', full_name='injective.oracle.v1beta1.QueryCoinbasePriceStatesResponse.price_states', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=837,
  serialized_end=939,
)


_QUERYMODULESTATEREQUEST = _descriptor.Descriptor(
  name='QueryModuleStateRequest',
  full_name='injective.oracle.v1beta1.QueryModuleStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=941,
  serialized_end=966,
)


_QUERYMODULESTATERESPONSE = _descriptor.Descriptor(
  name='QueryModuleStateResponse',
  full_name='injective.oracle.v1beta1.QueryModuleStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='injective.oracle.v1beta1.QueryModuleStateResponse.state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=968,
  serialized_end=1049,
)

_QUERYPARAMSRESPONSE.fields_by_name['params'].message_type = injective_dot_oracle_dot_v1beta1_dot_oracle__pb2._PARAMS
_QUERYBANDPRICESTATESRESPONSE.fields_by_name['price_states'].message_type = injective_dot_oracle_dot_v1beta1_dot_oracle__pb2._BANDPRICESTATE
_QUERYBANDIBCPRICESTATESRESPONSE.fields_by_name['price_states'].message_type = injective_dot_oracle_dot_v1beta1_dot_oracle__pb2._BANDPRICESTATE
_QUERYPRICEFEEDPRICESTATESRESPONSE.fields_by_name['price_states'].message_type = injective_dot_oracle_dot_v1beta1_dot_oracle__pb2._PRICEFEEDSTATE
_QUERYCOINBASEPRICESTATESRESPONSE.fields_by_name['price_states'].message_type = injective_dot_oracle_dot_v1beta1_dot_oracle__pb2._COINBASEPRICESTATE
_QUERYMODULESTATERESPONSE.fields_by_name['state'].message_type = injective_dot_oracle_dot_v1beta1_dot_genesis__pb2._GENESISSTATE
DESCRIPTOR.message_types_by_name['QueryParamsRequest'] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryParamsResponse'] = _QUERYPARAMSRESPONSE
DESCRIPTOR.message_types_by_name['QueryBandRelayersRequest'] = _QUERYBANDRELAYERSREQUEST
DESCRIPTOR.message_types_by_name['QueryBandRelayersResponse'] = _QUERYBANDRELAYERSRESPONSE
DESCRIPTOR.message_types_by_name['QueryBandPriceStatesRequest'] = _QUERYBANDPRICESTATESREQUEST
DESCRIPTOR.message_types_by_name['QueryBandPriceStatesResponse'] = _QUERYBANDPRICESTATESRESPONSE
DESCRIPTOR.message_types_by_name['QueryBandIBCPriceStatesRequest'] = _QUERYBANDIBCPRICESTATESREQUEST
DESCRIPTOR.message_types_by_name['QueryBandIBCPriceStatesResponse'] = _QUERYBANDIBCPRICESTATESRESPONSE
DESCRIPTOR.message_types_by_name['QueryPriceFeedPriceStatesRequest'] = _QUERYPRICEFEEDPRICESTATESREQUEST
DESCRIPTOR.message_types_by_name['QueryPriceFeedPriceStatesResponse'] = _QUERYPRICEFEEDPRICESTATESRESPONSE
DESCRIPTOR.message_types_by_name['QueryCoinbasePriceStatesRequest'] = _QUERYCOINBASEPRICESTATESREQUEST
DESCRIPTOR.message_types_by_name['QueryCoinbasePriceStatesResponse'] = _QUERYCOINBASEPRICESTATESRESPONSE
DESCRIPTOR.message_types_by_name['QueryModuleStateRequest'] = _QUERYMODULESTATEREQUEST
DESCRIPTOR.message_types_by_name['QueryModuleStateResponse'] = _QUERYMODULESTATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)

QueryBandRelayersRequest = _reflection.GeneratedProtocolMessageType('QueryBandRelayersRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYBANDRELAYERSREQUEST,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryBandRelayersRequest)
  })
_sym_db.RegisterMessage(QueryBandRelayersRequest)

QueryBandRelayersResponse = _reflection.GeneratedProtocolMessageType('QueryBandRelayersResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYBANDRELAYERSRESPONSE,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryBandRelayersResponse)
  })
_sym_db.RegisterMessage(QueryBandRelayersResponse)

QueryBandPriceStatesRequest = _reflection.GeneratedProtocolMessageType('QueryBandPriceStatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYBANDPRICESTATESREQUEST,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryBandPriceStatesRequest)
  })
_sym_db.RegisterMessage(QueryBandPriceStatesRequest)

QueryBandPriceStatesResponse = _reflection.GeneratedProtocolMessageType('QueryBandPriceStatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYBANDPRICESTATESRESPONSE,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryBandPriceStatesResponse)
  })
_sym_db.RegisterMessage(QueryBandPriceStatesResponse)

QueryBandIBCPriceStatesRequest = _reflection.GeneratedProtocolMessageType('QueryBandIBCPriceStatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYBANDIBCPRICESTATESREQUEST,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryBandIBCPriceStatesRequest)
  })
_sym_db.RegisterMessage(QueryBandIBCPriceStatesRequest)

QueryBandIBCPriceStatesResponse = _reflection.GeneratedProtocolMessageType('QueryBandIBCPriceStatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYBANDIBCPRICESTATESRESPONSE,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryBandIBCPriceStatesResponse)
  })
_sym_db.RegisterMessage(QueryBandIBCPriceStatesResponse)

QueryPriceFeedPriceStatesRequest = _reflection.GeneratedProtocolMessageType('QueryPriceFeedPriceStatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPRICEFEEDPRICESTATESREQUEST,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryPriceFeedPriceStatesRequest)
  })
_sym_db.RegisterMessage(QueryPriceFeedPriceStatesRequest)

QueryPriceFeedPriceStatesResponse = _reflection.GeneratedProtocolMessageType('QueryPriceFeedPriceStatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPRICEFEEDPRICESTATESRESPONSE,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryPriceFeedPriceStatesResponse)
  })
_sym_db.RegisterMessage(QueryPriceFeedPriceStatesResponse)

QueryCoinbasePriceStatesRequest = _reflection.GeneratedProtocolMessageType('QueryCoinbasePriceStatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCOINBASEPRICESTATESREQUEST,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryCoinbasePriceStatesRequest)
  })
_sym_db.RegisterMessage(QueryCoinbasePriceStatesRequest)

QueryCoinbasePriceStatesResponse = _reflection.GeneratedProtocolMessageType('QueryCoinbasePriceStatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCOINBASEPRICESTATESRESPONSE,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryCoinbasePriceStatesResponse)
  })
_sym_db.RegisterMessage(QueryCoinbasePriceStatesResponse)

QueryModuleStateRequest = _reflection.GeneratedProtocolMessageType('QueryModuleStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMODULESTATEREQUEST,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryModuleStateRequest)
  })
_sym_db.RegisterMessage(QueryModuleStateRequest)

QueryModuleStateResponse = _reflection.GeneratedProtocolMessageType('QueryModuleStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMODULESTATERESPONSE,
  '__module__' : 'injective.oracle.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.QueryModuleStateResponse)
  })
_sym_db.RegisterMessage(QueryModuleStateResponse)


DESCRIPTOR._options = None
_QUERYPARAMSRESPONSE.fields_by_name['params']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='injective.oracle.v1beta1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1052,
  serialized_end=2334,
  methods=[
  _descriptor.MethodDescriptor(
    name='Params',
    full_name='injective.oracle.v1beta1.Query.Params',
    index=0,
    containing_service=None,
    input_type=_QUERYPARAMSREQUEST,
    output_type=_QUERYPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002\"\022 /injective/oracle/v1beta1/params',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BandRelayers',
    full_name='injective.oracle.v1beta1.Query.BandRelayers',
    index=1,
    containing_service=None,
    input_type=_QUERYBANDRELAYERSREQUEST,
    output_type=_QUERYBANDRELAYERSRESPONSE,
    serialized_options=b'\202\323\344\223\002)\022\'/injective/oracle/v1beta1/band_relayers',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BandPriceStates',
    full_name='injective.oracle.v1beta1.Query.BandPriceStates',
    index=2,
    containing_service=None,
    input_type=_QUERYBANDPRICESTATESREQUEST,
    output_type=_QUERYBANDPRICESTATESRESPONSE,
    serialized_options=b'\202\323\344\223\002-\022+/injective/oracle/v1beta1/band_price_states',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BandIBCPriceStates',
    full_name='injective.oracle.v1beta1.Query.BandIBCPriceStates',
    index=3,
    containing_service=None,
    input_type=_QUERYBANDIBCPRICESTATESREQUEST,
    output_type=_QUERYBANDIBCPRICESTATESRESPONSE,
    serialized_options=b'\202\323\344\223\0021\022//injective/oracle/v1beta1/band_ibc_price_states',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PriceFeedPriceStates',
    full_name='injective.oracle.v1beta1.Query.PriceFeedPriceStates',
    index=4,
    containing_service=None,
    input_type=_QUERYPRICEFEEDPRICESTATESREQUEST,
    output_type=_QUERYPRICEFEEDPRICESTATESRESPONSE,
    serialized_options=b'\202\323\344\223\0022\0220/injective/oracle/v1beta1/pricefeed_price_states',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CoinbasePriceStates',
    full_name='injective.oracle.v1beta1.Query.CoinbasePriceStates',
    index=5,
    containing_service=None,
    input_type=_QUERYCOINBASEPRICESTATESREQUEST,
    output_type=_QUERYCOINBASEPRICESTATESRESPONSE,
    serialized_options=b'\202\323\344\223\0021\022//injective/oracle/v1beta1/coinbase_price_states',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='OracleModuleState',
    full_name='injective.oracle.v1beta1.Query.OracleModuleState',
    index=6,
    containing_service=None,
    input_type=_QUERYMODULESTATEREQUEST,
    output_type=_QUERYMODULESTATERESPONSE,
    serialized_options=b'\202\323\344\223\002(\022&/injective/oracle/v1beta1/module_state',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
