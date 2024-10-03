// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:msg/WheelRPM.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__WHEEL_RPM__BUILDER_HPP_
#define ROBOT_INTERFACES__MSG__DETAIL__WHEEL_RPM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_interfaces/msg/detail/wheel_rpm__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_interfaces
{

namespace msg
{

namespace builder
{

class Init_WheelRPM_rpm_right
{
public:
  explicit Init_WheelRPM_rpm_right(::robot_interfaces::msg::WheelRPM & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::msg::WheelRPM rpm_right(::robot_interfaces::msg::WheelRPM::_rpm_right_type arg)
  {
    msg_.rpm_right = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::msg::WheelRPM msg_;
};

class Init_WheelRPM_rpm_left
{
public:
  Init_WheelRPM_rpm_left()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WheelRPM_rpm_right rpm_left(::robot_interfaces::msg::WheelRPM::_rpm_left_type arg)
  {
    msg_.rpm_left = std::move(arg);
    return Init_WheelRPM_rpm_right(msg_);
  }

private:
  ::robot_interfaces::msg::WheelRPM msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::msg::WheelRPM>()
{
  return robot_interfaces::msg::builder::Init_WheelRPM_rpm_left();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__MSG__DETAIL__WHEEL_RPM__BUILDER_HPP_
