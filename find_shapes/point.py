"""
point.py

class Point:
containing x and y coordinate in 2 dimensions

changes:
1.0     2023-10-27      created

public functions:
    __init__(self, x=0, y=0):   constructor, taking optional coordinates
    __str__(self):              string representation

public attributes:
    x: x-coordinate
    y: y-coordinate

"""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


