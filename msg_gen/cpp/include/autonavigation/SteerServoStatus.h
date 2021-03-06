/* Auto-generated by genmsg_cpp for file /home/abc/ros_autonavigation_ws/src/autonavigation/msg/SteerServoStatus.msg */
#ifndef AUTONAVIGATION_MESSAGE_STEERSERVOSTATUS_H
#define AUTONAVIGATION_MESSAGE_STEERSERVOSTATUS_H
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
struct SteerServoStatus_ {
  typedef SteerServoStatus_<ContainerAllocator> Type;

  SteerServoStatus_()
  : ActualFrontWheelAngle(0.0)
  , DesiredFrontWheelAngle(0.0)
  , ActualCurvature(0.0)
  , DesiredCurvature(0.0)
  , LeftLightFlag(0)
  , RightLightFlag(0)
  {
  }

  SteerServoStatus_(const ContainerAllocator& _alloc)
  : ActualFrontWheelAngle(0.0)
  , DesiredFrontWheelAngle(0.0)
  , ActualCurvature(0.0)
  , DesiredCurvature(0.0)
  , LeftLightFlag(0)
  , RightLightFlag(0)
  {
  }

  typedef double _ActualFrontWheelAngle_type;
  double ActualFrontWheelAngle;

  typedef double _DesiredFrontWheelAngle_type;
  double DesiredFrontWheelAngle;

  typedef double _ActualCurvature_type;
  double ActualCurvature;

  typedef double _DesiredCurvature_type;
  double DesiredCurvature;

  typedef int32_t _LeftLightFlag_type;
  int32_t LeftLightFlag;

  typedef int32_t _RightLightFlag_type;
  int32_t RightLightFlag;


  typedef boost::shared_ptr< ::autonavigation::SteerServoStatus_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::autonavigation::SteerServoStatus_<ContainerAllocator>  const> ConstPtr;
}; // struct SteerServoStatus
typedef  ::autonavigation::SteerServoStatus_<std::allocator<void> > SteerServoStatus;

typedef boost::shared_ptr< ::autonavigation::SteerServoStatus> SteerServoStatusPtr;
typedef boost::shared_ptr< ::autonavigation::SteerServoStatus const> SteerServoStatusConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::autonavigation::SteerServoStatus_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::autonavigation::SteerServoStatus_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace autonavigation

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::autonavigation::SteerServoStatus_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::autonavigation::SteerServoStatus_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::autonavigation::SteerServoStatus_<ContainerAllocator> > {
  static const char* value() 
  {
    return "da34259b1aca2ad0bb4d7210546aeced";
  }

  static const char* value(const  ::autonavigation::SteerServoStatus_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xda34259b1aca2ad0ULL;
  static const uint64_t static_value2 = 0xbb4d7210546aecedULL;
};

template<class ContainerAllocator>
struct DataType< ::autonavigation::SteerServoStatus_<ContainerAllocator> > {
  static const char* value() 
  {
    return "autonavigation/SteerServoStatus";
  }

  static const char* value(const  ::autonavigation::SteerServoStatus_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::autonavigation::SteerServoStatus_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float64 ActualFrontWheelAngle\n\
float64 DesiredFrontWheelAngle\n\
float64 ActualCurvature\n\
float64 DesiredCurvature\n\
int32   LeftLightFlag\n\
int32   RightLightFlag\n\
\n\
";
  }

  static const char* value(const  ::autonavigation::SteerServoStatus_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::autonavigation::SteerServoStatus_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::autonavigation::SteerServoStatus_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.ActualFrontWheelAngle);
    stream.next(m.DesiredFrontWheelAngle);
    stream.next(m.ActualCurvature);
    stream.next(m.DesiredCurvature);
    stream.next(m.LeftLightFlag);
    stream.next(m.RightLightFlag);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct SteerServoStatus_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::autonavigation::SteerServoStatus_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::autonavigation::SteerServoStatus_<ContainerAllocator> & v) 
  {
    s << indent << "ActualFrontWheelAngle: ";
    Printer<double>::stream(s, indent + "  ", v.ActualFrontWheelAngle);
    s << indent << "DesiredFrontWheelAngle: ";
    Printer<double>::stream(s, indent + "  ", v.DesiredFrontWheelAngle);
    s << indent << "ActualCurvature: ";
    Printer<double>::stream(s, indent + "  ", v.ActualCurvature);
    s << indent << "DesiredCurvature: ";
    Printer<double>::stream(s, indent + "  ", v.DesiredCurvature);
    s << indent << "LeftLightFlag: ";
    Printer<int32_t>::stream(s, indent + "  ", v.LeftLightFlag);
    s << indent << "RightLightFlag: ";
    Printer<int32_t>::stream(s, indent + "  ", v.RightLightFlag);
  }
};


} // namespace message_operations
} // namespace ros

#endif // AUTONAVIGATION_MESSAGE_STEERSERVOSTATUS_H

