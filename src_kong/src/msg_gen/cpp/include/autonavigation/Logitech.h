/* Auto-generated by genmsg_cpp for file /home/wangyi/rosros_autonavigation_ws/src/autonavigation/msg/Logitech.msg */
#ifndef AUTONAVIGATION_MESSAGE_LOGITECH_H
#define AUTONAVIGATION_MESSAGE_LOGITECH_H
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
struct Logitech_ {
  typedef Logitech_<ContainerAllocator> Type;

  Logitech_()
  : SteeringWheel(0)
  , Clutch(0)
  , Brake(0)
  , SasPedal(0)
  , ShiftPaddlesL(0)
  , ShiftPaddlesR(0)
  , Ignition(0)
  , HandBrake(0)
  , StickShift(0)
  , CrossL(0)
  , CrossR(0)
  , ManualTransmission(0)
  , WheelFunctionKey()
  , ConcatenonSignal(0)
  , cmd_reserve2(0)
  , cmd_reserve3(0)
  , cmd_reserve4(0)
  , cmd_reserve5(0)
  {
  }

  Logitech_(const ContainerAllocator& _alloc)
  : SteeringWheel(0)
  , Clutch(0)
  , Brake(0)
  , SasPedal(0)
  , ShiftPaddlesL(0)
  , ShiftPaddlesR(0)
  , Ignition(0)
  , HandBrake(0)
  , StickShift(0)
  , CrossL(0)
  , CrossR(0)
  , ManualTransmission(0)
  , WheelFunctionKey(_alloc)
  , ConcatenonSignal(0)
  , cmd_reserve2(0)
  , cmd_reserve3(0)
  , cmd_reserve4(0)
  , cmd_reserve5(0)
  {
  }

  typedef int16_t _SteeringWheel_type;
  int16_t SteeringWheel;

  typedef uint8_t _Clutch_type;
  uint8_t Clutch;

  typedef uint8_t _Brake_type;
  uint8_t Brake;

  typedef uint8_t _SasPedal_type;
  uint8_t SasPedal;

  typedef uint8_t _ShiftPaddlesL_type;
  uint8_t ShiftPaddlesL;

  typedef uint8_t _ShiftPaddlesR_type;
  uint8_t ShiftPaddlesR;

  typedef uint8_t _Ignition_type;
  uint8_t Ignition;

  typedef uint8_t _HandBrake_type;
  uint8_t HandBrake;

  typedef uint8_t _StickShift_type;
  uint8_t StickShift;

  typedef uint8_t _CrossL_type;
  uint8_t CrossL;

  typedef uint8_t _CrossR_type;
  uint8_t CrossR;

  typedef uint8_t _ManualTransmission_type;
  uint8_t ManualTransmission;

  typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _WheelFunctionKey_type;
  std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  WheelFunctionKey;

  typedef uint8_t _ConcatenonSignal_type;
  uint8_t ConcatenonSignal;

  typedef uint8_t _cmd_reserve2_type;
  uint8_t cmd_reserve2;

  typedef uint8_t _cmd_reserve3_type;
  uint8_t cmd_reserve3;

  typedef uint8_t _cmd_reserve4_type;
  uint8_t cmd_reserve4;

  typedef uint8_t _cmd_reserve5_type;
  uint8_t cmd_reserve5;


  typedef boost::shared_ptr< ::autonavigation::Logitech_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::autonavigation::Logitech_<ContainerAllocator>  const> ConstPtr;
}; // struct Logitech
typedef  ::autonavigation::Logitech_<std::allocator<void> > Logitech;

