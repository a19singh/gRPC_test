# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: details.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='details.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rdetails.proto\"$\n\x07\x44\x65tails\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x03\"%\n\x08\x41\x64\x65tails\x12\x19\n\x07\x64\x65tails\x18\x01 \x03(\x0b\x32\x08.Details22\n\x0c\x41rrayDetails\x12\"\n\x08Personal\x12\x08.Details\x1a\x08.Details\"\x00\x30\x01\x62\x06proto3'
)




_DETAILS = _descriptor.Descriptor(
  name='Details',
  full_name='Details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='Details.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='Details.age', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=17,
  serialized_end=53,
)


_ADETAILS = _descriptor.Descriptor(
  name='Adetails',
  full_name='Adetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='Adetails.details', index=0,
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
  serialized_start=55,
  serialized_end=92,
)

_ADETAILS.fields_by_name['details'].message_type = _DETAILS
DESCRIPTOR.message_types_by_name['Details'] = _DETAILS
DESCRIPTOR.message_types_by_name['Adetails'] = _ADETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Details = _reflection.GeneratedProtocolMessageType('Details', (_message.Message,), {
  'DESCRIPTOR' : _DETAILS,
  '__module__' : 'details_pb2'
  # @@protoc_insertion_point(class_scope:Details)
  })
_sym_db.RegisterMessage(Details)

Adetails = _reflection.GeneratedProtocolMessageType('Adetails', (_message.Message,), {
  'DESCRIPTOR' : _ADETAILS,
  '__module__' : 'details_pb2'
  # @@protoc_insertion_point(class_scope:Adetails)
  })
_sym_db.RegisterMessage(Adetails)



_ARRAYDETAILS = _descriptor.ServiceDescriptor(
  name='ArrayDetails',
  full_name='ArrayDetails',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=94,
  serialized_end=144,
  methods=[
  _descriptor.MethodDescriptor(
    name='Personal',
    full_name='ArrayDetails.Personal',
    index=0,
    containing_service=None,
    input_type=_DETAILS,
    output_type=_DETAILS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ARRAYDETAILS)

DESCRIPTOR.services_by_name['ArrayDetails'] = _ARRAYDETAILS

# @@protoc_insertion_point(module_scope)