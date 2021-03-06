# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autonavigation/LadarPoint.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class LadarPoint(genpy.Message):
  _md5sum = "e47b7acf3aa42d31497a6d45f62b364a"
  _type = "autonavigation/LadarPoint"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint16   x         #cm
uint16   y
int16    z
uint16   angleH         #0.01度
uint16   angleV         #0.01度
uint16   realdistance   #cm
uint8    intensity
uint8    ring


"""
  __slots__ = ['x','y','z','angleH','angleV','realdistance','intensity','ring']
  _slot_types = ['uint16','uint16','int16','uint16','uint16','uint16','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x,y,z,angleH,angleV,realdistance,intensity,ring

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LadarPoint, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.x is None:
        self.x = 0
      if self.y is None:
        self.y = 0
      if self.z is None:
        self.z = 0
      if self.angleH is None:
        self.angleH = 0
      if self.angleV is None:
        self.angleV = 0
      if self.realdistance is None:
        self.realdistance = 0
      if self.intensity is None:
        self.intensity = 0
      if self.ring is None:
        self.ring = 0
    else:
      self.x = 0
      self.y = 0
      self.z = 0
      self.angleH = 0
      self.angleV = 0
      self.realdistance = 0
      self.intensity = 0
      self.ring = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_2Hh3H2B.pack(_x.x, _x.y, _x.z, _x.angleH, _x.angleV, _x.realdistance, _x.intensity, _x.ring))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 14
      (_x.x, _x.y, _x.z, _x.angleH, _x.angleV, _x.realdistance, _x.intensity, _x.ring,) = _struct_2Hh3H2B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_2Hh3H2B.pack(_x.x, _x.y, _x.z, _x.angleH, _x.angleV, _x.realdistance, _x.intensity, _x.ring))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 14
      (_x.x, _x.y, _x.z, _x.angleH, _x.angleV, _x.realdistance, _x.intensity, _x.ring,) = _struct_2Hh3H2B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2Hh3H2B = struct.Struct("<2Hh3H2B")
