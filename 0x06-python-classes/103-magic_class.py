#!/usr/bin/python3
"""ByteCode"""
import math


class MagicClass:
    """Magic class"""
    def __init__(self, radius=0):
        """Initialization of the class"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Area of the object"""
        return math.pi * self.__radius * self.__radius

    def circumference(self):
        """Circumference of the object"""
        return self.__radius * 2 * math.pi
