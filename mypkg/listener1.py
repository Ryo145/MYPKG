# SPDX-FileCopyrightText; 2023 Ryosuke Suzuki ryo135791113@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener():
    def __init__(self, node):
        self.sub = node.create_subscription(Int16, "countup", self.cb, 10)

    def cb(self, msg):
        node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("listener")
listener = Listener(node)
rclpy.spin(node)

