# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clock.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x63lock.proto\"\r\n\x0bTimeRequest\"!\n\x0cTimeResponse\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\"1\n\x0bSyncRequest\x12\"\n\x0bslave_times\x18\x01 \x03(\x0b\x32\r.TimeResponse\"\"\n\x0cSyncResponse\x12\x12\n\nadjustment\x18\x01 \x01(\x03\x32h\n\x11\x43lockSynchronizer\x12(\n\x07GetTime\x12\x0c.TimeRequest\x1a\r.TimeResponse\"\x00\x12)\n\x08SyncTime\x12\x0c.SyncRequest\x1a\r.SyncResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'clock_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TIMEREQUEST']._serialized_start=15
  _globals['_TIMEREQUEST']._serialized_end=28
  _globals['_TIMERESPONSE']._serialized_start=30
  _globals['_TIMERESPONSE']._serialized_end=63
  _globals['_SYNCREQUEST']._serialized_start=65
  _globals['_SYNCREQUEST']._serialized_end=114
  _globals['_SYNCRESPONSE']._serialized_start=116
  _globals['_SYNCRESPONSE']._serialized_end=150
  _globals['_CLOCKSYNCHRONIZER']._serialized_start=152
  _globals['_CLOCKSYNCHRONIZER']._serialized_end=256
# @@protoc_insertion_point(module_scope)
