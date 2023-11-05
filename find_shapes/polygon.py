"""
polygon.py

class Polygon:
polygon containing points

changes:
1.0     2023-10-27      created
1.1     2023-11-04      add: getCenter
1.1.1   2023-11-05      fix: function descriptions

public functions:
    __init__(self):     constructor, pass list of Point (s)
    __str__(self):      string representation
    getName(self):      print name of the polygon
    getCenter(self):    return center of circle (Point)

"""

from point import Point
from shape import Shape

import numpy as np

class Polygon(Shape):
    def __init__(self, points: list):
        """
        Constructor for the Polygon class
        Args:
            points, list of points of the polygon. requires a minimum of 3 points
        """
        if len(points) < 3:
            raise Exception(f'Too few points to represent a polygon ({len(points)})')
        for point in points:
            if not isinstance(point, Point):
                raise Exception(f'Each member has to be Point class (encountered {type(point)})')
        self.points = points
        self.color = ""

    def __str__(self):
        """
        Returns:
            string representation of the polygon
        """
        s = '['
        first = True
        for point in self.points:
            if not first:
                s += ', '
            s += f'{point}'
            first = False
        s += ']'
        return s

    def getName(self):
        """
        Gets the corresponding name of the polygon
        Returns:
            String of the polygon name, e.g. 'Triangle', 'Rectangle', 'Pentagon', etc...
        """
        if len(self.points) == 3:
            return 'Triangle'
        elif len(self.points) == 4:
            return 'Rectangle'
        elif len(self.points) == 5:
            return 'Pentagon'
        elif len(self.points) == 6:
            return 'Hexagon'
        else:
            return ""
            #raise Exception(f'Unknown polygon name containing {len(self.points))} points')

    def getCenter(self):
        """
        Returns:
            The center of mass of a polygon
        """
        center = Point()
        for point in self.points:
            center += point
        center /= len(self.points)
        return center

    def getContour(self):
        """
        Returns:
            The contour of the polygon
        """
        flat = []
        for p in self.points:
            flat.append([p.x, p.y])
        result = np.array(flat)
        return result

