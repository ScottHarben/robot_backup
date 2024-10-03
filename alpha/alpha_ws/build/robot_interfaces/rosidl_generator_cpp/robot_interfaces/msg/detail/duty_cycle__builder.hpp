// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:msg/DutyCycle.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__DUTY_CYCLE__BUILDER_HPP_
#define ROBOT_INTERFACES__MSG__DETAIL__DUTY_CYCLE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_interfaces/msg/detail/duty_cycle__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_interfaces
{

namespace msg
{

namespace builder
{

class Init_DutyCycle_duty_cycle_right
{
public:
  explicit Init_DutyCycle_duty_cycle_right(::robot_interfaces::msg::DutyCycle & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::msg::DutyCycle duty_cycle_right(::robot_interfaces::msg::DutyCycle::_duty_cycle_right_type arg)
  {
    msg_.duty_cycle_right = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::msg::DutyCycle msg_;
};

class Init_DutyCycle_duty_cycle_left
{
public:
  Init_DutyCycle_duty_cycle_left()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DutyCycle_duty_cycle_right duty_cycle_left(::robot_interfaces::msg::DutyCycle::_duty_cycle_left_type arg)
  {
    msg_.duty_cycle_left = std::move(arg);
    return Init_DutyCycle_duty_cycle_right(msg_);
  }

private:
  ::robot_interfaces::msg::DutyCycle msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::msg::DutyCycle>()
{
  return robot_interfaces::msg::builder::Init_DutyCycle_duty_cycle_left();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__MSG__DETAIL__DUTY_CYCLE__BUILDER_HPP_
