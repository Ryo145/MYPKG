# SPDX-FileCopyrightText; 2023 Ryosuke Suzuki ryo135791113@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class Talker1():
    def __init__(self, node):
        self.pub = node.create_publisher(Float64, "countup", 10)
        self.n = 0.0
        node.create_timer(0.5, self.cb)

    def cb(self):
        msg = Float64()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1.0

def main():
    rclpy.init()
    node = Node("talker1")
    talker1 = Talker1(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
