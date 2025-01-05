#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 15 ros2 launch mypkg weatherpublisher.launch.py > /tmp/mypkg.log

##cat /tmp/mypkg.log |
grep '湿度:' /tmp/mypkg.log
