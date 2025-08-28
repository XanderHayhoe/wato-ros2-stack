from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='cpp_wkspc', executable='talker', name='talker'),
        Node(package='cpp_wkspc', executable='listener', name='listener'),
    ])