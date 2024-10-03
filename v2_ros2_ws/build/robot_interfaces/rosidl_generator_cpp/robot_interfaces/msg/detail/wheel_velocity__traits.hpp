// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robot_interfaces:msg/WheelVelocity.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__WHEEL_VELOCITY__TRAITS_HPP_
#define ROBOT_INTERFACES__MSG__DETAIL__WHEEL_VELOCITY__TRAITS_HPP_

#include "robot_interfaces/msg/detail/wheel_velocity__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_interfaces::msg::WheelVelocity>()
{
  return "robot_interfaces::msg::WheelVelocity";
}

template<>
inline const char * name<robot_interfaces::msg::WheelVelocity>()
{
  return "robot_interfaces/msg/WheelVelocity";
}

template<>
struct has_fixed_size<robot_interfaces::msg::WheelVelocity>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robot_interfaces::msg::WheelVelocity>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robot_interfaces::msg::WheelVelocity>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBOT_INTERFACES__MSG__DETAIL__WHEEL_VELOCITY__TRAITS_HPP_
