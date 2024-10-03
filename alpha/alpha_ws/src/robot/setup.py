from setuptools import find_packages, setup

package_name = 'robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='scott',
    maintainer_email='scott@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'encoder_publisher_left = robot.encoder_publisher_left:main',
            'encoder_publisher_right = robot.encoder_publisher_right:main',
            'encoder_publisher = robot.encoder_publisher:main',
            'motor_controller = robot.motor_controller:main',
            'motor_driver = robot.motor_driver:main',
            'pid_controller_left = robot.pid_controller_left:main',
            'pid_controller_right = robot.pid_controller_right:main',
            'imu_publisher = robot.imu_publisher:main',
            'odom_publisher = robot.odom_publisher:main',
            # 'rpm_publisher_left = robot.rpm_publisher_left:main',
            # 'rpm_publisher_right = robot.rpm_publisher_right:main',
        ],
    },
)
