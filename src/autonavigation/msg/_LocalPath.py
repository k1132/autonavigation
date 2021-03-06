# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autonavigation/LocalPath.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import autonavigation.msg
import geometry_msgs.msg
import std_msgs.msg

class LocalPath(genpy.Message):
  _md5sum = "f5ad35f8909fe526985007d91d5de2b5"
  _type = "autonavigation/LocalPath"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """######下面为一系列宏定义#########

# command to vehicle
#ES:紧急停车；ST：停车；AD_SPEED:前进速度跟踪；AD_DISTANCE:前进定距跟踪；AD_POINT:前进定点停车；
#BK_SPEED:后退速度跟踪；BK_DISTANCE:后退定距跟踪；IG：点火；FO：熄火。

uint16 COMMAND_ES=200
uint16 COMMAND_ST=201
uint16 COMMAND_AD_SPEED=202
uint16 COMMAND_AD_DISTANCE=203
uint16 COMMAND_AD_POINT=204
uint16 COMMAND_BK_SPEED=205
uint16 COMMAND_BK_POINT=206
uint16 COMMAND_IG=207
uint16 COMMAND_FO=208

#系统状态
#RS-直道; RO-避障；RT-弯道；RB-分叉；
#HS-高速直道；HF-高速尾随；HT-高速弯道；HB-高速分叉；
#CN-越野；CO-越野避障
#MC-遥控；MR-遥控侦察
#IT-初始化；EM-异常; FI-终点停车 RD-准就绪 SP-停车
#SG-笔直直行
uint16 SYS_STATE_RS=100
uint16 SYS_STATE_RO=101
uint16 SYS_STATE_RT=102
uint16 SYS_STATE_RB=103
uint16 SYS_STATE_CN=104
uint16 SYS_STATE_CO=105
uint16 SYS_STATE_SG=106
uint16 SYS_STATE_HS=107
uint16 SYS_STATE_HF=108
uint16 SYS_STATE_HT=109
uint16 SYS_STATE_HB=110
uint16 SYS_STATE_RD=111
uint16 SYS_STATE_IT=112
uint16 SYS_STATE_MC=113
uint16 SYS_STATE_MR=114
uint16 SYS_STATE_EM=115
uint16 SYS_STATE_SP=116
uint16 SYS_STATE_FI=117

# plan state #
#PR-得到规划路径    NP-没有道路可通行     EC-紧急情况
#GT-到达目标点       PB－上一次的道路      RR-使用参考路
# WT-waiting       REPLAN 重规划       NORMAL_PLAN
uint16 PLAN_STATE_PR=50
uint16 PLAN_STATE_NP=51
uint16 PLAN_STATE_GT=52
uint16 PLAN_STATE_PB=53
uint16 PLAN_STATE_RR=54
uint16 PLAN_STATE_WT=55
uint16 PLAN_STATE_EC=56
uint16 PLAN_STATE_REPLAN=57
uint16 PLAN_STATE_NORMAL_PLAN=58

####宏定义结束############

##########################
####规划输出消息主体#######
##########################

Header      head
LocalPose   localPose
GpsPosition gpsPos

uint32		        plan_data_id 		                #局部路径规划帧号
LocalCoordinate         plan_frame				#冻结坐标 
uint16                  planOutputMode                          #规划输出模式，0-输出路径，1-输出期望速度和曲率                          
uint16		        is_ok					#路径数据有效标志：0 - 无效 1 - 有效
uint16		        effective_point_num	                #局部路径规划的有效点数目
WayPoint[]	        path	       	                        #局部路径规划点集,ros的Point32类型，单位厘米
PathProperty[]	        path_property
uint16                  vehicle_command		                #系统事件,规划给控制的命令，如点火，
uint16           	sys_state
uint16  	        plan_state				#系统状态  
int32		        speed                                   #速度: 公里/小时
VehicleObj              vehicle2Flo
WayPoint                point2Stop
float64                 expVelocity                             #期望速度，值域0.0~100.0，单位是m/s，double类型
float64                 expCurvature                            #期望曲率，单位是1/m,满足右手规则



================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: autonavigation/LocalPose
#LocalPose msg

float64 time			  
#centimeter  
int32 dr_x
int32 dr_y
int32 dr_z
#0.01degree
int32 dr_heading
int32 dr_roll
int32 dr_pitch		    

#left_front wheel speed,cm/s
int32 lf_speed
#right_front wheel speed,cm/s		    
int32 rf_speed
#left_rear wheel speed,cm/s		    
int32 lr_speed
#right_rear wheel speed,cm/s		    
int32 rr_speed		    

#imu三轴陀螺速度 0.01degree/s
int32 rot_x
int32 rot_y                      
int32 rot_z                      
#imu三轴加速度  0.01m/s^2
int32 acc_x                      
int32 acc_y                      
int32 acc_z                      

int32 batteryState
int32 batteryEnergy           #0-100

#-3000(right)~3000(left) degree  0.01degree/s
int32 steer   
#0(zero)~100(full)                  
int32 brake                 
#0(zero)~100(full)     
int32 fuel      
#PARK=0,BACKWARD=1,NEURAL=2,FORWARD=3                 
int8  trans                      
int8  VehicleState
#DIRECT_ACTUATOR=0,REMOTE_PILOT=1,AUTO_PILOT=2
int8  mode                       
#dr运行状态
int8 drStatus
#错误状态		    
int8 errorStatus		    
int8 emergency_flag
int8 hardswitch_on


================================================================================
MSG: autonavigation/GpsPosition
#gps info is updated
char          gps_flag               
uint32        gps_week
#millisecond in a week
float64       gps_millisecond   
#经纬度，单位为度     
float64	      longitude		      
float64	      laltitude
#高斯投影位置,cm
float64	      gaussX		      
float64       gaussY
#height,     cm
float64         height  
#欧拉角，单位为0.01度                
int32         pitch                   
int32         roll
#欧拉角，单位为0.01度,向东为零度，逆时针0-360                    
int32         azimuth                 

#north速度，单位为cm/s
int32         northVelocity           
int32         eastVelocity
int32         upVelocity
#系统运行状态
int32         positionStatus	      

#imu三轴陀螺速度 0.01degree/s
int32	        rot_x                      
int32           rot_y                      
int32           rot_z                      

#imu三轴加速度  0.01m/s^2
int32           acc_x                      
int32           acc_y                      
int32           acc_z                      
	

================================================================================
MSG: autonavigation/LocalCoordinate
int32 z_x
int32 z_y
int32 g_x
int32 g_y
int32 heading
int32 pitch
int32 roll
int32 height
uint8 class_id


================================================================================
MSG: autonavigation/WayPoint
int32 x
int32 y
int32 z

================================================================================
MSG: autonavigation/PathProperty
WayPoint left_boundary
WayPoint right_boundary
int32    direction


================================================================================
MSG: autonavigation/VehicleObj
#ID num
int32 ID       
# position, cm
int32 centerX
int32 centerY
# cm/s
int32 speed        
# 0.01degree   
int32 speedDirection  
int32 height         
# car, truck, bicycle, big obj, small obj, unknown obj 
int32 vehclass     

geometry_msgs/Polygon vehPolygon      

int32   vertexNumber
int32[] vertexX
int32[] vertexY

================================================================================
MSG: geometry_msgs/Polygon
#A specification of a polygon where the first and last points are assumed to be connected
Point32[] points

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z"""
  # Pseudo-constants
  COMMAND_ES = 200
  COMMAND_ST = 201
  COMMAND_AD_SPEED = 202
  COMMAND_AD_DISTANCE = 203
  COMMAND_AD_POINT = 204
  COMMAND_BK_SPEED = 205
  COMMAND_BK_POINT = 206
  COMMAND_IG = 207
  COMMAND_FO = 208
  SYS_STATE_RS = 100
  SYS_STATE_RO = 101
  SYS_STATE_RT = 102
  SYS_STATE_RB = 103
  SYS_STATE_CN = 104
  SYS_STATE_CO = 105
  SYS_STATE_SG = 106
  SYS_STATE_HS = 107
  SYS_STATE_HF = 108
  SYS_STATE_HT = 109
  SYS_STATE_HB = 110
  SYS_STATE_RD = 111
  SYS_STATE_IT = 112
  SYS_STATE_MC = 113
  SYS_STATE_MR = 114
  SYS_STATE_EM = 115
  SYS_STATE_SP = 116
  SYS_STATE_FI = 117
  PLAN_STATE_PR = 50
  PLAN_STATE_NP = 51
  PLAN_STATE_GT = 52
  PLAN_STATE_PB = 53
  PLAN_STATE_RR = 54
  PLAN_STATE_WT = 55
  PLAN_STATE_EC = 56
  PLAN_STATE_REPLAN = 57
  PLAN_STATE_NORMAL_PLAN = 58

  __slots__ = ['head','localPose','gpsPos','plan_data_id','plan_frame','planOutputMode','is_ok','effective_point_num','path','path_property','vehicle_command','sys_state','plan_state','speed','vehicle2Flo','point2Stop','expVelocity','expCurvature']
  _slot_types = ['std_msgs/Header','autonavigation/LocalPose','autonavigation/GpsPosition','uint32','autonavigation/LocalCoordinate','uint16','uint16','uint16','autonavigation/WayPoint[]','autonavigation/PathProperty[]','uint16','uint16','uint16','int32','autonavigation/VehicleObj','autonavigation/WayPoint','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       head,localPose,gpsPos,plan_data_id,plan_frame,planOutputMode,is_ok,effective_point_num,path,path_property,vehicle_command,sys_state,plan_state,speed,vehicle2Flo,point2Stop,expVelocity,expCurvature

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LocalPath, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.head is None:
        self.head = std_msgs.msg.Header()
      if self.localPose is None:
        self.localPose = autonavigation.msg.LocalPose()
      if self.gpsPos is None:
        self.gpsPos = autonavigation.msg.GpsPosition()
      if self.plan_data_id is None:
        self.plan_data_id = 0
      if self.plan_frame is None:
        self.plan_frame = autonavigation.msg.LocalCoordinate()
      if self.planOutputMode is None:
        self.planOutputMode = 0
      if self.is_ok is None:
        self.is_ok = 0
      if self.effective_point_num is None:
        self.effective_point_num = 0
      if self.path is None:
        self.path = []
      if self.path_property is None:
        self.path_property = []
      if self.vehicle_command is None:
        self.vehicle_command = 0
      if self.sys_state is None:
        self.sys_state = 0
      if self.plan_state is None:
        self.plan_state = 0
      if self.speed is None:
        self.speed = 0
      if self.vehicle2Flo is None:
        self.vehicle2Flo = autonavigation.msg.VehicleObj()
      if self.point2Stop is None:
        self.point2Stop = autonavigation.msg.WayPoint()
      if self.expVelocity is None:
        self.expVelocity = 0.
      if self.expCurvature is None:
        self.expCurvature = 0.
    else:
      self.head = std_msgs.msg.Header()
      self.localPose = autonavigation.msg.LocalPose()
      self.gpsPos = autonavigation.msg.GpsPosition()
      self.plan_data_id = 0
      self.plan_frame = autonavigation.msg.LocalCoordinate()
      self.planOutputMode = 0
      self.is_ok = 0
      self.effective_point_num = 0
      self.path = []
      self.path_property = []
      self.vehicle_command = 0
      self.sys_state = 0
      self.plan_state = 0
      self.speed = 0
      self.vehicle2Flo = autonavigation.msg.VehicleObj()
      self.point2Stop = autonavigation.msg.WayPoint()
      self.expVelocity = 0.
      self.expCurvature = 0.

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
      buff.write(_struct_3I.pack(_x.head.seq, _x.head.stamp.secs, _x.head.stamp.nsecs))
      _x = self.head.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_d21i7bBI6d13iI8iB3H.pack(_x.localPose.time, _x.localPose.dr_x, _x.localPose.dr_y, _x.localPose.dr_z, _x.localPose.dr_heading, _x.localPose.dr_roll, _x.localPose.dr_pitch, _x.localPose.lf_speed, _x.localPose.rf_speed, _x.localPose.lr_speed, _x.localPose.rr_speed, _x.localPose.rot_x, _x.localPose.rot_y, _x.localPose.rot_z, _x.localPose.acc_x, _x.localPose.acc_y, _x.localPose.acc_z, _x.localPose.batteryState, _x.localPose.batteryEnergy, _x.localPose.steer, _x.localPose.brake, _x.localPose.fuel, _x.localPose.trans, _x.localPose.VehicleState, _x.localPose.mode, _x.localPose.drStatus, _x.localPose.errorStatus, _x.localPose.emergency_flag, _x.localPose.hardswitch_on, _x.gpsPos.gps_flag, _x.gpsPos.gps_week, _x.gpsPos.gps_millisecond, _x.gpsPos.longitude, _x.gpsPos.laltitude, _x.gpsPos.gaussX, _x.gpsPos.gaussY, _x.gpsPos.height, _x.gpsPos.pitch, _x.gpsPos.roll, _x.gpsPos.azimuth, _x.gpsPos.northVelocity, _x.gpsPos.eastVelocity, _x.gpsPos.upVelocity, _x.gpsPos.positionStatus, _x.gpsPos.rot_x, _x.gpsPos.rot_y, _x.gpsPos.rot_z, _x.gpsPos.acc_x, _x.gpsPos.acc_y, _x.gpsPos.acc_z, _x.plan_data_id, _x.plan_frame.z_x, _x.plan_frame.z_y, _x.plan_frame.g_x, _x.plan_frame.g_y, _x.plan_frame.heading, _x.plan_frame.pitch, _x.plan_frame.roll, _x.plan_frame.height, _x.plan_frame.class_id, _x.planOutputMode, _x.is_ok, _x.effective_point_num))
      length = len(self.path)
      buff.write(_struct_I.pack(length))
      for val1 in self.path:
        _x = val1
        buff.write(_struct_3i.pack(_x.x, _x.y, _x.z))
      length = len(self.path_property)
      buff.write(_struct_I.pack(length))
      for val1 in self.path_property:
        _v1 = val1.left_boundary
        _x = _v1
        buff.write(_struct_3i.pack(_x.x, _x.y, _x.z))
        _v2 = val1.right_boundary
        _x = _v2
        buff.write(_struct_3i.pack(_x.x, _x.y, _x.z))
        buff.write(_struct_i.pack(val1.direction))
      _x = self
      buff.write(_struct_3H8i.pack(_x.vehicle_command, _x.sys_state, _x.plan_state, _x.speed, _x.vehicle2Flo.ID, _x.vehicle2Flo.centerX, _x.vehicle2Flo.centerY, _x.vehicle2Flo.speed, _x.vehicle2Flo.speedDirection, _x.vehicle2Flo.height, _x.vehicle2Flo.vehclass))
      length = len(self.vehicle2Flo.vehPolygon.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.vehicle2Flo.vehPolygon.points:
        _x = val1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
      buff.write(_struct_i.pack(self.vehicle2Flo.vertexNumber))
      length = len(self.vehicle2Flo.vertexX)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.vehicle2Flo.vertexX))
      length = len(self.vehicle2Flo.vertexY)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.vehicle2Flo.vertexY))
      _x = self
      buff.write(_struct_3i2d.pack(_x.point2Stop.x, _x.point2Stop.y, _x.point2Stop.z, _x.expVelocity, _x.expCurvature))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.head is None:
        self.head = std_msgs.msg.Header()
      if self.localPose is None:
        self.localPose = autonavigation.msg.LocalPose()
      if self.gpsPos is None:
        self.gpsPos = autonavigation.msg.GpsPosition()
      if self.plan_frame is None:
        self.plan_frame = autonavigation.msg.LocalCoordinate()
      if self.path is None:
        self.path = None
      if self.path_property is None:
        self.path_property = None
      if self.vehicle2Flo is None:
        self.vehicle2Flo = autonavigation.msg.VehicleObj()
      if self.point2Stop is None:
        self.point2Stop = autonavigation.msg.WayPoint()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.head.seq, _x.head.stamp.secs, _x.head.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.head.frame_id = str[start:end].decode('utf-8')
      else:
        self.head.frame_id = str[start:end]
      _x = self
      start = end
      end += 247
      (_x.localPose.time, _x.localPose.dr_x, _x.localPose.dr_y, _x.localPose.dr_z, _x.localPose.dr_heading, _x.localPose.dr_roll, _x.localPose.dr_pitch, _x.localPose.lf_speed, _x.localPose.rf_speed, _x.localPose.lr_speed, _x.localPose.rr_speed, _x.localPose.rot_x, _x.localPose.rot_y, _x.localPose.rot_z, _x.localPose.acc_x, _x.localPose.acc_y, _x.localPose.acc_z, _x.localPose.batteryState, _x.localPose.batteryEnergy, _x.localPose.steer, _x.localPose.brake, _x.localPose.fuel, _x.localPose.trans, _x.localPose.VehicleState, _x.localPose.mode, _x.localPose.drStatus, _x.localPose.errorStatus, _x.localPose.emergency_flag, _x.localPose.hardswitch_on, _x.gpsPos.gps_flag, _x.gpsPos.gps_week, _x.gpsPos.gps_millisecond, _x.gpsPos.longitude, _x.gpsPos.laltitude, _x.gpsPos.gaussX, _x.gpsPos.gaussY, _x.gpsPos.height, _x.gpsPos.pitch, _x.gpsPos.roll, _x.gpsPos.azimuth, _x.gpsPos.northVelocity, _x.gpsPos.eastVelocity, _x.gpsPos.upVelocity, _x.gpsPos.positionStatus, _x.gpsPos.rot_x, _x.gpsPos.rot_y, _x.gpsPos.rot_z, _x.gpsPos.acc_x, _x.gpsPos.acc_y, _x.gpsPos.acc_z, _x.plan_data_id, _x.plan_frame.z_x, _x.plan_frame.z_y, _x.plan_frame.g_x, _x.plan_frame.g_y, _x.plan_frame.heading, _x.plan_frame.pitch, _x.plan_frame.roll, _x.plan_frame.height, _x.plan_frame.class_id, _x.planOutputMode, _x.is_ok, _x.effective_point_num,) = _struct_d21i7bBI6d13iI8iB3H.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.path = []
      for i in range(0, length):
        val1 = autonavigation.msg.WayPoint()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3i.unpack(str[start:end])
        self.path.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.path_property = []
      for i in range(0, length):
        val1 = autonavigation.msg.PathProperty()
        _v3 = val1.left_boundary
        _x = _v3
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3i.unpack(str[start:end])
        _v4 = val1.right_boundary
        _x = _v4
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3i.unpack(str[start:end])
        start = end
        end += 4
        (val1.direction,) = _struct_i.unpack(str[start:end])
        self.path_property.append(val1)
      _x = self
      start = end
      end += 38
      (_x.vehicle_command, _x.sys_state, _x.plan_state, _x.speed, _x.vehicle2Flo.ID, _x.vehicle2Flo.centerX, _x.vehicle2Flo.centerY, _x.vehicle2Flo.speed, _x.vehicle2Flo.speedDirection, _x.vehicle2Flo.height, _x.vehicle2Flo.vehclass,) = _struct_3H8i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.vehicle2Flo.vehPolygon.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point32()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        self.vehicle2Flo.vehPolygon.points.append(val1)
      start = end
      end += 4
      (self.vehicle2Flo.vertexNumber,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.vehicle2Flo.vertexX = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.vehicle2Flo.vertexY = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 28
      (_x.point2Stop.x, _x.point2Stop.y, _x.point2Stop.z, _x.expVelocity, _x.expCurvature,) = _struct_3i2d.unpack(str[start:end])
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
      buff.write(_struct_3I.pack(_x.head.seq, _x.head.stamp.secs, _x.head.stamp.nsecs))
      _x = self.head.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_d21i7bBI6d13iI8iB3H.pack(_x.localPose.time, _x.localPose.dr_x, _x.localPose.dr_y, _x.localPose.dr_z, _x.localPose.dr_heading, _x.localPose.dr_roll, _x.localPose.dr_pitch, _x.localPose.lf_speed, _x.localPose.rf_speed, _x.localPose.lr_speed, _x.localPose.rr_speed, _x.localPose.rot_x, _x.localPose.rot_y, _x.localPose.rot_z, _x.localPose.acc_x, _x.localPose.acc_y, _x.localPose.acc_z, _x.localPose.batteryState, _x.localPose.batteryEnergy, _x.localPose.steer, _x.localPose.brake, _x.localPose.fuel, _x.localPose.trans, _x.localPose.VehicleState, _x.localPose.mode, _x.localPose.drStatus, _x.localPose.errorStatus, _x.localPose.emergency_flag, _x.localPose.hardswitch_on, _x.gpsPos.gps_flag, _x.gpsPos.gps_week, _x.gpsPos.gps_millisecond, _x.gpsPos.longitude, _x.gpsPos.laltitude, _x.gpsPos.gaussX, _x.gpsPos.gaussY, _x.gpsPos.height, _x.gpsPos.pitch, _x.gpsPos.roll, _x.gpsPos.azimuth, _x.gpsPos.northVelocity, _x.gpsPos.eastVelocity, _x.gpsPos.upVelocity, _x.gpsPos.positionStatus, _x.gpsPos.rot_x, _x.gpsPos.rot_y, _x.gpsPos.rot_z, _x.gpsPos.acc_x, _x.gpsPos.acc_y, _x.gpsPos.acc_z, _x.plan_data_id, _x.plan_frame.z_x, _x.plan_frame.z_y, _x.plan_frame.g_x, _x.plan_frame.g_y, _x.plan_frame.heading, _x.plan_frame.pitch, _x.plan_frame.roll, _x.plan_frame.height, _x.plan_frame.class_id, _x.planOutputMode, _x.is_ok, _x.effective_point_num))
      length = len(self.path)
      buff.write(_struct_I.pack(length))
      for val1 in self.path:
        _x = val1
        buff.write(_struct_3i.pack(_x.x, _x.y, _x.z))
      length = len(self.path_property)
      buff.write(_struct_I.pack(length))
      for val1 in self.path_property:
        _v5 = val1.left_boundary
        _x = _v5
        buff.write(_struct_3i.pack(_x.x, _x.y, _x.z))
        _v6 = val1.right_boundary
        _x = _v6
        buff.write(_struct_3i.pack(_x.x, _x.y, _x.z))
        buff.write(_struct_i.pack(val1.direction))
      _x = self
      buff.write(_struct_3H8i.pack(_x.vehicle_command, _x.sys_state, _x.plan_state, _x.speed, _x.vehicle2Flo.ID, _x.vehicle2Flo.centerX, _x.vehicle2Flo.centerY, _x.vehicle2Flo.speed, _x.vehicle2Flo.speedDirection, _x.vehicle2Flo.height, _x.vehicle2Flo.vehclass))
      length = len(self.vehicle2Flo.vehPolygon.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.vehicle2Flo.vehPolygon.points:
        _x = val1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
      buff.write(_struct_i.pack(self.vehicle2Flo.vertexNumber))
      length = len(self.vehicle2Flo.vertexX)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.vehicle2Flo.vertexX.tostring())
      length = len(self.vehicle2Flo.vertexY)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.vehicle2Flo.vertexY.tostring())
      _x = self
      buff.write(_struct_3i2d.pack(_x.point2Stop.x, _x.point2Stop.y, _x.point2Stop.z, _x.expVelocity, _x.expCurvature))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.head is None:
        self.head = std_msgs.msg.Header()
      if self.localPose is None:
        self.localPose = autonavigation.msg.LocalPose()
      if self.gpsPos is None:
        self.gpsPos = autonavigation.msg.GpsPosition()
      if self.plan_frame is None:
        self.plan_frame = autonavigation.msg.LocalCoordinate()
      if self.path is None:
        self.path = None
      if self.path_property is None:
        self.path_property = None
      if self.vehicle2Flo is None:
        self.vehicle2Flo = autonavigation.msg.VehicleObj()
      if self.point2Stop is None:
        self.point2Stop = autonavigation.msg.WayPoint()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.head.seq, _x.head.stamp.secs, _x.head.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.head.frame_id = str[start:end].decode('utf-8')
      else:
        self.head.frame_id = str[start:end]
      _x = self
      start = end
      end += 247
      (_x.localPose.time, _x.localPose.dr_x, _x.localPose.dr_y, _x.localPose.dr_z, _x.localPose.dr_heading, _x.localPose.dr_roll, _x.localPose.dr_pitch, _x.localPose.lf_speed, _x.localPose.rf_speed, _x.localPose.lr_speed, _x.localPose.rr_speed, _x.localPose.rot_x, _x.localPose.rot_y, _x.localPose.rot_z, _x.localPose.acc_x, _x.localPose.acc_y, _x.localPose.acc_z, _x.localPose.batteryState, _x.localPose.batteryEnergy, _x.localPose.steer, _x.localPose.brake, _x.localPose.fuel, _x.localPose.trans, _x.localPose.VehicleState, _x.localPose.mode, _x.localPose.drStatus, _x.localPose.errorStatus, _x.localPose.emergency_flag, _x.localPose.hardswitch_on, _x.gpsPos.gps_flag, _x.gpsPos.gps_week, _x.gpsPos.gps_millisecond, _x.gpsPos.longitude, _x.gpsPos.laltitude, _x.gpsPos.gaussX, _x.gpsPos.gaussY, _x.gpsPos.height, _x.gpsPos.pitch, _x.gpsPos.roll, _x.gpsPos.azimuth, _x.gpsPos.northVelocity, _x.gpsPos.eastVelocity, _x.gpsPos.upVelocity, _x.gpsPos.positionStatus, _x.gpsPos.rot_x, _x.gpsPos.rot_y, _x.gpsPos.rot_z, _x.gpsPos.acc_x, _x.gpsPos.acc_y, _x.gpsPos.acc_z, _x.plan_data_id, _x.plan_frame.z_x, _x.plan_frame.z_y, _x.plan_frame.g_x, _x.plan_frame.g_y, _x.plan_frame.heading, _x.plan_frame.pitch, _x.plan_frame.roll, _x.plan_frame.height, _x.plan_frame.class_id, _x.planOutputMode, _x.is_ok, _x.effective_point_num,) = _struct_d21i7bBI6d13iI8iB3H.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.path = []
      for i in range(0, length):
        val1 = autonavigation.msg.WayPoint()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3i.unpack(str[start:end])
        self.path.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.path_property = []
      for i in range(0, length):
        val1 = autonavigation.msg.PathProperty()
        _v7 = val1.left_boundary
        _x = _v7
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3i.unpack(str[start:end])
        _v8 = val1.right_boundary
        _x = _v8
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3i.unpack(str[start:end])
        start = end
        end += 4
        (val1.direction,) = _struct_i.unpack(str[start:end])
        self.path_property.append(val1)
      _x = self
      start = end
      end += 38
      (_x.vehicle_command, _x.sys_state, _x.plan_state, _x.speed, _x.vehicle2Flo.ID, _x.vehicle2Flo.centerX, _x.vehicle2Flo.centerY, _x.vehicle2Flo.speed, _x.vehicle2Flo.speedDirection, _x.vehicle2Flo.height, _x.vehicle2Flo.vehclass,) = _struct_3H8i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.vehicle2Flo.vehPolygon.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point32()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        self.vehicle2Flo.vehPolygon.points.append(val1)
      start = end
      end += 4
      (self.vehicle2Flo.vertexNumber,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.vehicle2Flo.vertexX = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.vehicle2Flo.vertexY = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      _x = self
      start = end
      end += 28
      (_x.point2Stop.x, _x.point2Stop.y, _x.point2Stop.z, _x.expVelocity, _x.expCurvature,) = _struct_3i2d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3i2d = struct.Struct("<3i2d")
_struct_i = struct.Struct("<i")
_struct_3H8i = struct.Struct("<3H8i")
_struct_3i = struct.Struct("<3i")
_struct_3I = struct.Struct("<3I")
_struct_d21i7bBI6d13iI8iB3H = struct.Struct("<d21i7bBI6d13iI8iB3H")
_struct_3f = struct.Struct("<3f")
