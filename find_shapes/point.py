"""
point.py

class Point:
containing x and y coordinate in 2 dimensions

changes:
1.0     2023-10-27      created
1.1     2023-11-02      add: asarray, dist, is_intersect, _onSegment, _orientation
1.2     2023-11-04      add: __add__, __sub__, __mul__, __truediv__; fix dist

public functions:
    __init__(self, x=0, y=0):   constructor, taking optional coordinates
    __str__(self):              string representation

public attributes:
    x: x-coordinate
    y: y-coordinate

"""

import numpy as np

def _onSegment(p, q, r):
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False

def _orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise
    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
    # for details of below formula.
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):
        # Clockwise orientation
        return 1
    elif (val < 0):
        # Counterclockwise orientation
        return 2
    else:
        # Collinear orientation
        return 0

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, new):
        if isinstance(new, int) or isinstance(new, float):
            return Point(self.x + new, self.y + new)
        elif isinstance(new, Point):
            return Point(self.x + new.x, self.y + new.y)
        else:
            raise ValueError("invalid argument")

    def __sub__(self, new):
        if isinstance(new, int) or isinstance(new, float):
            return Point(self.x - new, self.y - new)
        elif isinstance(new, Point):
            return Point(self.x - new.x, self.y - new.y)
        else:
            raise ValueError("invalid argument")

    def __mul__(self, new):
        if isinstance(new, int) or isinstance(new, float):
            return Point(self.x * new, self.y * new)
        elif isinstance(new, Point):
            return Point(self.x * new.x, self.y * new.y)
        else:
            raise ValueError("invalid argument")

    def __truediv__(self, new):
        if isinstance(new, int) or isinstance(new, float):
            return Point(self.x / new, self.y / new)
        elif isinstance(new, Point):
            return Point(self.x / new.x, self.y / new.y)
        else:
            raise ValueError("invalid argument")

    def asarray(self):
        return np.asarray([self.x, self.y])

    # https://stackoverflow.com/questions/39840030/distance-between-point-and-a-line-from-two-points
    # self=point, p2+p2=line
    def dist(self, p2=None, p3=None):
        if p2 is None and p3 is None:
            dist = np.sqrt((self.x)**2 + (self.y)**2)
            return dist
        elif p2 is not None and p3 is None:
            dist = np.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)
            return dist
        elif p2 is not None and p3 is not None:
            p1 = self.asarray()
            p2 = p2.asarray()
            p3 = p3.asarray()
            dist = np.abs(np.cross(p2-p1, p1-p3)) / np.linalg.norm(p2-p1)
            return dist
        else:
            raise ValueError("invalid argument combination")

    # https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
    # self+q1=line1, p2+q2=line2
    def is_intersect(self, q1, p2, q2):
        # Find the 4 orientations required for
        # the general and special cases
        p1 = self
        o1 = _orientation(p1, q1, p2)
        o2 = _orientation(p1, q1, q2)
        o3 = _orientation(p2, q2, p1)
        o4 = _orientation(p2, q2, q1)

        # General case
        if ((o1 != o2) and (o3 != o4)):
            return True

        # Special Cases
        # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
        if ((o1 == 0) and _onSegment(p1, p2, q1)):
            return True
        # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
        if ((o2 == 0) and _onSegment(p1, q2, q1)):
            return True
        # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
        if ((o3 == 0) and _onSegment(p2, p1, q2)):
            return True
        # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
        if ((o4 == 0) and _onSegment(p2, q1, q2)):
            return True

        # If none of the cases
        return False

