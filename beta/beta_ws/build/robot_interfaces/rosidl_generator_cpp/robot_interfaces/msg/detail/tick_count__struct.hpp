// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_interfaces:msg/TickCount.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__MSG__DETAIL__TICK_COUNT__STRUCT_HPP_
#define ROBOT_INTERFACES__MSG__DETAIL__TICK_COUNT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__robot_interfaces__msg__TickCount __attribute__((deprecated))
#else
# define DEPRECATED__robot_interfaces__msg__TickCount __declspec(deprecated)
#endif

namespace robot_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TickCount_
{
  using Type = TickCount_<ContainerAllocator>;

  explicit TickCount_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->left_wheel_tick_count = 0;
      this->right_wheel_tick_count = 0;
    }
  }

  explicit TickCount_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->left_wheel_tick_count = 0;
      this->right_wheel_tick_count = 0;
    }
  }

  // field types and members
  using _left_wheel_tick_count_type =
    int16_t;
  _left_wheel_tick_count_type left_wheel_tick_count;
  using _right_wheel_tick_count_type =
    int16_t;
  _right_wheel_tick_count_type right_wheel_tick_count;

  // setters for named parameter idiom
  Type & set__left_wheel_tick_count(
    const int16_t & _arg)
  {
    this->left_wheel_tick_count = _arg;
    return *this;
  }
  Type & set__right_wheel_tick_count(
    const int16_t & _arg)
  {
    this->right_wheel_tick_count = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_interfaces::msg::TickCount_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_interfaces::msg::TickCount_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_interfaces::msg::TickCount_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_interfaces::msg::TickCount_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_interfaces::msg::TickCount_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_interfaces::msg::TickCount_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_interfaces::msg::TickCount_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_interfaces::msg::TickCount_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_interfaces::msg::TickCount_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_interfaces::msg::TickCount_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_interfaces__msg__TickCount
    std::shared_ptr<robot_interfaces::msg::TickCount_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_interfaces__msg__TickCount
    std::shared_ptr<robot_interfaces::msg::TickCount_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TickCount_ & other) const
  {
    if (this->left_wheel_tick_count != other.left_wheel_tick_count) {
      return false;
    }
    if (this->right_wheel_tick_count != other.right_wheel_tick_count) {
      return false;
    }
    return true;
  }
  bool operator!=(const TickCount_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TickCount_

// alias to use template instance with default allocator
using TickCount =
  robot_interfaces::msg::TickCount_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__MSG__DETAIL__TICK_COUNT__STRUCT_HPP_
