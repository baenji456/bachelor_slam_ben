# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from sbg_driver/SbgEkfQuat.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import sbg_driver.msg
import std_msgs.msg

class SbgEkfQuat(genpy.Message):
  _md5sum = "f1257400ac859ad475d8b651b008ba22"
  _type = "sbg_driver/SbgEkfQuat"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# SBG Ellipse Messages

Header header

# Time since sensor is powered up [us]
uint32 time_stamp

# Quaternion parameter (ROS order X, Y, Z, W)
# The rotation definition depends on the driver NED/ENU configuration
# Please read the message SbgEkfEuler for more information
geometry_msgs/Quaternion quaternion

# Angle accuracy (Roll, Pitch, Yaw (heading)) (1 sigma) [rad]
geometry_msgs/Vector3 accuracy

#  Global solution status
SbgEkfStatus status

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
string frame_id

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: sbg_driver/SbgEkfStatus
# SBG Ellipse Messages
# Submessage

# Defines the Kalman filter computation mode (see the table 4 below)
# 0 UNINITIALIZED	The Kalman filter is not initialized and the returned data are all invalid.
# 1 VERTICAL_GYRO	The Kalman filter only rely on a vertical reference to compute roll and pitch angles. Heading and navigation data drift freely.
# 2 AHRS			A heading reference is available, the Kalman filter provides full orientation but navigation data drift freely.
# 3 NAV_VELOCITY	The Kalman filter computes orientation and velocity. Position is freely integrated from velocity estimation.
# 4 NAV_POSITION	Nominal mode, the Kalman filter computes all parameters (attitude, velocity, position). Absolute position is provided. 
uint8 solution_mode 

# True if Attitude data is reliable (Roll/Pitch error < 0,5 deg)
bool attitude_valid

# True if Heading data is reliable (Heading error < 1 deg)
bool heading_valid

# True if Velocity data is reliable (velocity error < 1.5 m/s)
bool velocity_valid

# True if Position data is reliable (Position error < 10m)
bool position_valid

# True if vertical reference is used in solution (data used and valid since 3s)
bool vert_ref_used

# True if magnetometer is used in solution (data used and valid since 3s)
bool mag_ref_used

# True if GPS velocity is used in solution (data used and valid since 3s)
bool gps1_vel_used

# True if GPS Position is used in solution (data used and valid since 3s)
bool gps1_pos_used

# True if GPS Course is used in solution (data used and valid since 3s)
bool gps1_course_used

# True if GPS True Heading is used in solution (data used and valid since 3s)
bool gps1_hdt_used

# True if GPS2 velocity is used in solution (data used and valid since 3s)
bool gps2_vel_used

# True if GPS2 Position is used in solution (data used and valid since 3s)
bool gps2_pos_used

# True if GPS2 Course is used in solution (data used and valid since 3s)
bool gps2_course_used

# True if GPS2 True Heading is used in solution (data used and valid since 3s)
bool gps2_hdt_used

