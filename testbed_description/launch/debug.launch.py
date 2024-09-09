import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    # Load the robot description
    load_description = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('testbed_description'),'launch','load.launch.py')]))
    
    # Add the joint state publisher GUI for simple testing
    jsp_gui = Node(package='joint_state_publisher_gui',
                   executable='joint_state_publisher_gui')

    # Launch!
    return LaunchDescription([
        load_description,
        jsp_gui
    ])