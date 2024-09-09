import os

from ament_index_python.packages import get_package_share_directory
from ament_index_python.packages import get_package_prefix

from launch import LaunchDescription
from launch.substitutions import EnvironmentVariable

from launch_ros.actions import Node

def generate_launch_description():
    
    # Position controller
    pos_cont_spawner = Node(
        package="controller_manager",
        prefix=[
            "sudo -E env PATH=",
            EnvironmentVariable("PATH", default_value="${PATH}"),
            " LD_LIBRARY_PATH=",
            EnvironmentVariable("LD_LIBRARY_PATH", default_value="${LD_LIBRARY_PATH}"),
            " PYTHONPATH=",
            EnvironmentVariable("PYTHONPATH", default_value="${PYTHONPATH}"),
            " HOME=/tmp ",
        ],
        executable="spawner",
        arguments=["forward_position_controller",
                   "--controller-manager",
                   "/controller_manager",
        ],
    )

    # Joint broadcaster
    joint_broad_spawner = Node(
        package="controller_manager",
        prefix=[
            "sudo -E env PATH=",
            EnvironmentVariable("PATH", default_value="${PATH}"),
            " LD_LIBRARY_PATH=",
            EnvironmentVariable("LD_LIBRARY_PATH", default_value="${LD_LIBRARY_PATH}"),
            " PYTHONPATH=",
            EnvironmentVariable("PYTHONPATH", default_value="${PYTHONPATH}"),
            " HOME=/tmp ",
        ],
        executable="spawner",
        arguments=["joint_state_broadcaster",
                   "--controller-manager",
                   "/controller_manager",
        ],
    )

    # Reference signal generator
    ref_signal_generator = Node(
        package="reference_signal_generator",
        executable="reference_signal_generator",
        ros_arguments=["-p", "topic_name:=/forward_position_controller/commands"])

    # Launch them all!
    return LaunchDescription([
        pos_cont_spawner,
        joint_broad_spawner,
        ref_signal_generator
    ])