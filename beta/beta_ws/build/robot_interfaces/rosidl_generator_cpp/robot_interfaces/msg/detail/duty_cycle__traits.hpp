// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robot_interfaces:msg/DutyCycle.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__DUTY_CYCLE__TRAITS_HPP_
#define ROBOT_INTERFACES__MSG__DETAIL__DUTY_CYCLE__TRAITS_HPP_

#include "robot_interfaces/msg/detail/duty_cycle__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_interfaces::msg::DutyCycle>()
{
  return "robot_interfaces::msg::DutyCycle";
}

template<>
inline const char * name<robot_interfaces::msg::DutyCycle>()
{
  return "robot_interfaces/msg/DutyCycle";
}

template<>
struct has_fixed_size<robot_interfaces::msg::DutyCycle>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robot_interfaces::msg::DutyCycle>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robot_interfaces::msg::DutyCycle>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBOT_INTERFACES__MSG__DETAIL__DUTY_CYCLE__TRAITS_HPP_
