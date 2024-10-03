// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:msg/WheelVelocity.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__WHEEL_VELOCITY__BUILDER_HPP_
#define ROBOT_INTERFACES__MSG__DETAIL__WHEEL_VELOCITY__BUILDER_HPP_

#include "robot_interfaces/msg/detail/wheel_velocity__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace robot_interfaces
{

namespace msg
{

namespace builder
{

class Init_WheelVelocity_linear_velocity_right
{
public:
  explicit Init_WheelVelocity_linear_velocity_right(::robot_interfaces::msg::WheelVelocity & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::msg::WheelVelocity linear_velocity_right(::robot_interfaces::msg::WheelVelocity::_linear_velocity_right_type arg)
  {
    msg_.linear_velocity_right = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::msg::WheelVelocity msg_;
};

class Init_WheelVelocity_linear_velocity_left
{
public:
  Init_WheelVelocity_linear_velocity_left()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WheelVelocity_linear_velocity_right linear_velocity_left(::robot_interfaces::msg::WheelVelocity::_linear_velocity_left_type arg)
  {
    msg_.linear_velocity_left = std::move(arg);
    return Init_WheelVelocity_linear_velocity_right(msg_);
  }

private:
  ::robot_interfaces::msg::WheelVelocity msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::msg::WheelVelocity>()
{
  return robot_interfaces::msg::builder::Init_WheelVelocity_linear_velocity_left();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__MSG__DETAIL__WHEEL_VELOCITY__BUILDER_HPP_
