# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tinkoff/invest/grpc/stoporders.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$tinkoff/invest/grpc/stoporders.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a tinkoff/invest/grpc/common.proto\"\xf8\x03\n\x14PostStopOrderRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x03\x12?\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x44\n\nstop_price\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12L\n\tdirection\x18\x05 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.StopOrderDirection\x12\x12\n\naccount_id\x18\x06 \x01(\t\x12W\n\x0f\x65xpiration_type\x18\x07 \x01(\x0e\x32>.tinkoff.public.invest.api.contract.v1.StopOrderExpirationType\x12M\n\x0fstop_order_type\x18\x08 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.StopOrderType\x12/\n\x0b\x65xpire_date\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\".\n\x15PostStopOrderResponse\x12\x15\n\rstop_order_id\x18\x01 \x01(\t\"*\n\x14GetStopOrdersRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\"^\n\x15GetStopOrdersResponse\x12\x45\n\x0bstop_orders\x18\x01 \x03(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.StopOrder\"C\n\x16\x43\x61ncelStopOrderRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x15\n\rstop_order_id\x18\x02 \x01(\t\"C\n\x17\x43\x61ncelStopOrderResponse\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x9b\x04\n\tStopOrder\x12\x15\n\rstop_order_id\x18\x01 \x01(\t\x12\x16\n\x0elots_requested\x18\x02 \x01(\x03\x12\x0c\n\x04\x66igi\x18\x03 \x01(\t\x12L\n\tdirection\x18\x04 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.StopOrderDirection\x12\x10\n\x08\x63urrency\x18\x05 \x01(\t\x12H\n\norder_type\x18\x06 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.StopOrderType\x12/\n\x0b\x63reate_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14\x61\x63tivation_date_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0f\x65xpiration_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12@\n\x05price\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x45\n\nstop_price\x18\x0b \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue*w\n\x12StopOrderDirection\x12$\n STOP_ORDER_DIRECTION_UNSPECIFIED\x10\x00\x12\x1c\n\x18STOP_ORDER_DIRECTION_BUY\x10\x01\x12\x1d\n\x19STOP_ORDER_DIRECTION_SELL\x10\x02*\xa5\x01\n\x17StopOrderExpirationType\x12*\n&STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED\x10\x00\x12/\n+STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL\x10\x01\x12-\n)STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE\x10\x02*\x90\x01\n\rStopOrderType\x12\x1f\n\x1bSTOP_ORDER_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bSTOP_ORDER_TYPE_TAKE_PROFIT\x10\x01\x12\x1d\n\x19STOP_ORDER_TYPE_STOP_LOSS\x10\x02\x12\x1e\n\x1aSTOP_ORDER_TYPE_STOP_LIMIT\x10\x03\x32\xc0\x03\n\x11StopOrdersService\x12\x8a\x01\n\rPostStopOrder\x12;.tinkoff.public.invest.api.contract.v1.PostStopOrderRequest\x1a<.tinkoff.public.invest.api.contract.v1.PostStopOrderResponse\x12\x8a\x01\n\rGetStopOrders\x12;.tinkoff.public.invest.api.contract.v1.GetStopOrdersRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetStopOrdersResponse\x12\x90\x01\n\x0f\x43\x61ncelStopOrder\x12=.tinkoff.public.invest.api.contract.v1.CancelStopOrderRequest\x1a>.tinkoff.public.invest.api.contract.v1.CancelStopOrderResponseBa\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_STOPORDERDIRECTION = DESCRIPTOR.enum_types_by_name['StopOrderDirection']
StopOrderDirection = enum_type_wrapper.EnumTypeWrapper(_STOPORDERDIRECTION)
_STOPORDEREXPIRATIONTYPE = DESCRIPTOR.enum_types_by_name['StopOrderExpirationType']
StopOrderExpirationType = enum_type_wrapper.EnumTypeWrapper(_STOPORDEREXPIRATIONTYPE)
_STOPORDERTYPE = DESCRIPTOR.enum_types_by_name['StopOrderType']
StopOrderType = enum_type_wrapper.EnumTypeWrapper(_STOPORDERTYPE)
STOP_ORDER_DIRECTION_UNSPECIFIED = 0
STOP_ORDER_DIRECTION_BUY = 1
STOP_ORDER_DIRECTION_SELL = 2
STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED = 0
STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL = 1
STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE = 2
STOP_ORDER_TYPE_UNSPECIFIED = 0
STOP_ORDER_TYPE_TAKE_PROFIT = 1
STOP_ORDER_TYPE_STOP_LOSS = 2
STOP_ORDER_TYPE_STOP_LIMIT = 3


