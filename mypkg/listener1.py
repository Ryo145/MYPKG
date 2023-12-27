# SPDX-FileCopyrightText: 2023 Ryosuke Suzuki ryo135791113@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class Listen1():
    def __init__(self, node):
        self.sub = node.create_subscription(Float64, "countup", self.cb, 10)
        self.pub = node.create_publisher(Float64, "addition", 10)
        self.total = 0.0

    def cb(self, msg):
        global node
        self.total += msg.data
        node.get_logger().info("Listen1: %f" % self.total)
        self.pub.publish(Float64(data = self.total))

rclpy.init()
node = Node("Listen1")
Listen1 = Listen1(node)
rclpy.spin(node)

