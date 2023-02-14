from launch import LaunchDescription
from launch_ros.actions import Node

def denerate_launch_description():
    return LaunchDescription(
        Node(package='my_package',
        executable='tm2',
        name='move_turtle',
        )
    )