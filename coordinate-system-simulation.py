# This code simulates a coordinate system using classes and dataclasses in Python. 
# It defines a Point class to represent points in the coordinate system and a Canvas class to represent the drawing area. 
# The Point class has a method to display its coordinates, and the 
# Canvas class has a method to create a Point instance and display its coordinates as well as its own dimensions.

from dataclasses import dataclass

@dataclass

# namespace for the Point class
class Point:
    x: int
    y: int

    def __init__(self, x:int, y: int):
        self.x = x
        self.y = y

    def show(self):
        print(f"x={self.x}, y={self.y}")
        
# Create instances of Point to represent the lower left and upper right corners of the coordinate system
lowerLeft = Point(0,0)
lowerLeft.show()
upperRight = Point(500,500)
upperRight.show()

# name: namespace for the Canvas class
# function: call_show() - creates an instance of Point and calls its show() method, then prints the dimensions of the canvas
# arguments: x (int), y (int) - dimensions of the canvas
# return: None
# effect: prints the coordinates of the Point instance and the dimensions of the canvas
class Canvas:
    x: int
    y: int

    def __init__(self, x:int, y: int):
        self.x = x
        self.y = y

    def call_show(self):
        instance_Point = Point(self.x, self.y)
        instance_Point.show()
        print(f"x={self.x}, y={self.y}")

#create an instance
obj_Canvas = Canvas(500, 500)

# call the method
obj_Canvas.call_show()
