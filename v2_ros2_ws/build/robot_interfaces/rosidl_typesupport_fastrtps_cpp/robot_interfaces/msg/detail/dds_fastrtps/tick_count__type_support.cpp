// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from robot_interfaces:msg/TickCount.idl
// generated code does not contain a copyright notice
#include "robot_interfaces/msg/detail/tick_count__rosidl_typesupport_fastrtps_cpp.hpp"
#include "robot_interfaces/msg/detail/tick_count__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace robot_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_robot_interfaces
cdr_serialize(
  const robot_interfaces::msg::TickCount & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: left_wheel_tick_count
  cdr << ros_message.left_wheel_tick_count;
  // Member: right_wheel_tick_count
  cdr << ros_message.right_wheel_tick_count;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_robot_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  robot_interfaces::msg::TickCount & ros_message)
{
  // Member: left_wheel_tick_count
  cdr >> ros_message.left_wheel_tick_count;

  // Member: right_wheel_tick_count
  cdr >> ros_message.right_wheel_tick_count;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_robot_interfaces
get_serialized_size(
  const robot_interfaces::msg::TickCount & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: left_wheel_tick_count
  {
    size_t item_size = sizeof(ros_message.left_wheel_tick_count);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: right_wheel_tick_count
  {
    size_t item_size = sizeof(ros_message.right_wheel_tick_count);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_robot_interfaces
max_serialized_size_TickCount(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: left_wheel_tick_count
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: right_wheel_tick_count
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  return current_alignment - initial_alignment;
}

static bool _TickCount__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const robot_interfaces::msg::TickCount *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _TickCount__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<robot_interfaces::msg::TickCount *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _TickCount__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const robot_interfaces::msg::TickCount *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _TickCount__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_TickCount(full_bounded, 0);
}

static message_type_support_callbacks_t _TickCount__callbacks = {
  "robot_interfaces::msg",
  "TickCount",
  _TickCount__cdr_serialize,
  _TickCount__cdr_deserialize,
  _TickCount__get_serialized_size,
  _TickCount__max_serialized_size
};

static rosidl_message_type_support_t _TickCount__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_TickCount__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace robot_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_robot_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_interfaces::msg::TickCount>()
{
  return &robot_interfaces::msg::typesupport_fastrtps_cpp::_TickCount__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_interfaces, msg, TickCount)() {
  return &robot_interfaces::msg::typesupport_fastrtps_cpp::_TickCount__handle;
}

#ifdef __cplusplus
}
#endif
