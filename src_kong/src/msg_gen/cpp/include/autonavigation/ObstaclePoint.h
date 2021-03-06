/* Auto-generated by genmsg_cpp for file /home/wangyi/rosros_autonavigation_ws/src/autonavigation/msg/ObstaclePoint.msg */
#ifndef AUTONAVIGATION_MESSAGE_OBSTACLEPOINT_H
#define AUTONAVIGATION_MESSAGE_OBSTACLEPOINT_H
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
struct ObstaclePoint_ {
  typedef ObstaclePoint_<ContainerAllocator> Type;

  ObstaclePoint_()
  : x(0)
  , y(0)
  , type(0)
  {
  }

  ObstaclePoint_(const ContainerAllocator& _alloc)
  : x(0)
  , y(0)
  , type(0)
  {
  }

  typedef uint16_t _x_type;
  uint16_t x;

  typedef uint16_t _y_type;
  uint16_t y;

  typedef uint8_t _type_type;
  uint8_t type;


  typedef boost::shared_ptr< ::autonavigation::ObstaclePoint_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::autonavigation::ObstaclePoint_<ContainerAllocator>  const> ConstPtr;
}; // struct ObstaclePoint
typedef  ::autonavigation::ObstaclePoint_<std::allocator<void> > ObstaclePoint;

typedef boost::shared_ptr< ::autonavigation::ObstaclePoint> ObstaclePointPtr;
typedef boost::shared_ptr< ::autonavigation::ObstaclePoint const> ObstaclePointConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::autonavigation::ObstaclePoint_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::autonavigation::ObstaclePoint_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace autonavigation

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::autonavigation::ObstaclePoint_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::autonavigation::ObstaclePoint_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::autonavigation::ObstaclePoint_<ContainerAllocator> > {
  static const char* value() 
  {
    return "0d28ab9595e22062d30f47c355c68c7e";
  }

  static const char* value(const  ::autonavigation::ObstaclePoint_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x0d28ab9595e22062ULL;
  static const uint64_t static_value2 = 0xd30f47c355c68c7eULL;
};

template<class ContainerAllocator>
struct DataType< ::autonavigation::ObstaclePoint_<ContainerAllocator> > {
  static const char* value() 
  {
    return "autonavigation/ObstaclePoint";
  }

  static const char* value(const  ::autonavigation::ObstaclePoint_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::autonavigation::ObstaclePoint_<ContainerAllocator> > {
  static const char* value() 
  {
    return "uint16 x\n\
uint16 y\n\
uint8  type\n\
\n\
";
  }

  static const char* value(const  ::autonavigation::ObstaclePoint_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::autonavigation::ObstaclePoint_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::autonavigation::ObstaclePoint_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.x);
    stream.next(m.y);
    stream.next(m.type);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ObstaclePoint_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::autonavigation::ObstaclePoint_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::autonavigation::ObstaclePoint_<ContainerAllocator> & v) 
  {
    s << indent << "x: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.y);
    s << indent << "type: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.type);
  }
};


} // namespace message_operations
} // namespace ros

#endif // AUTONAVIGATION_MESSAGE_OBSTACLEPOINT_H

