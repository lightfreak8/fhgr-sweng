"""
shape.py

abstract class Shape:
shape class template

changes:
1.0     2023-10-27      created

public functions:
    getName(self):      get name of shape: Circle, Triangle, Rectangle...

"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getName(self):
        pass

