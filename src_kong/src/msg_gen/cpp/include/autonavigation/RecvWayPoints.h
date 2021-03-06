/* Auto-generated by genmsg_cpp for file /home/wangyi/rosros_autonavigation_ws/src/autonavigation/msg/RecvWayPoints.msg */
#ifndef AUTONAVIGATION_MESSAGE_RECVWAYPOINTS_H
#define AUTONAVIGATION_MESSAGE_RECVWAYPOINTS_H
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
struct RecvWayPoints_ {
  typedef RecvWayPoints_<ContainerAllocator> Type;

  RecvWayPoints_()
  : waypointnumA(0)
  , Apx()
  , Apy()
  , waypointnumB(0)
  , Bpx()
  , Bpy()
  {
  }

  RecvWayPoints_(const ContainerAllocator& _alloc)
  : waypointnumA(0)
  , Apx(_alloc)
  , Apy(_alloc)
  , waypointnumB(0)
  , Bpx(_alloc)
  , Bpy(_alloc)
  {
  }

  typedef int32_t _waypointnumA_type;
  int32_t waypointnumA;

  typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _Apx_type;
  std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  Apx;

  typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _Apy_type;
  std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  Apy;

  typedef int32_t _waypointnumB_type;
  int32_t waypointnumB;

  typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _Bpx_type;
  std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  Bpx;

  typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _Bpy_type;
  std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  Bpy;


  typedef boost::shared_ptr< ::autonavigation::RecvWayPoints_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::autonavigation::RecvWayPoints_<ContainerAllocator>  const> ConstPtr;
}; // struct RecvWayPoints
typedef  ::autonavigation::RecvWayPoints_<std::allocator<void> > RecvWayPoints;

typedef boost::shared_ptr< ::autonavigation::RecvWayPoints> RecvWayPointsPtr;
typedef boost::shared_ptr< ::autonavigation::RecvWayPoints const> RecvWayPointsConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::autonavigation::RecvWayPoints_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::autonavigation::RecvWayPoints_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace autonavigation

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::autonavigation::RecvWayPoints_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::autonavigation::RecvWayPoints_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::autonavigation::RecvWayPoints_<ContainerAllocator> > {
  static const char* value() 
  {
    return "cfc84bf91694d7cb048a755fe64d02fa";
  }

  static const char* value(const  ::autonavigation::RecvWayPoints_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xcfc84bf91694d7cbULL;
  static const uint64_t static_value2 = 0x048a755fe64d02faULL;
};

template<class ContainerAllocator>
struct DataType< ::autonavigation::RecvWayPoints_<ContainerAllocator> > {
  static const char* value() 
  {
    return "autonavigation/RecvWayPoints";
  }

  static const char* value(const  ::autonavigation::RecvWayPoints_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::autonavigation::RecvWayPoints_<ContainerAllocator> > {
  static const char* value() 
  {
    return "#对应结构体Autonavigation_RecvWayPoints\n\
\n\
int32       waypointnumA         #路点个数\n\
int32[]     Apx                  #路点X坐标，单位cm\n\
int32[]     Apy                  #路点Y坐标，单位cm\n\
int32       waypointnumB         #路点个数\n\
int32[]     Bpx                  #路点X坐标，单位cm\n\
int32[]     Bpy                  #路点Y坐标，单位cm\n\
\n\
";
  }

  static const char* value(const  ::autonavigation::RecvWayPoints_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::autonavigation::RecvWayPoints_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.waypointnumA);
    stream.next(m.Apx);
    stream.next(m.Apy);
    stream.next(m.waypointnumB);
    stream.next(m.Bpx);
    stream.next(m.Bpy);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct RecvWayPoints_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::autonavigation::RecvWayPoints_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::autonavigation::RecvWayPoints_<ContainerAllocator> & v) 
  {
    s << indent << "waypointnumA: ";
    Printer<int32_t>::stream(s, indent + "  ", v.waypointnumA);
    s << indent << "Apx[]" << std::endl;
    for (size_t i = 0; i < v.Apx.size(); ++i)
    {
      s << indent << "  Apx[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.Apx[i]);
    }
    s << indent << "Apy[]" << std::endl;
    for (size_t i = 0; i < v.Apy.size(); ++i)
    {
      s << indent << "  Apy[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.Apy[i]);
    }
    s << indent << "waypointnumB: ";
    Printer<int32_t>::stream(s, indent + "  ", v.waypointnumB);
    s << indent << "Bpx[]" << std::endl;
    for (size_t i = 0; i < v.Bpx.size(); ++i)
    {
      s << indent << "  Bpx[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.Bpx[i]);
    }
    s << indent << "Bpy[]" << std::endl;
    for (size_t i = 0; i < v.Bpy.size(); ++i)
    {
      s << indent << "  Bpy[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.Bpy[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // AUTONAVIGATION_MESSAGE_RECVWAYPOINTS_H

