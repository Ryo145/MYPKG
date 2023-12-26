#!/bin/bash
# SPDX-FileCopyrightText: 2023 Ryosuke Suzuki ryo135791113@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 5 ros2 launch mypkg t1_l1_l2_l3_l4.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep -e 'Listen1: 0.000000' -e 'Listen2: 0.000000' -e 'Listen4: 100000.000000' 
