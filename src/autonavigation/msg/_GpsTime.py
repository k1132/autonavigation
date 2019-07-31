# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autonavigation/GpsTime.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GpsTime(genpy.Message):
  _md5sum = "83d68f97b802f68fa3f9de2d9684e369"
  _type = "autonavigation/GpsTime"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#对应结构体

uint32     unique_key          #自主行驶载车唯一标识，用于区分载车的id
uint32     gps_week            #GPS周
uint64     gps_millisecond     #取GPS周的毫秒级时间    
float64	   longitude	       #经度，单位为度       
float64	   laltitude           #纬度，单位为度 
uint8      gps_reserve1        #预留
uint8      gps_reserve2
uint8      gps_reserve3
uint8      gps_reserve4
uint8      gps_reserve5
uint8      gps_reserve6
"""
  __slots__ = ['unique_key','gps_week','gps_millisecond','longitude','laltitude','gps_reserve1','gps_reserve2','gps_reserve3','gps_reserve4','gps_reserve5','gps_reserve6']
  _slot_types = ['uint32','uint32','uint64','float64','float64','uint8','uint8','uint8','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       unique_key,gps_week,gps_millisecond,longitude,laltitude,gps_reserve1,gps_reserve2,gps_reserve3,gps_reserve4,gps_reserve5,gps_reserve6

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GpsTime, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.unique_key is None:
        self.unique_key = 0
      if self.gps_week is None:
        self.gps_week = 0
      if self.gps_millisecond is None:
        self.gps_millisecond = 0
      if self.longitude is None:
        self.longitude = 0.
      if self.laltitude is None:
        self.laltitude = 0.
      if self.gps_reserve1 is None:
        self.gps_reserve1 = 0
      if self.gps_reserve2 is None:
        self.gps_reserve2 = 0
      if self.gps_reserve3 is None:
        self.gps_reserve3 = 0
      if self.gps_reserve4 is None:
        self.gps_reserve4 = 0
      if self.gps_reserve5 is None:
        self.gps_reserve5 = 0
      if self.gps_reserve6 is None:
        self.gps_reserve6 = 0
    else:
      self.unique_key = 0
      self.gps_week = 0
      self.gps_millisecond = 0
      self.longitude = 0.
      self.laltitude = 0.
      self.gps_reserve1 = 0
      self.gps_reserve2 = 0
      self.gps_reserve3 = 0
      self.gps_reserve4 = 0
      self.gps_reserve5 = 0
      self.gps_reserve6 = 0

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
      buff.write(_struct_2IQ2d6B.pack(_x.unique_key, _x.gps_week, _x.gps_millisecond, _x.longitude, _x.laltitude, _x.gps_reserve1, _x.gps_reserve2, _x.gps_reserve3, _x.gps_reserve4, _x.gps_reserve5, _x.gps_reserve6))
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
      end += 38
      (_x.unique_key, _x.gps_week, _x.gps_millisecond, _x.longitude, _x.laltitude, _x.gps_reserve1, _x.gps_reserve2, _x.gps_reserve3, _x.gps_reserve4, _x.gps_reserve5, _x.gps_reserve6,) = _struct_2IQ2d6B.unpack(str[start:end])
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
      buff.write(_struct_2IQ2d6B.pack(_x.unique_key, _x.gps_week, _x.gps_millisecond, _x.longitude, _x.laltitude, _x.gps_reserve1, _x.gps_reserve2, _x.gps_reserve3, _x.gps_reserve4, _x.gps_reserve5, _x.gps_reserve6))
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
      end += 38
      (_x.unique_key, _x.gps_week, _x.gps_millisecond, _x.longitude, _x.laltitude, _x.gps_reserve1, _x.gps_reserve2, _x.gps_reserve3, _x.gps_reserve4, _x.gps_reserve5, _x.gps_reserve6,) = _struct_2IQ2d6B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2IQ2d6B = struct.Struct("<2IQ2d6B")