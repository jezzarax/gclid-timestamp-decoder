# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gclid.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gclid.proto',
  package='gclid_decoder',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0bgclid.proto\x12\rgclid_decoder\"\xb3\x02\n\x07GClIdv1\x12\x0c\n\x04val1\x18\x02 \x02(\x03\x12+\n\x02n1\x18\x03 \x02(\x0b\x32\x1f.gclid_decoder.GClIdv1.Nesting1\x12\r\n\x04val2\x18\xfe\x7f \x02(\x03\x1a\x34\n\x08Nesting3\x12\x0c\n\x04val1\x18\x01 \x02(\x03\x12\x0c\n\x04val2\x18\x02 \x02(\x0c\x12\x0c\n\x04val3\x18\x03 \x02(\x0c\x1a\x61\n\x08Nesting2\x12+\n\x02n1\x18\x01 \x02(\x0b\x32\x1f.gclid_decoder.GClIdv1.Nesting3\x12\x0c\n\x04val2\x18\x02 \x02(\x03\x12\x0c\n\x04val3\x18\x03 \x02(\x03\x12\x0c\n\x04val4\x18\x04 \x02(\x03\x1a\x45\n\x08Nesting1\x12+\n\x02n1\x18\x01 \x02(\x0b\x32\x1f.gclid_decoder.GClIdv1.Nesting2\x12\x0c\n\x04val1\x18\x02 \x02(\x0c\"\xcc\x01\n\x07GClIdv2\x12+\n\x02n1\x18\x01 \x02(\x0b\x32\x1f.gclid_decoder.GClIdv2.Nesting1\x12\x0c\n\x04val1\x18\x02 \x02(\x03\x12\r\n\x04val2\x18\xfe\x7f \x02(\x03\x1a&\n\x08Nesting2\x12\x0c\n\x04val1\x18\x01 \x02(\x03\x12\x0c\n\x04val2\x18\x02 \x02(\x03\x1aO\n\x08Nesting1\x12+\n\x02n2\x18\x01 \x02(\x0b\x32\x1f.gclid_decoder.GClIdv2.Nesting2\x12\n\n\x02\x62\x31\x18\x02 \x02(\x0c\x12\n\n\x02\x62\x32\x18\x03 \x02(\x0c')
)




_GCLIDV1_NESTING3 = _descriptor.Descriptor(
  name='Nesting3',
  full_name='gclid_decoder.GClIdv1.Nesting3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='val1', full_name='gclid_decoder.GClIdv1.Nesting3.val1', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val2', full_name='gclid_decoder.GClIdv1.Nesting3.val2', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val3', full_name='gclid_decoder.GClIdv1.Nesting3.val3', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=168,
)

_GCLIDV1_NESTING2 = _descriptor.Descriptor(
  name='Nesting2',
  full_name='gclid_decoder.GClIdv1.Nesting2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n1', full_name='gclid_decoder.GClIdv1.Nesting2.n1', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val2', full_name='gclid_decoder.GClIdv1.Nesting2.val2', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val3', full_name='gclid_decoder.GClIdv1.Nesting2.val3', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val4', full_name='gclid_decoder.GClIdv1.Nesting2.val4', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=267,
)

_GCLIDV1_NESTING1 = _descriptor.Descriptor(
  name='Nesting1',
  full_name='gclid_decoder.GClIdv1.Nesting1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n1', full_name='gclid_decoder.GClIdv1.Nesting1.n1', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val1', full_name='gclid_decoder.GClIdv1.Nesting1.val1', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=338,
)

_GCLIDV1 = _descriptor.Descriptor(
  name='GClIdv1',
  full_name='gclid_decoder.GClIdv1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='val1', full_name='gclid_decoder.GClIdv1.val1', index=0,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n1', full_name='gclid_decoder.GClIdv1.n1', index=1,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val2', full_name='gclid_decoder.GClIdv1.val2', index=2,
      number=16382, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GCLIDV1_NESTING3, _GCLIDV1_NESTING2, _GCLIDV1_NESTING1, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=338,
)


_GCLIDV2_NESTING2 = _descriptor.Descriptor(
  name='Nesting2',
  full_name='gclid_decoder.GClIdv2.Nesting2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='val1', full_name='gclid_decoder.GClIdv2.Nesting2.val1', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val2', full_name='gclid_decoder.GClIdv2.Nesting2.val2', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=464,
)

_GCLIDV2_NESTING1 = _descriptor.Descriptor(
  name='Nesting1',
  full_name='gclid_decoder.GClIdv2.Nesting1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n2', full_name='gclid_decoder.GClIdv2.Nesting1.n2', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b1', full_name='gclid_decoder.GClIdv2.Nesting1.b1', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b2', full_name='gclid_decoder.GClIdv2.Nesting1.b2', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=466,
  serialized_end=545,
)

