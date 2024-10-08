// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from robot_interfaces:msg/TickCount.idl
// generated code does not contain a copyright notice
#include "robot_interfaces/msg/detail/tick_count__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "robot_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "robot_interfaces/msg/detail/tick_count__struct.h"
#include "robot_interfaces/msg/detail/tick_count__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _TickCount__ros_msg_type = robot_interfaces__msg__TickCount;

static bool _TickCount__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TickCount__ros_msg_type * ros_message = static_cast<const _TickCount__ros_msg_type *>(untyped_ros_message);
  // Field name: left_wheel_tick_count
  {
    cdr << ros_message->left_wheel_tick_count;
  }

  // Field name: right_wheel_tick_count
  {
    cdr << ros_message->right_wheel_tick_count;
  }

  return true;
}

static bool _TickCount__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TickCount__ros_msg_type * ros_message = static_cast<_TickCount__ros_msg_type *>(untyped_ros_message);
  // Field name: left_wheel_tick_count
  {
    cdr >> ros_message->left_wheel_tick_count;
  }

  // Field name: right_wheel_tick_count
  {
    cdr >> ros_message->right_wheel_tick_count;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robot_interfaces
size_t get_serialized_size_robot_interfaces__msg__TickCount(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TickCount__ros_msg_type * ros_message = static_cast<const _TickCount__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name left_wheel_tick_count
  {
    size_t item_size = sizeof(ros_message->left_wheel_tick_count);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name right_wheel_tick_count
  {
    size_t item_size = sizeof(ros_message->right_wheel_tick_count);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _TickCount__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_robot_interfaces__msg__TickCount(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robot_interfaces
size_t max_serialized_size_robot_interfaces__msg__TickCount(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: left_wheel_tick_count
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: right_wheel_tick_count
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _TickCount__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_robot_interfaces__msg__TickCount(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_TickCount = {
  "robot_interfaces::msg",
  "TickCount",
  _TickCount__cdr_serialize,
  _TickCount__cdr_deserialize,
  _TickCount__get_serialized_size,
  _TickCount__max_serialized_size
};

static rosidl_message_type_support_t _TickCount__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TickCount,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, robot_interfaces, msg, TickCount)() {
  return &_TickCount__type_support;
}

#if defined(__cplusplus)
}
#endif
