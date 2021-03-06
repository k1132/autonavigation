/* Auto-generated by genmsg_cpp for file /home/wangyi/rosros_autonavigation_ws/src/autonavigation/msg/GpsPosition.msg */
#ifndef AUTONAVIGATION_MESSAGE_GPSPOSITION_H
#define AUTONAVIGATION_MESSAGE_GPSPOSITION_H
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


namespace autonavigation
{
template <class ContainerAllocator>
struct GpsPosition_ {
  typedef GpsPosition_<ContainerAllocator> Type;

  GpsPosition_()
  : gps_flag(0)
  , gps_week(0)
  , gps_millisecond(0.0)
  , longitude(0.0)
  , laltitude(0.0)
  , gaussX(0.0)
  , gaussY(0.0)
  , height(0.0)
  , pitch(0)
  , roll(0)
  , azimuth(0)
  , northVelocity(0)
  , eastVelocity(0)
  , upVelocity(0)
  , positionStatus(0)
  , rot_x(0)
  , rot_y(0)
  , rot_z(0)
  , acc_x(0)
  , acc_y(0)
  , acc_z(0)
  {
  }

  GpsPosition_(const ContainerAllocator& _alloc)
  : gps_flag(0)
  , gps_week(0)
  , gps_millisecond(0.0)
  , longitude(0.0)
  , laltitude(0.0)
  , gaussX(0.0)
  , gaussY(0.0)
  , height(0.0)
  , pitch(0)
  , roll(0)
  , azimuth(0)
  , northVelocity(0)
  , eastVelocity(0)
  , upVelocity(0)
  , positionStatus(0)
  , rot_x(0)
  , rot_y(0)
  , rot_z(0)
  , acc_x(0)
  , acc_y(0)
  , acc_z(0)
  {
  }

  typedef uint8_t _gps_flag_type;
  uint8_t gps_flag;

  typedef uint32_t _gps_week_type;
  uint32_t gps_week;

  typedef double _gps_millisecond_type;
  double gps_millisecond;

  typedef double _longitude_type;
  double longitude;

  typedef double _laltitude_type;
  double laltitude;

  typedef double _gaussX_type;
  double gaussX;

  typedef double _gaussY_type;
  double gaussY;

  typedef double _height_type;
  double height;

  typedef int32_t _pitch_type;
  int32_t pitch;

  typedef int32_t _roll_type;
  int32_t roll;

  typedef int32_t _azimuth_type;
  int32_t azimuth;

  typedef int32_t _northVelocity_type;
  int32_t northVelocity;

  typedef int32_t _eastVelocity_type;
  int32_t eastVelocity;

  typedef int32_t _upVelocity_type;
  int32_t upVelocity;

  typedef int32_t _positionStatus_type;
  int32_t positionStatus;

  typedef int32_t _rot_x_type;
  int32_t rot_x;

  typedef int32_t _rot_y_type;
  int32_t rot_y;

  typedef int32_t _rot_z_type;
  int32_t rot_z;

  typedef int32_t _acc_x_type;
  int32_t acc_x;

  typedef int32_t _acc_y_type;
  int32_t acc_y;

  typedef int32_t _acc_z_type;
  int32_t acc_z;


