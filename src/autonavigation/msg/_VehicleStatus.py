# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autonavigation/VehicleStatus.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class VehicleStatus(genpy.Message):
  _md5sum = "91d7fe875bafc86f4b02d632ea4842cd"
  _type = "autonavigation/VehicleStatus"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#对应结构体Autonavigation_Vehicle_Status

uint32     unique_key           #自主行驶载车唯一标识
uint32     gps_week             #GPS周
uint64     gps_millisecond      #GPS毫秒,以周的零点开始的毫秒数
float64    longitude            #经度，单位为度
float64    latitude             #纬度，单位为度
int64      gaussX               #高斯坐标X
int64      gaussY               #高斯坐标Y
int32      height               #距离海平面高度
int32      azimuth              #航向角，单位0.01度，向东为0，逆时针0～36000
int32      pitch                #俯仰角，欧拉角，单位0.01度
int32      roll                 #翻滚角，欧拉角，单位0.01度
int32      northVelocity        #北向速度，单位cm/s
int32      eastVelocity         #东向速度，单位cm/s
int32      upVelocity           #向上速度，单位cm/s
uint32     travel_distance      #T0时刻开始后，前进的里程，单位米
int32      remain_time          #距离T0时刻还有多少时间，单位毫秒
uint32     time_delay           #网络延时，单位毫秒
int16      steer                #单位0.01度，前轮转角，左转为正
uint8      fuel                 #剩余油量，百分比
uint8      shift                #档位
uint8      voltage              #电压
uint8      throttle             #当前使用油门量，百分比
uint8      brake                #当前使用刹车量，百分比
uint8      engine_speed         #单位100转/分钟，发动机转速
uint8      vehicle_speed        #单位km/h，汽车时速
uint8      water_temperature    #汽车水温
uint8      control_status       #控制状态
uint8      error_status         #错误状态
uint8      barometer1           #单位0.1kpa
uint8      barometer2           #单位0.1kpa
uint8      handbrake            #手刹状态    0：手刹放开 1：手刹拉紧
uint8      engine_status        #发动机点火状态  0：发动机熄火  1：发动机运行  
uint8      sts_mode             #0-默认状态, 1-md5文件校验结果
uint8      controllable1        #Bit8：方向盘 Bit7：油门 Bit6：刹车 Bit5：档位 Bit4：手刹 Bit3：点火 Bit2：熄火 Bit1：预留 相应位为1表示受方舱控制 
uint8      enable               #能否进行自主 0：不能  1：能
uint8      reserve3             #record_status
uint8      reserve4 
uint8      reserve5 
uint8      reserve6 
uint8      reserve7 
uint8[]    md5_str              #md5文件校验值

