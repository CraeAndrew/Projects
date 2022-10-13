import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    joy_node = Node(
        package="projects",
        executable="joy",
        #parameters=[{"steering_offset": 0.0}],
    )
    ld.add_action(joy_node)
    return ld
