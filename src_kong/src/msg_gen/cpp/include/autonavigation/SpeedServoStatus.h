/* Auto-generated by genmsg_cpp for file /home/wangyi/rosros_autonavigation_ws/src/autonavigation/msg/SpeedServoStatus.msg */
#ifndef AUTONAVIGATION_MESSAGE_SPEEDSERVOSTATUS_H
#define AUTONAVIGATION_MESSAGE_SPEEDSERVOSTATUS_H
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
struct SpeedServoStatus_ {
  typedef SpeedServoStatus_<ContainerAllocator> Type;

  SpeedServoStatus_()
  : DesiredSpeed(0.0)
  , DesiredAcc(0.0)
  , CurrentSpeed(0.0)
  , CurrentAcc(0.0)
  , DesiredBrake(0.0)
  , CurrentBrake(0.0)
  , DesiredFuel(0.0)
  , CurrentFuel(0.0)
  , DesiredTransPos(0)
  , CurrentTransPos(0)
  , HardSwitchOn(0)
  , EmergenceFlag(0)
  , BcanControlFlag(0)
  , HornOnFlag(0)
  , EmergencyLightonFlag(0)
  {
  }

  SpeedServoStatus_(const ContainerAllocator& _alloc)
  : DesiredSpeed(0.0)
  , DesiredAcc(0.0)
  , CurrentSpeed(0.0)
  , CurrentAcc(0.0)
  , DesiredBrake(0.0)
  , CurrentBrake(0.0)
  , DesiredFuel(0.0)
  , CurrentFuel(0.0)
  , DesiredTransPos(0)
  , CurrentTransPos(0)
  , HardSwitchOn(0)
  , EmergenceFlag(0)
  , BcanControlFlag(0)
  , HornOnFlag(0)
  , EmergencyLightonFlag(0)
  {
  }

  typedef double _DesiredSpeed_type;
  double DesiredSpeed;

  typedef double _DesiredAcc_type;
  double DesiredAcc;

  typedef double _CurrentSpeed_type;
  double CurrentSpeed;

  typedef double _CurrentAcc_type;
  double CurrentAcc;

  typedef double _DesiredBrake_type;
  double DesiredBrake;

  typedef double _CurrentBrake_type;
  double CurrentBrake;

  typedef double _DesiredFuel_type;
  double DesiredFuel;

  typedef double _CurrentFuel_type;
  double CurrentFuel;

  typedef int32_t _DesiredTransPos_type;
  int32_t DesiredTransPos;

  typedef int32_t _CurrentTransPos_type;
  int32_t CurrentTransPos;

  typedef int32_t _HardSwitchOn_type;
  int32_t HardSwitchOn;

  typedef int32_t _EmergenceFlag_type;
  int32_t EmergenceFlag;

  typedef int32_t _BcanControlFlag_type;
  int32_t BcanControlFlag;

  typedef int32_t _HornOnFlag_type;
  int32_t HornOnFlag;

  typedef int32_t _EmergencyLightonFlag_type;
  int32_t EmergencyLightonFlag;


  typedef boost::shared_ptr< ::autonavigation::SpeedServoStatus_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::autonavigation::SpeedServoStatus_<ContainerAllocator>  const> ConstPtr;
}; // struct SpeedServoStatus
typedef  ::autonavigation::SpeedServoStatus_<std::allocator<void> > SpeedServoStatus;