_POSTSTOPORDERREQUEST = DESCRIPTOR.message_types_by_name['PostStopOrderRequest']
_POSTSTOPORDERRESPONSE = DESCRIPTOR.message_types_by_name['PostStopOrderResponse']
_GETSTOPORDERSREQUEST = DESCRIPTOR.message_types_by_name['GetStopOrdersRequest']
_GETSTOPORDERSRESPONSE = DESCRIPTOR.message_types_by_name['GetStopOrdersResponse']
_CANCELSTOPORDERREQUEST = DESCRIPTOR.message_types_by_name['CancelStopOrderRequest']
_CANCELSTOPORDERRESPONSE = DESCRIPTOR.message_types_by_name['CancelStopOrderResponse']
_STOPORDER = DESCRIPTOR.message_types_by_name['StopOrder']
PostStopOrderRequest = _reflection.GeneratedProtocolMessageType('PostStopOrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _POSTSTOPORDERREQUEST,
  '__module__' : 'tinkoff.invest.grpc.stoporders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.PostStopOrderRequest)
  })
_sym_db.RegisterMessage(PostStopOrderRequest)

PostStopOrderResponse = _reflection.GeneratedProtocolMessageType('PostStopOrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _POSTSTOPORDERRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.stoporders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.PostStopOrderResponse)
  })
_sym_db.RegisterMessage(PostStopOrderResponse)

GetStopOrdersRequest = _reflection.GeneratedProtocolMessageType('GetStopOrdersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTOPORDERSREQUEST,
  '__module__' : 'tinkoff.invest.grpc.stoporders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetStopOrdersRequest)
  })
_sym_db.RegisterMessage(GetStopOrdersRequest)

GetStopOrdersResponse = _reflection.GeneratedProtocolMessageType('GetStopOrdersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTOPORDERSRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.stoporders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetStopOrdersResponse)
  })
_sym_db.RegisterMessage(GetStopOrdersResponse)

CancelStopOrderRequest = _reflection.GeneratedProtocolMessageType('CancelStopOrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELSTOPORDERREQUEST,
  '__module__' : 'tinkoff.invest.grpc.stoporders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.CancelStopOrderRequest)
  })
_sym_db.RegisterMessage(CancelStopOrderRequest)

CancelStopOrderResponse = _reflection.GeneratedProtocolMessageType('CancelStopOrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELSTOPORDERRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.stoporders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.CancelStopOrderResponse)
  })
_sym_db.RegisterMessage(CancelStopOrderResponse)

StopOrder = _reflection.GeneratedProtocolMessageType('StopOrder', (_message.Message,), {
  'DESCRIPTOR' : _STOPORDER,
  '__module__' : 'tinkoff.invest.grpc.stoporders_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.StopOrder)
  })
_sym_db.RegisterMessage(StopOrder)

_STOPORDERSSERVICE = DESCRIPTOR.services_by_name['StopOrdersService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _STOPORDERDIRECTION._serialized_start=1521
  _STOPORDERDIRECTION._serialized_end=1640
  _STOPORDEREXPIRATIONTYPE._serialized_start=1643
  _STOPORDEREXPIRATIONTYPE._serialized_end=1808
  _STOPORDERTYPE._serialized_start=1811
  _STOPORDERTYPE._serialized_end=1955
  _POSTSTOPORDERREQUEST._serialized_start=147
  _POSTSTOPORDERREQUEST._serialized_end=651
  _POSTSTOPORDERRESPONSE._serialized_start=653
  _POSTSTOPORDERRESPONSE._serialized_end=699
  _GETSTOPORDERSREQUEST._serialized_start=701
  _GETSTOPORDERSREQUEST._serialized_end=743
  _GETSTOPORDERSRESPONSE._serialized_start=745
  _GETSTOPORDERSRESPONSE._serialized_end=839
  _CANCELSTOPORDERREQUEST._serialized_start=841
  _CANCELSTOPORDERREQUEST._serialized_end=908
  _CANCELSTOPORDERRESPONSE._serialized_start=910
  _CANCELSTOPORDERRESPONSE._serialized_end=977
  _STOPORDER._serialized_start=980
  _STOPORDER._serialized_end=1519
  _STOPORDERSSERVICE._serialized_start=1958
  _STOPORDERSSERVICE._serialized_end=2406
# @@protoc_insertion_point(module_scope)