"""
  __slots__ = ['unique_key','gps_week','gps_millisecond','longitude','latitude','gaussX','gaussY','height','azimuth','pitch','roll','northVelocity','eastVelocity','upVelocity','travel_distance','remain_time','time_delay','steer','fuel','shift','voltage','throttle','brake','engine_speed','vehicle_speed','water_temperature','control_status','error_status','barometer1','barometer2','handbrake','engine_status','sts_mode','controllable1','enable','reserve3','reserve4','reserve5','reserve6','reserve7','md5_str']
  _slot_types = ['uint32','uint32','uint64','float64','float64','int64','int64','int32','int32','int32','int32','int32','int32','int32','uint32','int32','uint32','int16','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       unique_key,gps_week,gps_millisecond,longitude,latitude,gaussX,gaussY,height,azimuth,pitch,roll,northVelocity,eastVelocity,upVelocity,travel_distance,remain_time,time_delay,steer,fuel,shift,voltage,throttle,brake,engine_speed,vehicle_speed,water_temperature,control_status,error_status,barometer1,barometer2,handbrake,engine_status,sts_mode,controllable1,enable,reserve3,reserve4,reserve5,reserve6,reserve7,md5_str

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VehicleStatus, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.unique_key is None:
        self.unique_key = 0
      if self.gps_week is None:
        self.gps_week = 0
      if self.gps_millisecond is None:
        self.gps_millisecond = 0
      if self.longitude is None:
        self.longitude = 0.
      if self.latitude is None:
        self.latitude = 0.
      if self.gaussX is None:
        self.gaussX = 0
      if self.gaussY is None:
        self.gaussY = 0
      if self.height is None:
        self.height = 0
      if self.azimuth is None:
        self.azimuth = 0
      if self.pitch is None:
        self.pitch = 0
      if self.roll is None:
        self.roll = 0
      if self.northVelocity is None:
        self.northVelocity = 0
      if self.eastVelocity is None:
        self.eastVelocity = 0
      if self.upVelocity is None:
        self.upVelocity = 0
      if self.travel_distance is None:
        self.travel_distance = 0
      if self.remain_time is None:
        self.remain_time = 0
      if self.time_delay is None:
        self.time_delay = 0
      if self.steer is None:
        self.steer = 0
      if self.fuel is None:
        self.fuel = 0
      if self.shift is None:
        self.shift = 0
      if self.voltage is None:
        self.voltage = 0
      if self.throttle is None:
        self.throttle = 0
      if self.brake is None:
        self.brake = 0
      if self.engine_speed is None:
        self.engine_speed = 0
      if self.vehicle_speed is None:
        self.vehicle_speed = 0
      if self.water_temperature is None:
        self.water_temperature = 0
      if self.control_status is None:
        self.control_status = 0
      if self.error_status is None:
        self.error_status = 0
      if self.barometer1 is None:
        self.barometer1 = 0
      if self.barometer2 is None:
        self.barometer2 = 0
      if self.handbrake is None:
        self.handbrake = 0
      if self.engine_status is None:
        self.engine_status = 0
      if self.sts_mode is None:
        self.sts_mode = 0
      if self.controllable1 is None:
        self.controllable1 = 0
      if self.enable is None:
        self.enable = 0
      if self.reserve3 is None:
        self.reserve3 = 0
      if self.reserve4 is None:
        self.reserve4 = 0
      if self.reserve5 is None:
        self.reserve5 = 0
      if self.reserve6 is None:
        self.reserve6 = 0
      if self.reserve7 is None:
        self.reserve7 = 0
      if self.md5_str is None:
        self.md5_str = ''
    else:
      self.unique_key = 0
      self.gps_week = 0
      self.gps_millisecond = 0
      self.longitude = 0.
      self.latitude = 0.
      self.gaussX = 0
      self.gaussY = 0
      self.height = 0
      self.azimuth = 0
      self.pitch = 0
      self.roll = 0
      self.northVelocity = 0
      self.eastVelocity = 0
      self.upVelocity = 0
      self.travel_distance = 0
      self.remain_time = 0
      self.time_delay = 0
      self.steer = 0
      self.fuel = 0
      self.shift = 0
      self.voltage = 0
      self.throttle = 0
      self.brake = 0
      self.engine_speed = 0
      self.vehicle_speed = 0
      self.water_temperature = 0
      self.control_status = 0
      self.error_status = 0
      self.barometer1 = 0
      self.barometer2 = 0
      self.handbrake = 0
      self.engine_status = 0
      self.sts_mode = 0
      self.controllable1 = 0
      self.enable = 0
      self.reserve3 = 0
      self.reserve4 = 0
      self.reserve5 = 0
      self.reserve6 = 0
      self.reserve7 = 0
      self.md5_str = ''

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
      buff.write(_struct_2IQ2d2q7iIiIh22B.pack(_x.unique_key, _x.gps_week, _x.gps_millisecond, _x.longitude, _x.latitude, _x.gaussX, _x.gaussY, _x.height, _x.azimuth, _x.pitch, _x.roll, _x.northVelocity, _x.eastVelocity, _x.upVelocity, _x.travel_distance, _x.remain_time, _x.time_delay, _x.steer, _x.fuel, _x.shift, _x.voltage, _x.throttle, _x.brake, _x.engine_speed, _x.vehicle_speed, _x.water_temperature, _x.control_status, _x.error_status, _x.barometer1, _x.barometer2, _x.handbrake, _x.engine_status, _x.sts_mode, _x.controllable1, _x.enable, _x.reserve3, _x.reserve4, _x.reserve5, _x.reserve6, _x.reserve7))
      _x = self.md5_str
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
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
      end += 112
      (_x.unique_key, _x.gps_week, _x.gps_millisecond, _x.longitude, _x.latitude, _x.gaussX, _x.gaussY, _x.height, _x.azimuth, _x.pitch, _x.roll, _x.northVelocity, _x.eastVelocity, _x.upVelocity, _x.travel_distance, _x.remain_time, _x.time_delay, _x.steer, _x.fuel, _x.shift, _x.voltage, _x.throttle, _x.brake, _x.engine_speed, _x.vehicle_speed, _x.water_temperature, _x.control_status, _x.error_status, _x.barometer1, _x.barometer2, _x.handbrake, _x.engine_status, _x.sts_mode, _x.controllable1, _x.enable, _x.reserve3, _x.reserve4, _x.reserve5, _x.reserve6, _x.reserve7,) = _struct_2IQ2d2q7iIiIh22B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.md5_str = str[start:end]
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
      buff.write(_struct_2IQ2d2q7iIiIh22B.pack(_x.unique_key, _x.gps_week, _x.gps_millisecond, _x.longitude, _x.latitude, _x.gaussX, _x.gaussY, _x.height, _x.azimuth, _x.pitch, _x.roll, _x.northVelocity, _x.eastVelocity, _x.upVelocity, _x.travel_distance, _x.remain_time, _x.time_delay, _x.steer, _x.fuel, _x.shift, _x.voltage, _x.throttle, _x.brake, _x.engine_speed, _x.vehicle_speed, _x.water_temperature, _x.control_status, _x.error_status, _x.barometer1, _x.barometer2, _x.handbrake, _x.engine_status, _x.sts_mode, _x.controllable1, _x.enable, _x.reserve3, _x.reserve4, _x.reserve5, _x.reserve6, _x.reserve7))
      _x = self.md5_str
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
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
      end += 112
      (_x.unique_key, _x.gps_week, _x.gps_millisecond, _x.longitude, _x.latitude, _x.gaussX, _x.gaussY, _x.height, _x.azimuth, _x.pitch, _x.roll, _x.northVelocity, _x.eastVelocity, _x.upVelocity, _x.travel_distance, _x.remain_time, _x.time_delay, _x.steer, _x.fuel, _x.shift, _x.voltage, _x.throttle, _x.brake, _x.engine_speed, _x.vehicle_speed, _x.water_temperature, _x.control_status, _x.error_status, _x.barometer1, _x.barometer2, _x.handbrake, _x.engine_status, _x.sts_mode, _x.controllable1, _x.enable, _x.reserve3, _x.reserve4, _x.reserve5, _x.reserve6, _x.reserve7,) = _struct_2IQ2d2q7iIiIh22B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.md5_str = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2IQ2d2q7iIiIh22B = struct.Struct("<2IQ2d2q7iIiIh22B")