# True if Odometer is used in solution (data used and valid since 3s)
bool odo_used
"""
  __slots__ = ['header','time_stamp','quaternion','accuracy','status']
  _slot_types = ['std_msgs/Header','uint32','geometry_msgs/Quaternion','geometry_msgs/Vector3','sbg_driver/SbgEkfStatus']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,time_stamp,quaternion,accuracy,status

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SbgEkfQuat, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.time_stamp is None:
        self.time_stamp = 0
      if self.quaternion is None:
        self.quaternion = geometry_msgs.msg.Quaternion()
      if self.accuracy is None:
        self.accuracy = geometry_msgs.msg.Vector3()
      if self.status is None:
        self.status = sbg_driver.msg.SbgEkfStatus()
    else:
      self.header = std_msgs.msg.Header()
      self.time_stamp = 0
      self.quaternion = geometry_msgs.msg.Quaternion()
      self.accuracy = geometry_msgs.msg.Vector3()
      self.status = sbg_driver.msg.SbgEkfStatus()

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_I7d16B().pack(_x.time_stamp, _x.quaternion.x, _x.quaternion.y, _x.quaternion.z, _x.quaternion.w, _x.accuracy.x, _x.accuracy.y, _x.accuracy.z, _x.status.solution_mode, _x.status.attitude_valid, _x.status.heading_valid, _x.status.velocity_valid, _x.status.position_valid, _x.status.vert_ref_used, _x.status.mag_ref_used, _x.status.gps1_vel_used, _x.status.gps1_pos_used, _x.status.gps1_course_used, _x.status.gps1_hdt_used, _x.status.gps2_vel_used, _x.status.gps2_pos_used, _x.status.gps2_course_used, _x.status.gps2_hdt_used, _x.status.odo_used))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.quaternion is None:
        self.quaternion = geometry_msgs.msg.Quaternion()
      if self.accuracy is None:
        self.accuracy = geometry_msgs.msg.Vector3()
      if self.status is None:
        self.status = sbg_driver.msg.SbgEkfStatus()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 76
      (_x.time_stamp, _x.quaternion.x, _x.quaternion.y, _x.quaternion.z, _x.quaternion.w, _x.accuracy.x, _x.accuracy.y, _x.accuracy.z, _x.status.solution_mode, _x.status.attitude_valid, _x.status.heading_valid, _x.status.velocity_valid, _x.status.position_valid, _x.status.vert_ref_used, _x.status.mag_ref_used, _x.status.gps1_vel_used, _x.status.gps1_pos_used, _x.status.gps1_course_used, _x.status.gps1_hdt_used, _x.status.gps2_vel_used, _x.status.gps2_pos_used, _x.status.gps2_course_used, _x.status.gps2_hdt_used, _x.status.odo_used,) = _get_struct_I7d16B().unpack(str[start:end])
      self.status.attitude_valid = bool(self.status.attitude_valid)
      self.status.heading_valid = bool(self.status.heading_valid)
      self.status.velocity_valid = bool(self.status.velocity_valid)
      self.status.position_valid = bool(self.status.position_valid)
      self.status.vert_ref_used = bool(self.status.vert_ref_used)
      self.status.mag_ref_used = bool(self.status.mag_ref_used)
      self.status.gps1_vel_used = bool(self.status.gps1_vel_used)
      self.status.gps1_pos_used = bool(self.status.gps1_pos_used)
      self.status.gps1_course_used = bool(self.status.gps1_course_used)
      self.status.gps1_hdt_used = bool(self.status.gps1_hdt_used)
      self.status.gps2_vel_used = bool(self.status.gps2_vel_used)
      self.status.gps2_pos_used = bool(self.status.gps2_pos_used)
      self.status.gps2_course_used = bool(self.status.gps2_course_used)
      self.status.gps2_hdt_used = bool(self.status.gps2_hdt_used)
      self.status.odo_used = bool(self.status.odo_used)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_I7d16B().pack(_x.time_stamp, _x.quaternion.x, _x.quaternion.y, _x.quaternion.z, _x.quaternion.w, _x.accuracy.x, _x.accuracy.y, _x.accuracy.z, _x.status.solution_mode, _x.status.attitude_valid, _x.status.heading_valid, _x.status.velocity_valid, _x.status.position_valid, _x.status.vert_ref_used, _x.status.mag_ref_used, _x.status.gps1_vel_used, _x.status.gps1_pos_used, _x.status.gps1_course_used, _x.status.gps1_hdt_used, _x.status.gps2_vel_used, _x.status.gps2_pos_used, _x.status.gps2_course_used, _x.status.gps2_hdt_used, _x.status.odo_used))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.quaternion is None:
        self.quaternion = geometry_msgs.msg.Quaternion()
      if self.accuracy is None:
        self.accuracy = geometry_msgs.msg.Vector3()
      if self.status is None:
        self.status = sbg_driver.msg.SbgEkfStatus()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 76
      (_x.time_stamp, _x.quaternion.x, _x.quaternion.y, _x.quaternion.z, _x.quaternion.w, _x.accuracy.x, _x.accuracy.y, _x.accuracy.z, _x.status.solution_mode, _x.status.attitude_valid, _x.status.heading_valid, _x.status.velocity_valid, _x.status.position_valid, _x.status.vert_ref_used, _x.status.mag_ref_used, _x.status.gps1_vel_used, _x.status.gps1_pos_used, _x.status.gps1_course_used, _x.status.gps1_hdt_used, _x.status.gps2_vel_used, _x.status.gps2_pos_used, _x.status.gps2_course_used, _x.status.gps2_hdt_used, _x.status.odo_used,) = _get_struct_I7d16B().unpack(str[start:end])
      self.status.attitude_valid = bool(self.status.attitude_valid)
      self.status.heading_valid = bool(self.status.heading_valid)
      self.status.velocity_valid = bool(self.status.velocity_valid)
      self.status.position_valid = bool(self.status.position_valid)
      self.status.vert_ref_used = bool(self.status.vert_ref_used)
      self.status.mag_ref_used = bool(self.status.mag_ref_used)
      self.status.gps1_vel_used = bool(self.status.gps1_vel_used)
      self.status.gps1_pos_used = bool(self.status.gps1_pos_used)
      self.status.gps1_course_used = bool(self.status.gps1_course_used)
      self.status.gps1_hdt_used = bool(self.status.gps1_hdt_used)
      self.status.gps2_vel_used = bool(self.status.gps2_vel_used)
      self.status.gps2_pos_used = bool(self.status.gps2_pos_used)
      self.status.gps2_course_used = bool(self.status.gps2_course_used)
      self.status.gps2_hdt_used = bool(self.status.gps2_hdt_used)
      self.status.odo_used = bool(self.status.odo_used)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_I7d16B = None
def _get_struct_I7d16B():
    global _struct_I7d16B
    if _struct_I7d16B is None:
        _struct_I7d16B = struct.Struct("<I7d16B")
    return _struct_I7d16B