typedef boost::shared_ptr< ::autonavigation::SpeedServoStatus> SpeedServoStatusPtr;
typedef boost::shared_ptr< ::autonavigation::SpeedServoStatus const> SpeedServoStatusConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::autonavigation::SpeedServoStatus_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::autonavigation::SpeedServoStatus_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace autonavigation

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::autonavigation::SpeedServoStatus_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::autonavigation::SpeedServoStatus_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::autonavigation::SpeedServoStatus_<ContainerAllocator> > {
  static const char* value() 
  {
    return "91bbb94b1c08c13aa4b81b868ef0ac37";
  }

  static const char* value(const  ::autonavigation::SpeedServoStatus_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x91bbb94b1c08c13aULL;
  static const uint64_t static_value2 = 0xa4b81b868ef0ac37ULL;
};

template<class ContainerAllocator>
struct DataType< ::autonavigation::SpeedServoStatus_<ContainerAllocator> > {
  static const char* value() 
  {
    return "autonavigation/SpeedServoStatus";
  }

  static const char* value(const  ::autonavigation::SpeedServoStatus_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::autonavigation::SpeedServoStatus_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float64 DesiredSpeed\n\
float64 DesiredAcc\n\
float64 CurrentSpeed\n\
float64 CurrentAcc\n\
float64 DesiredBrake\n\
float64 CurrentBrake\n\
float64 DesiredFuel\n\
float64 CurrentFuel\n\
int32 DesiredTransPos\n\
int32 CurrentTransPos\n\
int32 HardSwitchOn\n\
int32 EmergenceFlag\n\
int32 BcanControlFlag\n\
int32 HornOnFlag\n\
int32 EmergencyLightonFlag\n\
\n\
\n\
\n\
";
  }

  static const char* value(const  ::autonavigation::SpeedServoStatus_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::autonavigation::SpeedServoStatus_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::autonavigation::SpeedServoStatus_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.DesiredSpeed);
    stream.next(m.DesiredAcc);
    stream.next(m.CurrentSpeed);
    stream.next(m.CurrentAcc);
    stream.next(m.DesiredBrake);
    stream.next(m.CurrentBrake);
    stream.next(m.DesiredFuel);
    stream.next(m.CurrentFuel);
    stream.next(m.DesiredTransPos);
    stream.next(m.CurrentTransPos);
    stream.next(m.HardSwitchOn);
    stream.next(m.EmergenceFlag);
    stream.next(m.BcanControlFlag);
    stream.next(m.HornOnFlag);
    stream.next(m.EmergencyLightonFlag);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct SpeedServoStatus_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::autonavigation::SpeedServoStatus_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::autonavigation::SpeedServoStatus_<ContainerAllocator> & v) 
  {
    s << indent << "DesiredSpeed: ";
    Printer<double>::stream(s, indent + "  ", v.DesiredSpeed);
    s << indent << "DesiredAcc: ";
    Printer<double>::stream(s, indent + "  ", v.DesiredAcc);
    s << indent << "CurrentSpeed: ";
    Printer<double>::stream(s, indent + "  ", v.CurrentSpeed);
    s << indent << "CurrentAcc: ";
    Printer<double>::stream(s, indent + "  ", v.CurrentAcc);
    s << indent << "DesiredBrake: ";
    Printer<double>::stream(s, indent + "  ", v.DesiredBrake);
    s << indent << "CurrentBrake: ";
    Printer<double>::stream(s, indent + "  ", v.CurrentBrake);
    s << indent << "DesiredFuel: ";
    Printer<double>::stream(s, indent + "  ", v.DesiredFuel);
    s << indent << "CurrentFuel: ";
    Printer<double>::stream(s, indent + "  ", v.CurrentFuel);
    s << indent << "DesiredTransPos: ";
    Printer<int32_t>::stream(s, indent + "  ", v.DesiredTransPos);
    s << indent << "CurrentTransPos: ";
    Printer<int32_t>::stream(s, indent + "  ", v.CurrentTransPos);
    s << indent << "HardSwitchOn: ";
    Printer<int32_t>::stream(s, indent + "  ", v.HardSwitchOn);
    s << indent << "EmergenceFlag: ";
    Printer<int32_t>::stream(s, indent + "  ", v.EmergenceFlag);
    s << indent << "BcanControlFlag: ";
    Printer<int32_t>::stream(s, indent + "  ", v.BcanControlFlag);
    s << indent << "HornOnFlag: ";
    Printer<int32_t>::stream(s, indent + "  ", v.HornOnFlag);
    s << indent << "EmergencyLightonFlag: ";
    Printer<int32_t>::stream(s, indent + "  ", v.EmergencyLightonFlag);
  }
};


} // namespace message_operations
} // namespace ros

#endif // AUTONAVIGATION_MESSAGE_SPEEDSERVOSTATUS_H

