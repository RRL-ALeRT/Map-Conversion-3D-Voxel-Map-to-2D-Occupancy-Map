from launch import LaunchDescription
from launch_ros.actions import Node
import math

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mapconversion',
            executable='map_conversion_oct_node',
            name='map_conversion',
            output='screen',
            parameters=[{
                'map_frame': 'map',
                'minimum_z': 0.35,
                'max_slope_ugv': math.radians(10.0),
                'slope_estimation_size': 1,  
                'minimum_occupancy': 100,
                'map_position_z': 0.0,
                'partial_map_updates': True,
                # QoS parameters
                'subscriber_qos_reliable': True,
                'subscriber_qos_transient_local': False,
                'publisher_qos_reliable': True,
                'publisher_qos_transient_local': False,
            }],
            remappings=[
                ('octomap', 'octomap_full')
            ]
        ),
        # Uncomment if using offline map
        # Node(
        #     package='octomap_server',
        #     executable='octomap_server_node',
        #     name='octomap_server',
        #     output='screen',
        #     parameters=[{
        #         'octomap_path': '/path/to/octomap.bt'
        #     }]
        # )
    ])