  typedef boost::shared_ptr< ::autonavigation::GpsPosition_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::autonavigation::GpsPosition_<ContainerAllocator>  const> ConstPtr;
}; // struct GpsPosition
typedef  ::autonavigation::GpsPosition_<std::allocator<void> > GpsPosition;

typedef boost::shared_ptr< ::autonavigation::GpsPosition> GpsPositionPtr;
typedef boost::shared_ptr< ::autonavigation::GpsPosition const> GpsPositionConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::autonavigation::GpsPosition_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::autonavigation::GpsPosition_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace autonavigation

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::autonavigation::GpsPosition_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::autonavigation::GpsPosition_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::autonavigation::GpsPosition_<ContainerAllocator> > {
  static const char* value() 
  {
    return "23f605ef77c75aec90e8a95d7f54bcb5";
  }

  static const char* value(const  ::autonavigation::GpsPosition_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x23f605ef77c75aecULL;
  static const uint64_t static_value2 = 0x90e8a95d7f54bcb5ULL;
};

template<class ContainerAllocator>
struct DataType< ::autonavigation::GpsPosition_<ContainerAllocator> > {
  static const char* value() 
  {
    return "autonavigation/GpsPosition";
  }

  static const char* value(const  ::autonavigation::GpsPosition_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::autonavigation::GpsPosition_<ContainerAllocator> > {
  static const char* value() 
  {
    return "#gps info is updated\n\
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
";
  }

  static const char* value(const  ::autonavigation::GpsPosition_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::autonavigation::GpsPosition_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::autonavigation::GpsPosition_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.gps_flag);
    stream.next(m.gps_week);
    stream.next(m.gps_millisecond);
    stream.next(m.longitude);
    stream.next(m.laltitude);
    stream.next(m.gaussX);
    stream.next(m.gaussY);
    stream.next(m.height);
    stream.next(m.pitch);
    stream.next(m.roll);
    stream.next(m.azimuth);
    stream.next(m.northVelocity);
    stream.next(m.eastVelocity);
    stream.next(m.upVelocity);
    stream.next(m.positionStatus);
    stream.next(m.rot_x);
    stream.next(m.rot_y);
    stream.next(m.rot_z);
    stream.next(m.acc_x);
    stream.next(m.acc_y);
    stream.next(m.acc_z);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct GpsPosition_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::autonavigation::GpsPosition_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::autonavigation::GpsPosition_<ContainerAllocator> & v) 
  {
    s << indent << "gps_flag: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.gps_flag);
    s << indent << "gps_week: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.gps_week);
    s << indent << "gps_millisecond: ";
    Printer<double>::stream(s, indent + "  ", v.gps_millisecond);
    s << indent << "longitude: ";
    Printer<double>::stream(s, indent + "  ", v.longitude);
    s << indent << "laltitude: ";
    Printer<double>::stream(s, indent + "  ", v.laltitude);
    s << indent << "gaussX: ";
    Printer<double>::stream(s, indent + "  ", v.gaussX);
    s << indent << "gaussY: ";
    Printer<double>::stream(s, indent + "  ", v.gaussY);
    s << indent << "height: ";
    Printer<double>::stream(s, indent + "  ", v.height);
    s << indent << "pitch: ";
    Printer<int32_t>::stream(s, indent + "  ", v.pitch);
    s << indent << "roll: ";
    Printer<int32_t>::stream(s, indent + "  ", v.roll);
    s << indent << "azimuth: ";
    Printer<int32_t>::stream(s, indent + "  ", v.azimuth);
    s << indent << "northVelocity: ";
    Printer<int32_t>::stream(s, indent + "  ", v.northVelocity);
    s << indent << "eastVelocity: ";
    Printer<int32_t>::stream(s, indent + "  ", v.eastVelocity);
    s << indent << "upVelocity: ";
    Printer<int32_t>::stream(s, indent + "  ", v.upVelocity);
    s << indent << "positionStatus: ";
    Printer<int32_t>::stream(s, indent + "  ", v.positionStatus);
    s << indent << "rot_x: ";
    Printer<int32_t>::stream(s, indent + "  ", v.rot_x);
    s << indent << "rot_y: ";
    Printer<int32_t>::stream(s, indent + "  ", v.rot_y);
    s << indent << "rot_z: ";
    Printer<int32_t>::stream(s, indent + "  ", v.rot_z);
    s << indent << "acc_x: ";
    Printer<int32_t>::stream(s, indent + "  ", v.acc_x);
    s << indent << "acc_y: ";
    Printer<int32_t>::stream(s, indent + "  ", v.acc_y);
    s << indent << "acc_z: ";
    Printer<int32_t>::stream(s, indent + "  ", v.acc_z);
  }
};


} // namespace message_operations
} // namespace ros

#endif // AUTONAVIGATION_MESSAGE_GPSPOSITION_H

