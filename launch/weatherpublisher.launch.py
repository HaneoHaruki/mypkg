import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    weatherpublish = launch_ros.actions.Node(
        package='mypkg',
        executable='weatherpublisher',
    )

    listen = launch_ros.actions.Node(
        package = 'mypkg',
        executable = 'listener',
        output = 'screen',
    )


    return launch.LaunchDescription([weatherpublish,listen])                      