typedef boost::shared_ptr< ::autonavigation::Logitech> LogitechPtr;
typedef boost::shared_ptr< ::autonavigation::Logitech const> LogitechConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::autonavigation::Logitech_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::autonavigation::Logitech_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace autonavigation

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::autonavigation::Logitech_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::autonavigation::Logitech_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::autonavigation::Logitech_<ContainerAllocator> > {
  static const char* value() 
  {
    return "514b52ad33f160a6fe6f8bec1d48757b";
  }

  static const char* value(const  ::autonavigation::Logitech_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x514b52ad33f160a6ULL;
  static const uint64_t static_value2 = 0xfe6f8bec1d48757bULL;
};

template<class ContainerAllocator>
struct DataType< ::autonavigation::Logitech_<ContainerAllocator> > {
  static const char* value() 
  {
    return "autonavigation/Logitech";
  }

  static const char* value(const  ::autonavigation::Logitech_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::autonavigation::Logitech_<ContainerAllocator> > {
  static const char* value() 
  {
    return "#罗技力G27反馈方向盘\n\
\n\
int16 SteeringWheel #规定右正左负值变化：0-540 \n\
uint8 Clutch #离合器值：0-100，放松状态为0\n\
uint8 Brake #刹车值:0-100，放松状态为0\n\
uint8 SasPedal #油门值:0-100,放松状态为0\n\
uint8 ShiftPaddlesL #左换档拨片定义为降档,空状态为0,按下为1\n\
uint8 ShiftPaddlesR #右换档拨片定义为升档，空状态为0,按下为1\n\
uint8 Ignition #点火为1,熄火为2,空状态为0\n\
uint8 HandBrake #松手刹为1,拉手刹为2,空状态为0\n\
uint8 StickShift #自动档，由十字架上下按键操作 0为P，1为R，2为N，3为D,4为S, 5为L 6为空档，7为切换到换档拨片\n\
uint8 CrossL #十字架左键\n\
uint8 CrossR #十字架右键\n\
uint8 ManualTransmission #手动档换档杆:第一排依次为1,3,5档，第二排依次为2,4,6,R档\n\
uint8[]  WheelFunctionKey #方向盘6个红色功能键 \n\
uint8 ConcatenonSignal #未连接初始值为0,连接成功为1\n\
uint8 cmd_reserve2 #预留\n\
uint8 cmd_reserve3 #预留\n\
uint8 cmd_reserve4 #预留\n\
uint8 cmd_reserve5 #预留\n\
\n\
";
  }

  static const char* value(const  ::autonavigation::Logitech_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::autonavigation::Logitech_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.SteeringWheel);
    stream.next(m.Clutch);
    stream.next(m.Brake);
    stream.next(m.SasPedal);
    stream.next(m.ShiftPaddlesL);
    stream.next(m.ShiftPaddlesR);
    stream.next(m.Ignition);
    stream.next(m.HandBrake);
    stream.next(m.StickShift);
    stream.next(m.CrossL);
    stream.next(m.CrossR);
    stream.next(m.ManualTransmission);
    stream.next(m.WheelFunctionKey);
    stream.next(m.ConcatenonSignal);
    stream.next(m.cmd_reserve2);
    stream.next(m.cmd_reserve3);
    stream.next(m.cmd_reserve4);
    stream.next(m.cmd_reserve5);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct Logitech_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::autonavigation::Logitech_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::autonavigation::Logitech_<ContainerAllocator> & v) 
  {
    s << indent << "SteeringWheel: ";
    Printer<int16_t>::stream(s, indent + "  ", v.SteeringWheel);
    s << indent << "Clutch: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Clutch);
    s << indent << "Brake: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Brake);
    s << indent << "SasPedal: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.SasPedal);
    s << indent << "ShiftPaddlesL: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ShiftPaddlesL);
    s << indent << "ShiftPaddlesR: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ShiftPaddlesR);
    s << indent << "Ignition: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Ignition);
    s << indent << "HandBrake: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.HandBrake);
    s << indent << "StickShift: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.StickShift);
    s << indent << "CrossL: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.CrossL);
    s << indent << "CrossR: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.CrossR);
    s << indent << "ManualTransmission: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ManualTransmission);
    s << indent << "WheelFunctionKey[]" << std::endl;
    for (size_t i = 0; i < v.WheelFunctionKey.size(); ++i)
    {
      s << indent << "  WheelFunctionKey[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.WheelFunctionKey[i]);
    }
    s << indent << "ConcatenonSignal: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ConcatenonSignal);
    s << indent << "cmd_reserve2: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.cmd_reserve2);
    s << indent << "cmd_reserve3: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.cmd_reserve3);
    s << indent << "cmd_reserve4: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.cmd_reserve4);
    s << indent << "cmd_reserve5: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.cmd_reserve5);
  }
};


} // namespace message_operations
} // namespace ros

#endif // AUTONAVIGATION_MESSAGE_LOGITECH_H

