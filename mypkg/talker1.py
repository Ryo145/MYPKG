# SPDX-FileCopyrightText; 2023 Ryosuke Suzuki ryo135791113@gmail.com
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self, node):
        self.pub_up = node.create_publisher(Int16, "countup", 10)
        self.pub_down = node.create_publisher(Int16, "countdown", 10)
        self.n_up = 0
        self.n_down = 100
        node.create_timer(0.5, self.cb)

    def cb(self):
        msg_up = Int16()
        msg_up.data = self.n_up
        self.pub_up.publish(msg_up)
        self.n_up += 1

        msg_down = Int16()
        msg_down.data = self.n_down
        self.pub_down.publish(msg_down)
        self.n_down -= 1

rclpy.init()
node = Node("talker")
talker = Talker(node)
rclpy.spin(node)

