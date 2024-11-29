#!/usr/bin/env python3

# TODO: Collect, publish, and/or process data from the sensors

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from boat_msgs.msg import YoloOuput
import cv2
from ultralytics import YOLO
import os
import time
import numpy as np

# Get the YOLOv11 weights
model_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', "data", "best.pt")
# Start a YOLO model that uses the weights from training
model = YOLO(model_path)

class CameraSubscriber(Node):
    def __init__(self):
        # Subscribe to the camera publisher to get the images
        super().__init__("camera_subscriber")
        self.create_subscription(Image, "/color/image_raw", self.callback, 10)
        
        # Create a publisher to output detection data 
        self.publisher = self.create_publisher(YoloOuput, "YoloOutput")

def main():
    rclpy.init()
    rclpy.spin()

if __name__ == "__main__":
    main()