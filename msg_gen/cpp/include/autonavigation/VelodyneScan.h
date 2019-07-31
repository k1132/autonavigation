/* Auto-generated by genmsg_cpp for file /home/abc/ros_autonavigation_ws/src/autonavigation/msg/VelodyneScan.msg */
#ifndef AUTONAVIGATION_MESSAGE_VELODYNESCAN_H
#define AUTONAVIGATION_MESSAGE_VELODYNESCAN_H
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
#include "autonavigation/VelodynePacket.h"

namespace autonavigation
{
template <class ContainerAllocator>
struct VelodyneScan_ {
  typedef VelodyneScan_<ContainerAllocator> Type;

  VelodyneScan_()
  : header()
  , localPose()
  , gpsPos()
  , packets()
  {
  }

  VelodyneScan_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , localPose(_alloc)
  , gpsPos(_alloc)
  , packets(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef  ::autonavigation::LocalPose_<ContainerAllocator>  _localPose_type;
   ::autonavigation::LocalPose_<ContainerAllocator>  localPose;

  typedef  ::autonavigation::GpsPosition_<ContainerAllocator>  _gpsPos_type;
   ::autonavigation::GpsPosition_<ContainerAllocator>  gpsPos;

  typedef std::vector< ::autonavigation::VelodynePacket_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::autonavigation::VelodynePacket_<ContainerAllocator> >::other >  _packets_type;
  std::vector< ::autonavigation::VelodynePacket_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::autonavigation::VelodynePacket_<ContainerAllocator> >::other >  packets;


  typedef boost::shared_ptr< ::autonavigation::VelodyneScan_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::autonavigation::VelodyneScan_<ContainerAllocator>  const> ConstPtr;
}; // struct VelodyneScan
typedef  ::autonavigation::VelodyneScan_<std::allocator<void> > VelodyneScan;

typedef boost::shared_ptr< ::autonavigation::VelodyneScan> VelodyneScanPtr;
typedef boost::shared_ptr< ::autonavigation::VelodyneScan const> VelodyneScanConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::autonavigation::VelodyneScan_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::autonavigation::VelodyneScan_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace autonavigation

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::autonavigation::VelodyneScan_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::autonavigation::VelodyneScan_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::autonavigation::VelodyneScan_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b84db49b197bce2da993f944c9202cd1";
  }

  static const char* value(const  ::autonavigation::VelodyneScan_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xb84db49b197bce2dULL;
  static const uint64_t static_value2 = 0xa993f944c9202cd1ULL;
};

template<class ContainerAllocator>
struct DataType< ::autonavigation::VelodyneScan_<ContainerAllocator> > {
  static const char* value() 
  {
    return "autonavigation/VelodyneScan";
  }

  static const char* value(const  ::autonavigation::VelodyneScan_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::autonavigation::VelodyneScan_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# Velodyne LIDAR scan packets.\n\
\n\
Header           header         # standard ROS message header\n\
LocalPose   localPose\n\
GpsPosition gpsPos\n\
\n\
VelodynePacket[] packets        # vector of raw packets\n\
\n\
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
MSG: autonavigation/VelodynePacket\n\
# Raw Velodyne LIDAR packet.\n\
\n\
time stamp              # packet timestamp\n\
uint8[1206] data        # packet contents\n\
\n\
\n\
";
  }

  static const char* value(const  ::autonavigation::VelodyneScan_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::autonavigation::VelodyneScan_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::autonavigation::VelodyneScan_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::autonavigation::VelodyneScan_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.localPose);
    stream.next(m.gpsPos);
    stream.next(m.packets);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct VelodyneScan_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::autonavigation::VelodyneScan_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::autonavigation::VelodyneScan_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "localPose: ";
s << std::endl;
    Printer< ::autonavigation::LocalPose_<ContainerAllocator> >::stream(s, indent + "  ", v.localPose);
    s << indent << "gpsPos: ";
s << std::endl;
    Printer< ::autonavigation::GpsPosition_<ContainerAllocator> >::stream(s, indent + "  ", v.gpsPos);
    s << indent << "packets[]" << std::endl;
    for (size_t i = 0; i < v.packets.size(); ++i)
    {
      s << indent << "  packets[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::autonavigation::VelodynePacket_<ContainerAllocator> >::stream(s, indent + "    ", v.packets[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // AUTONAVIGATION_MESSAGE_VELODYNESCAN_H
