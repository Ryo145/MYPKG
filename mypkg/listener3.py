# SPDX-FileCopyrightText; 2023 Ryosuke Suzuki ryo135791113@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random

class Listen3():
    def __init__(self, node):
        self.sub = node.create_subscription(Float64, "countup2", self.cb, 10)
        self.pub = node.create_publisher(Float64, "countup3", 10)
        self.total = 1.0

    def cb(self, msg):
        global node
        if msg.data == 0:
            msg.data = float(random.randint(10, 100))
        self.total *= msg.data
        if self.total >= 999999999999999.999999:
            self.total = 1.0
        node.get_logger().info("Listen3: %f" % self.total)
        self.pub.publish(Float64(data = self.total))

rclpy.init()
node = Node("Listen3")
Listen3 = Listen3(node)
rclpy.spin(node)

