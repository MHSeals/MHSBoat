#!/usr/bin/env python3

# TODO: Use the GPIO output of the Jetson to output PWM signals

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped

"""
Subscribe to the cmd_vel topic and run the pwm_output
function to output the PWM signals to the Odroid with
basic kinematics calculations.
NOTE: May seperate access and kinematic scripts if necessary
"""
class Motors(Node):
    def __init__(self):
        super().__init__("motor_controller")
        self.cmd_vel_subscriber = self.create_subscription(
            TwistStamped,
            '/cmd_vel', 
            self.pwm_output,
            10,
        )
        self.cmd_vel = TwistStamped()

"""
Outputs the pwm signal
"""
    def pwm_output(self, cmd_vel){
        # TODO: Calculate the left and right PWM outpust then output it to the Odroid
        # NOTE: Don't make a new script for everything, it's okay to have multiple processes take place in a single script
    }

"""
This will create the node
It will continue to run it before destroying it
One done it will destroy the node and shutdown rcply
"""
def main():
    rclpy.init()
    motor_controller = Motors()
    rclpy.spin(Motor_controller)
    motor_controller.destroy_node()
    rclpy.shutdown()
    return

# Runs the main method when used as an executable in the launch script
if __name__ == "__main__":
    main()
