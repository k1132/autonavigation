# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autonavigation/RadarObject.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RadarObject(genpy.Message):
  _md5sum = "990f6008a0f1e90d45f985a0d38242f3"
  _type = "autonavigation/RadarObject"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 Range
float64 RangeRate
float64 Angle
float64 PosX
float64 PosY
float64 Speed
float64 SpeedX
float64 SpeedY
float64 Width
float64 Length
int32   Used
int32   exist

"""
  __slots__ = ['Range','RangeRate','Angle','PosX','PosY','Speed','SpeedX','SpeedY','Width','Length','Used','exist']
  _slot_types = ['float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Range,RangeRate,Angle,PosX,PosY,Speed,SpeedX,SpeedY,Width,Length,Used,exist

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RadarObject, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.Range is None:
        self.Range = 0.
      if self.RangeRate is None:
        self.RangeRate = 0.
      if self.Angle is None:
        self.Angle = 0.
      if self.PosX is None:
        self.PosX = 0.
      if self.PosY is None:
        self.PosY = 0.
      if self.Speed is None:
        self.Speed = 0.
      if self.SpeedX is None:
        self.SpeedX = 0.
      if self.SpeedY is None:
        self.SpeedY = 0.
      if self.Width is None:
        self.Width = 0.
      if self.Length is None:
        self.Length = 0.
      if self.Used is None:
        self.Used = 0
      if self.exist is None:
        self.exist = 0
    else:
      self.Range = 0.
      self.RangeRate = 0.
      self.Angle = 0.
      self.PosX = 0.
      self.PosY = 0.
      self.Speed = 0.
      self.SpeedX = 0.
      self.SpeedY = 0.
      self.Width = 0.
      self.Length = 0.
      self.Used = 0
      self.exist = 0

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
      buff.write(_struct_10d2i.pack(_x.Range, _x.RangeRate, _x.Angle, _x.PosX, _x.PosY, _x.Speed, _x.SpeedX, _x.SpeedY, _x.Width, _x.Length, _x.Used, _x.exist))
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
      end += 88
      (_x.Range, _x.RangeRate, _x.Angle, _x.PosX, _x.PosY, _x.Speed, _x.SpeedX, _x.SpeedY, _x.Width, _x.Length, _x.Used, _x.exist,) = _struct_10d2i.unpack(str[start:end])
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
      buff.write(_struct_10d2i.pack(_x.Range, _x.RangeRate, _x.Angle, _x.PosX, _x.PosY, _x.Speed, _x.SpeedX, _x.SpeedY, _x.Width, _x.Length, _x.Used, _x.exist))
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
      end += 88
      (_x.Range, _x.RangeRate, _x.Angle, _x.PosX, _x.PosY, _x.Speed, _x.SpeedX, _x.SpeedY, _x.Width, _x.Length, _x.Used, _x.exist,) = _struct_10d2i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_10d2i = struct.Struct("<10d2i")