_GCLIDV2 = _descriptor.Descriptor(
  name='GClIdv2',
  full_name='gclid_decoder.GClIdv2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n1', full_name='gclid_decoder.GClIdv2.n1', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val1', full_name='gclid_decoder.GClIdv2.val1', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val2', full_name='gclid_decoder.GClIdv2.val2', index=2,
      number=16382, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GCLIDV2_NESTING2, _GCLIDV2_NESTING1, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=341,
  serialized_end=545,
)

_GCLIDV1_NESTING3.containing_type = _GCLIDV1
_GCLIDV1_NESTING2.fields_by_name['n1'].message_type = _GCLIDV1_NESTING3
_GCLIDV1_NESTING2.containing_type = _GCLIDV1
_GCLIDV1_NESTING1.fields_by_name['n1'].message_type = _GCLIDV1_NESTING2
_GCLIDV1_NESTING1.containing_type = _GCLIDV1
_GCLIDV1.fields_by_name['n1'].message_type = _GCLIDV1_NESTING1
_GCLIDV2_NESTING2.containing_type = _GCLIDV2
_GCLIDV2_NESTING1.fields_by_name['n2'].message_type = _GCLIDV2_NESTING2
_GCLIDV2_NESTING1.containing_type = _GCLIDV2
_GCLIDV2.fields_by_name['n1'].message_type = _GCLIDV2_NESTING1
DESCRIPTOR.message_types_by_name['GClIdv1'] = _GCLIDV1
DESCRIPTOR.message_types_by_name['GClIdv2'] = _GCLIDV2
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GClIdv1 = _reflection.GeneratedProtocolMessageType('GClIdv1', (_message.Message,), dict(

  Nesting3 = _reflection.GeneratedProtocolMessageType('Nesting3', (_message.Message,), dict(
    DESCRIPTOR = _GCLIDV1_NESTING3,
    __module__ = 'gclid_pb2'
    # @@protoc_insertion_point(class_scope:gclid_decoder.GClIdv1.Nesting3)
    ))
  ,

  Nesting2 = _reflection.GeneratedProtocolMessageType('Nesting2', (_message.Message,), dict(
    DESCRIPTOR = _GCLIDV1_NESTING2,
    __module__ = 'gclid_pb2'
    # @@protoc_insertion_point(class_scope:gclid_decoder.GClIdv1.Nesting2)
    ))
  ,

  Nesting1 = _reflection.GeneratedProtocolMessageType('Nesting1', (_message.Message,), dict(
    DESCRIPTOR = _GCLIDV1_NESTING1,
    __module__ = 'gclid_pb2'
    # @@protoc_insertion_point(class_scope:gclid_decoder.GClIdv1.Nesting1)
    ))
  ,
  DESCRIPTOR = _GCLIDV1,
  __module__ = 'gclid_pb2'
  # @@protoc_insertion_point(class_scope:gclid_decoder.GClIdv1)
  ))
_sym_db.RegisterMessage(GClIdv1)
_sym_db.RegisterMessage(GClIdv1.Nesting3)
_sym_db.RegisterMessage(GClIdv1.Nesting2)
_sym_db.RegisterMessage(GClIdv1.Nesting1)

GClIdv2 = _reflection.GeneratedProtocolMessageType('GClIdv2', (_message.Message,), dict(

  Nesting2 = _reflection.GeneratedProtocolMessageType('Nesting2', (_message.Message,), dict(
    DESCRIPTOR = _GCLIDV2_NESTING2,
    __module__ = 'gclid_pb2'
    # @@protoc_insertion_point(class_scope:gclid_decoder.GClIdv2.Nesting2)
    ))
  ,

  Nesting1 = _reflection.GeneratedProtocolMessageType('Nesting1', (_message.Message,), dict(
    DESCRIPTOR = _GCLIDV2_NESTING1,
    __module__ = 'gclid_pb2'
    # @@protoc_insertion_point(class_scope:gclid_decoder.GClIdv2.Nesting1)
    ))
  ,
  DESCRIPTOR = _GCLIDV2,
  __module__ = 'gclid_pb2'
  # @@protoc_insertion_point(class_scope:gclid_decoder.GClIdv2)
  ))
_sym_db.RegisterMessage(GClIdv2)
_sym_db.RegisterMessage(GClIdv2.Nesting2)
_sym_db.RegisterMessage(GClIdv2.Nesting1)


# @@protoc_insertion_point(module_scope)
