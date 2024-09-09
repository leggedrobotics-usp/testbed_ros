import os

from ament_index_python.packages import get_package_share_directory
from ament_index_python.packages import get_package_prefix

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, EnvironmentVariable, FindExecutable, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    # Load the robot description, with "simulation" argument set to false (loads ODRI Master Board hardware interface)
    load_description = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('testbed_description'),'launch','load.launch.py')]),
        launch_arguments={'simulation': 'false'}.items())
    
    # Include the robot description using xacro
    robot_description_content = Command([
        PathJoinSubstitution([FindExecutable(name="xacro")]),
        " ",
        PathJoinSubstitution([FindPackageShare("testbed_description"), "urdf", "testbed.urdf.xacro"]),
    ])
    robot_description = {"robot_description": robot_description_content}

    # Find the controllers configuration file
    robot_controllers = PathJoinSubstitution([
        FindPackageShare("testbed_control"),
        "config",
        "controllers.yaml",
    ])

    # Control node
    # Passing robot_description as a parameter is deprecated, however necessary for the hardware interface to work properly
    control_node = Node(
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
        executable="ros2_control_node",
        parameters=[robot_description, robot_controllers],
        remappings=[("/controller_manager/robot_description", "/robot_description"),],
        output={
            "stdout": "screen",
            "stderr": "screen",
        },
    )

    # Launch them all!
    return LaunchDescription([
        load_description,
        control_node
    ])