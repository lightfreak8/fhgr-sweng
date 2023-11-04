"""
shape.py

abstract class Shape:
shape class template

changes:
1.0     2023-10-27      created
1.1     2023-11-04      add getCenter

public functions:
    getName(self):      get name of shape: Circle, Triangle, Rectangle...
    getCenter(self):    get center of mass (point)
    getColor(self):     get color (string)

"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getName(self):
        pass
    def getCenter(self):
        pass
    def getColor(self):
        if self.color is None:
            return ""
        else:
            return self.color

