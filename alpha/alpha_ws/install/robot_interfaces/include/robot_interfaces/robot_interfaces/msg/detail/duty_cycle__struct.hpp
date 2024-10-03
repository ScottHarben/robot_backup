// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_interfaces:msg/DutyCycle.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__DUTY_CYCLE__STRUCT_HPP_
#define ROBOT_INTERFACES__MSG__DETAIL__DUTY_CYCLE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__robot_interfaces__msg__DutyCycle __attribute__((deprecated))
#else
# define DEPRECATED__robot_interfaces__msg__DutyCycle __declspec(deprecated)
#endif

namespace robot_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct DutyCycle_
{
  using Type = DutyCycle_<ContainerAllocator>;

  explicit DutyCycle_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->duty_cycle_left = 0.0;
      this->duty_cycle_right = 0.0;
    }
  }

  explicit DutyCycle_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->duty_cycle_left = 0.0;
      this->duty_cycle_right = 0.0;
    }
  }

  // field types and members
  using _duty_cycle_left_type =
    double;
  _duty_cycle_left_type duty_cycle_left;
  using _duty_cycle_right_type =
    double;
  _duty_cycle_right_type duty_cycle_right;

  // setters for named parameter idiom
  Type & set__duty_cycle_left(
    const double & _arg)
  {
    this->duty_cycle_left = _arg;
    return *this;
  }
  Type & set__duty_cycle_right(
    const double & _arg)
  {
    this->duty_cycle_right = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_interfaces::msg::DutyCycle_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_interfaces::msg::DutyCycle_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_interfaces::msg::DutyCycle_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_interfaces::msg::DutyCycle_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_interfaces::msg::DutyCycle_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_interfaces::msg::DutyCycle_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_interfaces::msg::DutyCycle_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_interfaces::msg::DutyCycle_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_interfaces::msg::DutyCycle_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_interfaces::msg::DutyCycle_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_interfaces__msg__DutyCycle
    std::shared_ptr<robot_interfaces::msg::DutyCycle_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_interfaces__msg__DutyCycle
    std::shared_ptr<robot_interfaces::msg::DutyCycle_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DutyCycle_ & other) const
  {
    if (this->duty_cycle_left != other.duty_cycle_left) {
      return false;
    }
    if (this->duty_cycle_right != other.duty_cycle_right) {
      return false;
    }
    return true;
  }
  bool operator!=(const DutyCycle_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DutyCycle_

// alias to use template instance with default allocator
using DutyCycle =
  robot_interfaces::msg::DutyCycle_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__MSG__DETAIL__DUTY_CYCLE__STRUCT_HPP_
