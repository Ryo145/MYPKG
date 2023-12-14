# SPDX-FileCopyrightText; 2023 Ryosuke Suzuki ryo135791113@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker1 = launch_ros.actions.Node(
            package='mypkg',
            executable='talker1',
            )
    listener1 = launch_ros.actions.Node(
            package='mypkg',
            executable='listener1',
            output='screen'
            )

    return launch.LaunchDescription([talker1, listener1])
