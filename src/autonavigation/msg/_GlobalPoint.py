# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autonavigation/GlobalPoint.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GlobalPoint(genpy.Message):
  _md5sum = "52ea414ee4525ca16ed4c3da37e048ae"
  _type = "autonavigation/GlobalPoint"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """    float64  x
    float64  y
    int32     envType        #环境描述（停止线，斑马线，行人，交通灯类型）
    int32     actType        #车辆行为描述（停车及持续时间，超车，换道）
    int32     curveRadius    #曲率
    int32     maxSpeed       #限速
    int32     slope          #坡度
    int32     pointId        #全局id号

"""
  __slots__ = ['x','y','envType','actType','curveRadius','maxSpeed','slope','pointId']
  _slot_types = ['float64','float64','int32','int32','int32','int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x,y,envType,actType,curveRadius,maxSpeed,slope,pointId

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GlobalPoint, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.envType is None:
        self.envType = 0
      if self.actType is None:
        self.actType = 0
      if self.curveRadius is None:
        self.curveRadius = 0
      if self.maxSpeed is None:
        self.maxSpeed = 0
      if self.slope is None:
        self.slope = 0
      if self.pointId is None:
        self.pointId = 0
    else:
      self.x = 0.
      self.y = 0.
      self.envType = 0
      self.actType = 0
      self.curveRadius = 0
      self.maxSpeed = 0
      self.slope = 0
      self.pointId = 0

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
      buff.write(_struct_2d6i.pack(_x.x, _x.y, _x.envType, _x.actType, _x.curveRadius, _x.maxSpeed, _x.slope, _x.pointId))
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
      end += 40
      (_x.x, _x.y, _x.envType, _x.actType, _x.curveRadius, _x.maxSpeed, _x.slope, _x.pointId,) = _struct_2d6i.unpack(str[start:end])
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
      buff.write(_struct_2d6i.pack(_x.x, _x.y, _x.envType, _x.actType, _x.curveRadius, _x.maxSpeed, _x.slope, _x.pointId))
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
      end += 40
      (_x.x, _x.y, _x.envType, _x.actType, _x.curveRadius, _x.maxSpeed, _x.slope, _x.pointId,) = _struct_2d6i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2d6i = struct.Struct("<2d6i")
