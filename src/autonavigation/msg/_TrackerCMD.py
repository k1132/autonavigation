# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autonavigation/TrackerCMD.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TrackerCMD(genpy.Message):
  _md5sum = "a81e0c287c880465e69aa04676c74a46"
  _type = "autonavigation/TrackerCMD"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 DesiredCurvature
float64 DesiredVelocity
int32 VehicleCommand
float64 YError
float64 HeadingError
int32 ControlMode
int32 SteerEnable
int32 BrakeFuelEnable
"""
  __slots__ = ['DesiredCurvature','DesiredVelocity','VehicleCommand','YError','HeadingError','ControlMode','SteerEnable','BrakeFuelEnable']
  _slot_types = ['float64','float64','int32','float64','float64','int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       DesiredCurvature,DesiredVelocity,VehicleCommand,YError,HeadingError,ControlMode,SteerEnable,BrakeFuelEnable

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TrackerCMD, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.DesiredCurvature is None:
        self.DesiredCurvature = 0.
      if self.DesiredVelocity is None:
        self.DesiredVelocity = 0.
      if self.VehicleCommand is None:
        self.VehicleCommand = 0
      if self.YError is None:
        self.YError = 0.
      if self.HeadingError is None:
        self.HeadingError = 0.
      if self.ControlMode is None:
        self.ControlMode = 0
      if self.SteerEnable is None:
        self.SteerEnable = 0
      if self.BrakeFuelEnable is None:
        self.BrakeFuelEnable = 0
    else:
      self.DesiredCurvature = 0.
      self.DesiredVelocity = 0.
      self.VehicleCommand = 0
      self.YError = 0.
      self.HeadingError = 0.
      self.ControlMode = 0
      self.SteerEnable = 0
      self.BrakeFuelEnable = 0

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
      buff.write(_struct_2di2d3i.pack(_x.DesiredCurvature, _x.DesiredVelocity, _x.VehicleCommand, _x.YError, _x.HeadingError, _x.ControlMode, _x.SteerEnable, _x.BrakeFuelEnable))
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
      end += 48
      (_x.DesiredCurvature, _x.DesiredVelocity, _x.VehicleCommand, _x.YError, _x.HeadingError, _x.ControlMode, _x.SteerEnable, _x.BrakeFuelEnable,) = _struct_2di2d3i.unpack(str[start:end])
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
      buff.write(_struct_2di2d3i.pack(_x.DesiredCurvature, _x.DesiredVelocity, _x.VehicleCommand, _x.YError, _x.HeadingError, _x.ControlMode, _x.SteerEnable, _x.BrakeFuelEnable))
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
      end += 48
      (_x.DesiredCurvature, _x.DesiredVelocity, _x.VehicleCommand, _x.YError, _x.HeadingError, _x.ControlMode, _x.SteerEnable, _x.BrakeFuelEnable,) = _struct_2di2d3i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2di2d3i = struct.Struct("<2di2d3i")