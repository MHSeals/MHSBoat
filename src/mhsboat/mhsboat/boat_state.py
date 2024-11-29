#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from geometry_msgs.msg import TwistStamped

"""
This script uses a simple state machine to transition
between control modes, tasks, actions, etc. Remember,
this script isn't run directly, but rather called
within the launch file that starts all the nodes that
communicate with the state machine node that makes 
decisions. The node outputs to /cmd_vel, which is used 
by motors.py to output PWM signals.

"""

class BoatStateMachine(Node):
    # Initialize the robot and set states
    def __init__(self):
        super().__init__('mhsboat')

        self.states = {
            "manual": self.manual_state,
            "stop": self.stop_state,
            "search": self.search_state,
            "task1": self.task1_state,
            "task2": self.task2_state, 
        }
        self.current_state = "manual"

    def manual_state(self):
        return
    
    def stop_state(self):
        return
    
    def search_state(self):
        return
    
    def task1_state(self):
        return
    
    def task2_state(self):
        return
    
def main():
    rclpy.init()
    
if __name__ == "__main__":
    main()