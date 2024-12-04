#!/usr/bin/env python3

# TODO: Use the GPIO output of the Jetson to output PWM signals

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped

"""
This part of the code create a node that publishes to a topic
The topic is named 'velocity set'
It publishes the TwistStamped to the topic
TwistStamped is the boat's forward, backward, and angular velocity all timestamped
"""
class Motors(Node):
    def __init__(self):
        super().__init__("motor_controller")
        self.cmd_vel_publisher = self.create_publisher(TwistStamped, 'velocityset', 10)
        self.cmd_vel = TwistStamped()

"""
Methods are defined to change the boats velocity
When the method is called, it will set the boat to the new velocity
"""
    def set_forward_velocity(self, velocity: float):
        self.cmd_vel.twist.linear.x = velocity

    def set_backward_velocity(self, velocity: float):
        self.cmd_vel.twist.linear.y = velocity

    def set_angular_velocity(self, velocity: float):
        self.cmd_vel.twist.angular.z = velocity

"""
This will create the node
It will continue to run it before destroying it
One done it will destroy the node and shutdown rcply
"""
def main():
    rclpy.init(args=args)
    motor_controller = Motors()
    rclpy.spin(Motor_controller)
    motor_controller.destroy_node()
    rclpy.shutdown()
    return

if __name__ == "__main__":
    main()
