#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg t1_l1_l2_l3_l4.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Listen1: 0.000000'
