import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

"""
This is the launch file used to run all of the scripts/nodes
in our boat. Once we flesh things out more, we can implement
further visual development tools. For instance, we can start
an rviz node, use MatPlotLib, an OpenCV canvas, etc.

Note: For every script that you want to run through the launch
script, don't forget to add the shebang line:

#!/usr/bin/env python3

This ensures that the interpreter can run the script.

"""

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='mhsboat').find('mhsboat')
    default_rviz_config_path = os.path.join(pkg_share, 'config/view_boat.rviz')

    # rviz_node = launch_ros.actions.Node(
    #     package='rviz2',
    #     executable='rviz2',
    #     name='rviz2',
    #     output='screen',
    #     arguments=['-d', LaunchConfiguration('rvizconfig')],
    # )

    camera_node = launch_ros.actions.Node(
        package='mhsboat',
        executable='python3',
        name='camera',
        output='screen',
        arguments=[os.path.join(pkg_share, 'mhsboat', 'sensors', 'sensors.py')],
    )

    motor_node = launch_ros.actions.Node(
        package='mhsboat',
        executable='python3',
        name='motors',
        output='screen',
        arguments=[os.path.join(pkg_share, 'mhsboat', 'motors.py')],
    )

    boat_state_node = launch_ros.actions.Node(
        package='mhsboat',
        executable='python3',
        name='boat_state',
        output='screen',
        arguments=[os.path.join(pkg_share, 'mhsboat', 'boat_state.py')],
    )

    return launch.LaunchDescription([
        # launch.actions.DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path)
        # rviz_node,
        camera_node,
        motor_node,
        boat_state_node
    ])