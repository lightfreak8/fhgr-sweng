"""
circle.py

class Circle:
circle containing position and radius

changes:
1.0     2023-10-27      created
1.1     2023-11-04      add: getCenter
1.1.1   2023-11-05      fix: function descriptions

public functions:
    __init__(self):     constructor, pass point and radius
    __str__(self):      string representation
    getName(self):      print name of the polygon
    getCenter(self):    return center of circle (Point)

"""

from typing import Union
from point import Point
from shape import Shape

class Circle(Shape):
    def __init__(self, origin: Point, radius: Union[float, int]):
        """
        constructor
        Args:
            origin, center of circle
            radius, radius of circle
        """
        if not isinstance(origin, Point):
            raise Exception(f'Expected a Point (got {type(origin)})')
        if not isinstance(radius, float) and not isinstance(radius, int):
            raise Exception(f'Wrong type for radius ({type(radius)})')
        self.origin = origin
        self.radius = radius
        self.color = ""

    def __str__(self):
        """
        Returns:
            string representation
        """
        s = f'[{self.origin}, {self.radius}]'
        return s

    def getCenter(self):
        """
        Returns:
            center point of the circle
        """
        return self.origin

    def getName(self):
        """
        Returns:
            string literal 'Circle'
        """
        return 'Circle'
