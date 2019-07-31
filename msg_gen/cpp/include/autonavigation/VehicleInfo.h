/* Auto-generated by genmsg_cpp for file /home/abc/ros_autonavigation_ws/src/autonavigation/msg/VehicleInfo.msg */
#ifndef AUTONAVIGATION_MESSAGE_VEHICLEINFO_H
#define AUTONAVIGATION_MESSAGE_VEHICLEINFO_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"
#include "autonavigation/LocalPose.h"
#include "autonavigation/GpsPosition.h"
#include "autonavigation/VehicleObj.h"

namespace autonavigation
{
template <class ContainerAllocator>
struct VehicleInfo_ {
  typedef VehicleInfo_<ContainerAllocator> Type;

  VehicleInfo_()
  : head()
  , localPose()
  , gpsPos()
  , vehicleNum(0)
  , vehicles()
  {
  }

  VehicleInfo_(const ContainerAllocator& _alloc)
  : head(_alloc)
  , localPose(_alloc)
  , gpsPos(_alloc)
  , vehicleNum(0)
  , vehicles(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _head_type;
   ::std_msgs::Header_<ContainerAllocator>  head;

  typedef  ::autonavigation::LocalPose_<ContainerAllocator>  _localPose_type;
   ::autonavigation::LocalPose_<ContainerAllocator>  localPose;

  typedef  ::autonavigation::GpsPosition_<ContainerAllocator>  _gpsPos_type;
   ::autonavigation::GpsPosition_<ContainerAllocator>  gpsPos;

  typedef int32_t _vehicleNum_type;
  int32_t vehicleNum;

  typedef std::vector< ::autonavigation::VehicleObj_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::autonavigation::VehicleObj_<ContainerAllocator> >::other >  _vehicles_type;
  std::vector< ::autonavigation::VehicleObj_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::autonavigation::VehicleObj_<ContainerAllocator> >::other >  vehicles;


  typedef boost::shared_ptr< ::autonavigation::VehicleInfo_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::autonavigation::VehicleInfo_<ContainerAllocator>  const> ConstPtr;
}; // struct VehicleInfo
typedef  ::autonavigation::VehicleInfo_<std::allocator<void> > VehicleInfo;

typedef boost::shared_ptr< ::autonavigation::VehicleInfo> VehicleInfoPtr;
typedef boost::shared_ptr< ::autonavigation::VehicleInfo const> VehicleInfoConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::autonavigation::VehicleInfo_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::autonavigation::VehicleInfo_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace autonavigation

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::autonavigation::VehicleInfo_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::autonavigation::VehicleInfo_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::autonavigation::VehicleInfo_<ContainerAllocator> > {
  static const char* value() 
  {
    return "cfd47a6e913d2b0b7e6b6b0972f6e337";
  }

  static const char* value(const  ::autonavigation::VehicleInfo_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xcfd47a6e913d2b0bULL;
  static const uint64_t static_value2 = 0x7e6b6b0972f6e337ULL;
};

template<class ContainerAllocator>
struct DataType< ::autonavigation::VehicleInfo_<ContainerAllocator> > {
  static const char* value() 
  {
    return "autonavigation/VehicleInfo";
  }

  static const char* value(const  ::autonavigation::VehicleInfo_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::autonavigation::VehicleInfo_<ContainerAllocator> > {
  static const char* value() 
  {
    return "Header      head\n\
LocalPose   localPose\n\
GpsPosition gpsPos\n\
\n\
int32        vehicleNum\n\
VehicleObj[] vehicles\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: autonavigation/LocalPose\n\
#LocalPose msg\n\
\n\
float64 time			  \n\
#centimeter  \n\
int32 dr_x\n\
int32 dr_y\n\
int32 dr_z\n\
#0.01degree\n\
int32 dr_heading\n\
int32 dr_roll\n\
int32 dr_pitch		    \n\
\n\
#left_front wheel speed,cm/s\n\
int32 lf_speed\n\
#right_front wheel speed,cm/s		    \n\
int32 rf_speed\n\
#left_rear wheel speed,cm/s		    \n\
int32 lr_speed\n\
#right_rear wheel speed,cm/s		    \n\
int32 rr_speed		    \n\
\n\
#imu三轴陀螺速度 0.01degree/s\n\
int32 rot_x\n\
int32 rot_y                      \n\
int32 rot_z                      \n\
#imu三轴加速度  0.01m/s^2\n\
int32 acc_x                      \n\
int32 acc_y                      \n\
int32 acc_z                      \n\
\n\
int32 batteryState\n\
int32 batteryEnergy           #0-100\n\
\n\
#-3000(right)~3000(left) degree  0.01degree/s\n\
int32 steer   \n\
#0(zero)~100(full)                  \n\
int32 brake                 \n\
#0(zero)~100(full)     \n\
int32 fuel      \n\
#PARK=0,BACKWARD=1,NEURAL=2,FORWARD=3                 \n\
int8  trans                      \n\
int8  VehicleState\n\
#DIRECT_ACTUATOR=0,REMOTE_PILOT=1,AUTO_PILOT=2\n\
int8  mode                       \n\
#dr运行状态\n\
int8 drStatus\n\
#错误状态		    \n\
int8 errorStatus		    \n\
int8 emergency_flag\n\
int8 hardswitch_on\n\
\n\
\n\
================================================================================\n\
MSG: autonavigation/GpsPosition\n\
#gps info is updated\n\
char          gps_flag               \n\
uint32        gps_week\n\
#millisecond in a week\n\
float64       gps_millisecond   \n\
#经纬度，单位为度     \n\
float64	      longitude		      \n\
float64	      laltitude\n\
#高斯投影位置,cm\n\
float64	      gaussX		      \n\
float64       gaussY\n\
#height,     cm\n\
float64         height  \n\
#欧拉角，单位为0.01度                \n\
int32         pitch                   \n\
int32         roll\n\
#欧拉角，单位为0.01度,向东为零度，逆时针0-360                    \n\
int32         azimuth                 \n\
\n\
#north速度，单位为cm/s\n\
int32         northVelocity           \n\
int32         eastVelocity\n\
int32         upVelocity\n\
#系统运行状态\n\
int32         positionStatus	      \n\
\n\
#imu三轴陀螺速度 0.01degree/s\n\
int32	        rot_x                      \n\
int32           rot_y                      \n\
int32           rot_z                      \n\
\n\
#imu三轴加速度  0.01m/s^2\n\
int32           acc_x                      \n\
int32           acc_y                      \n\
int32           acc_z                      \n\
	\n\
\n\
================================================================================\n\
MSG: autonavigation/VehicleObj\n\
#ID num\n\
int32 ID       \n\
# position, cm\n\
int32 centerX\n\
int32 centerY\n\
# cm/s\n\
int32 speed        \n\
# 0.01degree   \n\
int32 speedDirection  \n\
int32 height         \n\
# car, truck, bicycle, big obj, small obj, unknown obj \n\
int32 vehclass     \n\
\n\
geometry_msgs/Polygon vehPolygon      \n\
\n\
int32   vertexNumber\n\
int32[] vertexX\n\
int32[] vertexY\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Polygon\n\
#A specification of a polygon where the first and last points are assumed to be connected\n\
Point32[] points\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point32\n\
# This contains the position of a point in free space(with 32 bits of precision).\n\
# It is recommeded to use Point wherever possible instead of Point32.  \n\
# \n\
# This recommendation is to promote interoperability.  \n\
#\n\
# This message is designed to take up less space when sending\n\
# lots of points at once, as in the case of a PointCloud.  \n\
\n\
float32 x\n\
float32 y\n\
float32 z\n\
";
  }

  static const char* value(const  ::autonavigation::VehicleInfo_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::autonavigation::VehicleInfo_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.head);
    stream.next(m.localPose);
    stream.next(m.gpsPos);
    stream.next(m.vehicleNum);
    stream.next(m.vehicles);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct VehicleInfo_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::autonavigation::VehicleInfo_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::autonavigation::VehicleInfo_<ContainerAllocator> & v) 
  {
    s << indent << "head: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.head);
    s << indent << "localPose: ";
s << std::endl;
    Printer< ::autonavigation::LocalPose_<ContainerAllocator> >::stream(s, indent + "  ", v.localPose);
    s << indent << "gpsPos: ";
s << std::endl;
    Printer< ::autonavigation::GpsPosition_<ContainerAllocator> >::stream(s, indent + "  ", v.gpsPos);
    s << indent << "vehicleNum: ";
    Printer<int32_t>::stream(s, indent + "  ", v.vehicleNum);
    s << indent << "vehicles[]" << std::endl;
    for (size_t i = 0; i < v.vehicles.size(); ++i)
    {
      s << indent << "  vehicles[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::autonavigation::VehicleObj_<ContainerAllocator> >::stream(s, indent + "    ", v.vehicles[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // AUTONAVIGATION_MESSAGE_VEHICLEINFO_H
