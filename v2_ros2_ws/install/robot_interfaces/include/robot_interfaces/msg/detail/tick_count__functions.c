// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robot_interfaces:msg/TickCount.idl
// generated code does not contain a copyright notice
#include "robot_interfaces/msg/detail/tick_count__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
robot_interfaces__msg__TickCount__init(robot_interfaces__msg__TickCount * msg)
{
  if (!msg) {
    return false;
  }
  // left_wheel_tick_count
  // right_wheel_tick_count
  return true;
}

void
robot_interfaces__msg__TickCount__fini(robot_interfaces__msg__TickCount * msg)
{
  if (!msg) {
    return;
  }
  // left_wheel_tick_count
  // right_wheel_tick_count
}

bool
robot_interfaces__msg__TickCount__are_equal(const robot_interfaces__msg__TickCount * lhs, const robot_interfaces__msg__TickCount * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // left_wheel_tick_count
  if (lhs->left_wheel_tick_count != rhs->left_wheel_tick_count) {
    return false;
  }
  // right_wheel_tick_count
  if (lhs->right_wheel_tick_count != rhs->right_wheel_tick_count) {
    return false;
  }
  return true;
}

bool
robot_interfaces__msg__TickCount__copy(
  const robot_interfaces__msg__TickCount * input,
  robot_interfaces__msg__TickCount * output)
{
  if (!input || !output) {
    return false;
  }
  // left_wheel_tick_count
  output->left_wheel_tick_count = input->left_wheel_tick_count;
  // right_wheel_tick_count
  output->right_wheel_tick_count = input->right_wheel_tick_count;
  return true;
}

robot_interfaces__msg__TickCount *
robot_interfaces__msg__TickCount__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_interfaces__msg__TickCount * msg = (robot_interfaces__msg__TickCount *)allocator.allocate(sizeof(robot_interfaces__msg__TickCount), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robot_interfaces__msg__TickCount));
  bool success = robot_interfaces__msg__TickCount__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robot_interfaces__msg__TickCount__destroy(robot_interfaces__msg__TickCount * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robot_interfaces__msg__TickCount__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robot_interfaces__msg__TickCount__Sequence__init(robot_interfaces__msg__TickCount__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_interfaces__msg__TickCount * data = NULL;

  if (size) {
    data = (robot_interfaces__msg__TickCount *)allocator.zero_allocate(size, sizeof(robot_interfaces__msg__TickCount), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robot_interfaces__msg__TickCount__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robot_interfaces__msg__TickCount__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
robot_interfaces__msg__TickCount__Sequence__fini(robot_interfaces__msg__TickCount__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      robot_interfaces__msg__TickCount__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

robot_interfaces__msg__TickCount__Sequence *
robot_interfaces__msg__TickCount__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_interfaces__msg__TickCount__Sequence * array = (robot_interfaces__msg__TickCount__Sequence *)allocator.allocate(sizeof(robot_interfaces__msg__TickCount__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robot_interfaces__msg__TickCount__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robot_interfaces__msg__TickCount__Sequence__destroy(robot_interfaces__msg__TickCount__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robot_interfaces__msg__TickCount__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robot_interfaces__msg__TickCount__Sequence__are_equal(const robot_interfaces__msg__TickCount__Sequence * lhs, const robot_interfaces__msg__TickCount__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robot_interfaces__msg__TickCount__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robot_interfaces__msg__TickCount__Sequence__copy(
  const robot_interfaces__msg__TickCount__Sequence * input,
  robot_interfaces__msg__TickCount__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(robot_interfaces__msg__TickCount);
    robot_interfaces__msg__TickCount * data =
      (robot_interfaces__msg__TickCount *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robot_interfaces__msg__TickCount__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          robot_interfaces__msg__TickCount__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robot_interfaces__msg__TickCount__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
