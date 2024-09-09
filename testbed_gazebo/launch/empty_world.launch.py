import os

from ament_index_python.packages import get_package_share_directory
from ament_index_python.packages import get_package_prefix

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

def generate_launch_description():

    # Load the robot description, with "simulation" argument set to true (loads Gazebo hardware interface)
    load_description = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('testbed_description'),'launch','load.launch.py')]),
        launch_arguments={'simulation': 'true'}.items())

    # Set the GAZEBO_MODEL_PATH environment variable to include the models from our own package.
    pkg_install_path = os.path.join(get_package_prefix('testbed_description'), "share")

    if 'GAZEBO_MODEL_PATH' in os.environ:
        model_path = os.environ['GAZEBO_MODEL_PATH'] + os.pathsep + pkg_install_path
    else:
        model_path = pkg_install_path

    # Include the Gazebo launch file, provided by the gazebo_ros package
    # Verbosity level: 1 (errors only)
    # Server only (headless) mode: "-s" argument
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
                    launch_arguments=[('gz_args', ['-r -v 1 empty.sdf -s'])])

    # Run the spawner node from the ros_gz_sim package.
    spawn_entity = Node(package='ros_gz_sim', executable='create',
                        arguments=['-topic', 'robot_description',
                                   '-name', 'testbed',
                                   '-allow_renaming', 'false'],
                        output='screen')

    # Gazebo Real Time Factor (RTF) publisher
    rtf_publisher = Node(package="gz_rtf_publisher",
                         executable="gz_rtf_publisher")

    # Launch them all!
    return LaunchDescription([
        SetEnvironmentVariable('GZ_SIM_RESOURCE_PATH', model_path),
        load_description,
        gazebo,
        spawn_entity,
        rtf_publisher
    ])