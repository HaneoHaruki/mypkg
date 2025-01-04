import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    weatherpublisher = launch_ros.actions.Node(
        package='mypkg',      #パッケージの名前を指定
        executable='weatherpublisher',  #実行するファイルの指定
        )
    return launch.LaunchDescription([weatherpublisher])                      
