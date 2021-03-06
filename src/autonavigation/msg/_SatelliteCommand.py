# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autonavigation/SatelliteCommand.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SatelliteCommand(genpy.Message):
  _md5sum = "76a796826c5946696132c32a06bd9d85"
  _type = "autonavigation/SatelliteCommand"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#对应结构体Autonavigation_Satellite_Command
#该命令用于卫星数据链


uint32     unique_key          #自主行驶载车唯一标识，用于区分载车的id
uint32     gps_week            #GPS周
uint64     gps_millisecond     #取GPS周的毫秒级时间
uint64     cmd_millisecond     #T0 时间
uint8      cmd_priority        #优先权，0-最高优先级，无条件响应此命令。1-与电台优先级相同，2-低于电台优先级
uint8      cmd_task_mode       #任务模式默认值0，什么都不做，1：遥控模式2：立即进入自主模式3:T0 模式
uint8      cmd_hand_brake      #0：松开手刹, 1：拉紧手刹
uint8      cmd_throttle        #油门量命令，百分比
uint8      cmd_brake           #刹车量命令，百分比
uint8      cmd_shift           #换档命令,0: P, 1: R, 2: N, 3:D, 4: S, 5: L
uint8      cmd_ignition        #0：熄火1：点火
uint8      cmd_light           #灯光
uint8      cmd_reserve1
uint8      cmd_reserve2
uint8      cmd_reserve3
uint8      cmd_reserve4
uint8      cmd_reserve5
uint8      cmd_reserve6
uint8      cmd_reserve7
uint8      cmd_reserve8 



"""
  __slots__ = ['unique_key','gps_week','gps_millisecond','cmd_millisecond','cmd_priority','cmd_task_mode','cmd_hand_brake','cmd_throttle','cmd_brake','cmd_shift','cmd_ignition','cmd_light','cmd_reserve1','cmd_reserve2','cmd_reserve3','cmd_reserve4','cmd_reserve5','cmd_reserve6','cmd_reserve7','cmd_reserve8']
  _slot_types = ['uint32','uint32','uint64','uint64','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       unique_key,gps_week,gps_millisecond,cmd_millisecond,cmd_priority,cmd_task_mode,cmd_hand_brake,cmd_throttle,cmd_brake,cmd_shift,cmd_ignition,cmd_light,cmd_reserve1,cmd_reserve2,cmd_reserve3,cmd_reserve4,cmd_reserve5,cmd_reserve6,cmd_reserve7,cmd_reserve8

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SatelliteCommand, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.unique_key is None:
        self.unique_key = 0
      if self.gps_week is None:
        self.gps_week = 0
      if self.gps_millisecond is None:
        self.gps_millisecond = 0
      if self.cmd_millisecond is None:
        self.cmd_millisecond = 0
      if self.cmd_priority is None:
        self.cmd_priority = 0
      if self.cmd_task_mode is None:
        self.cmd_task_mode = 0
      if self.cmd_hand_brake is None:
        self.cmd_hand_brake = 0
      if self.cmd_throttle is None:
        self.cmd_throttle = 0
      if self.cmd_brake is None:
        self.cmd_brake = 0
      if self.cmd_shift is None:
        self.cmd_shift = 0
      if self.cmd_ignition is None:
        self.cmd_ignition = 0
      if self.cmd_light is None:
        self.cmd_light = 0
      if self.cmd_reserve1 is None:
        self.cmd_reserve1 = 0
      if self.cmd_reserve2 is None:
        self.cmd_reserve2 = 0
      if self.cmd_reserve3 is None:
        self.cmd_reserve3 = 0
      if self.cmd_reserve4 is None:
        self.cmd_reserve4 = 0
      if self.cmd_reserve5 is None:
        self.cmd_reserve5 = 0
      if self.cmd_reserve6 is None:
        self.cmd_reserve6 = 0
      if self.cmd_reserve7 is None:
        self.cmd_reserve7 = 0
      if self.cmd_reserve8 is None:
        self.cmd_reserve8 = 0
    else:
      self.unique_key = 0
      self.gps_week = 0
      self.gps_millisecond = 0
      self.cmd_millisecond = 0
      self.cmd_priority = 0
      self.cmd_task_mode = 0
      self.cmd_hand_brake = 0
      self.cmd_throttle = 0
      self.cmd_brake = 0
      self.cmd_shift = 0
      self.cmd_ignition = 0
      self.cmd_light = 0
      self.cmd_reserve1 = 0
      self.cmd_reserve2 = 0
      self.cmd_reserve3 = 0
      self.cmd_reserve4 = 0
      self.cmd_reserve5 = 0
      self.cmd_reserve6 = 0
      self.cmd_reserve7 = 0
      self.cmd_reserve8 = 0

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
      buff.write(_struct_2I2Q16B.pack(_x.unique_key, _x.gps_week, _x.gps_millisecond, _x.cmd_millisecond, _x.cmd_priority, _x.cmd_task_mode, _x.cmd_hand_brake, _x.cmd_throttle, _x.cmd_brake, _x.cmd_shift, _x.cmd_ignition, _x.cmd_light, _x.cmd_reserve1, _x.cmd_reserve2, _x.cmd_reserve3, _x.cmd_reserve4, _x.cmd_reserve5, _x.cmd_reserve6, _x.cmd_reserve7, _x.cmd_reserve8))
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
      (_x.unique_key, _x.gps_week, _x.gps_millisecond, _x.cmd_millisecond, _x.cmd_priority, _x.cmd_task_mode, _x.cmd_hand_brake, _x.cmd_throttle, _x.cmd_brake, _x.cmd_shift, _x.cmd_ignition, _x.cmd_light, _x.cmd_reserve1, _x.cmd_reserve2, _x.cmd_reserve3, _x.cmd_reserve4, _x.cmd_reserve5, _x.cmd_reserve6, _x.cmd_reserve7, _x.cmd_reserve8,) = _struct_2I2Q16B.unpack(str[start:end])
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
      buff.write(_struct_2I2Q16B.pack(_x.unique_key, _x.gps_week, _x.gps_millisecond, _x.cmd_millisecond, _x.cmd_priority, _x.cmd_task_mode, _x.cmd_hand_brake, _x.cmd_throttle, _x.cmd_brake, _x.cmd_shift, _x.cmd_ignition, _x.cmd_light, _x.cmd_reserve1, _x.cmd_reserve2, _x.cmd_reserve3, _x.cmd_reserve4, _x.cmd_reserve5, _x.cmd_reserve6, _x.cmd_reserve7, _x.cmd_reserve8))
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
      (_x.unique_key, _x.gps_week, _x.gps_millisecond, _x.cmd_millisecond, _x.cmd_priority, _x.cmd_task_mode, _x.cmd_hand_brake, _x.cmd_throttle, _x.cmd_brake, _x.cmd_shift, _x.cmd_ignition, _x.cmd_light, _x.cmd_reserve1, _x.cmd_reserve2, _x.cmd_reserve3, _x.cmd_reserve4, _x.cmd_reserve5, _x.cmd_reserve6, _x.cmd_reserve7, _x.cmd_reserve8,) = _struct_2I2Q16B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2I2Q16B = struct.Struct("<2I2Q16B")
