import numpy as np
from typing_extensions import Self

"""
This won't script won't be used to publish or
subscribe to any data. It is purely filled with
utilities that may be repeatedly used in scripts
for calculations (i.e. useful functions or classes).

"""

# Helper function for calculating the midpoint of two points by using matrix addition
def mdpt(p1, p2):
    return (p1 + p2) / 2
    
# Calculates Euclidean norm aka distance from the origin after subtracting to get overall magnitude
def dist(p1, p2):
    return np.linalg.norm(p1 - p2)

# Simplifying the problem by making a buoy a single point in 2D space
class Buoy:
    # First buoy assignment method that takes in a 2D point
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    # Second buoy assignment method that takes in a bounding box
    @classmethod
    def from_camera(cls, bbox, type) -> Self:
        return cls(*mdpt(bbox[0], bbox[1]), type)

    # To string method for debugging
    def __str__(self) -> str:
        return f"Buoy({self.x}, {self.y}, {self.type})"

# This class will be expanded upon later
class BuoyPair:
    def __init__(self, buoy1, buoy2):
        self.buoy1 = buoy1
        self.buoy2 = buoy2
        self.mdpt = Buoy(*mdpt(buoy1, buoy2))