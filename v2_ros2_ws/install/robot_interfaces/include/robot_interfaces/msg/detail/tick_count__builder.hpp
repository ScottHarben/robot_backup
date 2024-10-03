// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:msg/TickCount.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__TICK_COUNT__BUILDER_HPP_
#define ROBOT_INTERFACES__MSG__DETAIL__TICK_COUNT__BUILDER_HPP_

#include "robot_interfaces/msg/detail/tick_count__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace robot_interfaces
{

namespace msg
{

namespace builder
{

class Init_TickCount_tower_tick_count
{
public:
  explicit Init_TickCount_tower_tick_count(::robot_interfaces::msg::TickCount & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::msg::TickCount tower_tick_count(::robot_interfaces::msg::TickCount::_tower_tick_count_type arg)
  {
    msg_.tower_tick_count = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::msg::TickCount msg_;
};

class Init_TickCount_right_wheel_tick_count
{
public:
  explicit Init_TickCount_right_wheel_tick_count(::robot_interfaces::msg::TickCount & msg)
  : msg_(msg)
  {}
  Init_TickCount_tower_tick_count right_wheel_tick_count(::robot_interfaces::msg::TickCount::_right_wheel_tick_count_type arg)
  {
    msg_.right_wheel_tick_count = std::move(arg);
    return Init_TickCount_tower_tick_count(msg_);
  }

private:
  ::robot_interfaces::msg::TickCount msg_;
};

class Init_TickCount_left_wheel_tick_count
{
public:
  Init_TickCount_left_wheel_tick_count()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TickCount_right_wheel_tick_count left_wheel_tick_count(::robot_interfaces::msg::TickCount::_left_wheel_tick_count_type arg)
  {
    msg_.left_wheel_tick_count = std::move(arg);
    return Init_TickCount_right_wheel_tick_count(msg_);
  }

private:
  ::robot_interfaces::msg::TickCount msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::msg::TickCount>()
{
  return robot_interfaces::msg::builder::Init_TickCount_left_wheel_tick_count();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__MSG__DETAIL__TICK_COUNT__BUILDER_HPP_
