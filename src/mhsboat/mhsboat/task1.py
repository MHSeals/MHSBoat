import numpy as np
from utils import *
import rclpy
from rclpy.node import Node

# TODO: Fix syntax and finish writing task

class task1(Node):
"""
Constructor for a node with the name "task1_subscriber"
Expected to recieve a BouyPair from 'topic'
Has a queue size of 10
"""
  def __init__(self):
    super().__init__('task1_subscriber')
    self.subscription = self.create_subscription(
      BouyPair, '/yolo_output', self.listener_callback, 10
    )
      
#After hearing from node, adjusts so midpt of bouys is in the middle of camera
  def listener_callback(self, msg):
    """
    Psuedo code

    find mind point of bouy pair
    if too far left
      power left motor
    if too far right
      power right motor
    if middle
      power motors evenly
    """

def start_task1():
  rclpy.__init__()
  task1_subscriber = Task1_subscriber()
  rclpy.spin(task1_subscriber)
  task1_subscriber.destroy_node

"""
Notes + Goals:
- The first task is far simpler than I anticipated, you only have to navigate
  between two pairs of buoys that are lined up with task 2.
- The red buoy is on the left, the green buoy is on the right.
- The buoys in each pair are 6-10ft apart and each pair is 25-100ft apart.
- The buoys are 18 inches in diameter and 39 inches above the waterline.
- Since it is the first task, you can line up the boat 6 feet before the buoys,
  making it an even easier problem.
- This task should be possible with only using a camera.
- This script can be imported by writing "from taskone import start_task1"
- ADD ROS FUNCTIONALITY, I wrote these scripts with raw Python because that
  was faster for me.

"""
