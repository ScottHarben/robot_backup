// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_interfaces:msg/WheelVelocity.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__WHEEL_VELOCITY__STRUCT_H_
#define ROBOT_INTERFACES__MSG__DETAIL__WHEEL_VELOCITY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/WheelVelocity in the package robot_interfaces.
typedef struct robot_interfaces__msg__WheelVelocity
{
  double linear_velocity_left;
  double linear_velocity_right;
} robot_interfaces__msg__WheelVelocity;

// Struct for a sequence of robot_interfaces__msg__WheelVelocity.
typedef struct robot_interfaces__msg__WheelVelocity__Sequence
{
  robot_interfaces__msg__WheelVelocity * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interfaces__msg__WheelVelocity__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_INTERFACES__MSG__DETAIL__WHEEL_VELOCITY__STRUCT_H_
