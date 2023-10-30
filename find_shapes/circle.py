"""
circle.py

class Circle:
circle containing position and radius

changes:
1.0     2023-10-27      created

public functions:
    __init__(self):     constructor, pass point and radius
    __str__(self):      string representation
    getName(self):      print name of the polygon

"""

from typing import Union
from point import Point
from shape import Shape

class Circle(Shape):
    def __init__(self, origin: Point, radius: Union[float, int]):
        if not isinstance(origin, Point):
            raise Exception(f'Expected a Point (got {type(origin)})')
        if not isinstance(radius, float) and not isinstance(radius, int):
            raise Exception(f'Wrong type for radius ({type(radius)})')
        self.origin = origin
        self.radius = radius
        self.color = ""

    def __str__(self):
        s = f'[{self.origin}, {self.radius}]'
        return s

    def getName(self):
        return 'Circle'
