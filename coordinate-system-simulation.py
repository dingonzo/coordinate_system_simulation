from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def __init__(self, x:int, y: int):
        self.x = x
        self.y = y

    def show(self):
        print(f"x={self.x}, y={self.y}")

lowerLeft = Point(0,0)
lowerLeft.show()
upperRight = Point(500,500)
upperRight.show()

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


