// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_interfaces:msg/TickCount.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__TICK_COUNT__STRUCT_H_
#define ROBOT_INTERFACES__MSG__DETAIL__TICK_COUNT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/TickCount in the package robot_interfaces.
typedef struct robot_interfaces__msg__TickCount
{
  int16_t left_wheel_tick_count;
  int16_t right_wheel_tick_count;
  int16_t tower_tick_count;
} robot_interfaces__msg__TickCount;

// Struct for a sequence of robot_interfaces__msg__TickCount.
typedef struct robot_interfaces__msg__TickCount__Sequence
{
  robot_interfaces__msg__TickCount * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interfaces__msg__TickCount__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_INTERFACES__MSG__DETAIL__TICK_COUNT__STRUCT_H_
