#!/usr/bin/python3
"""Area of a square"""


class Square:
    """Defines a square based on 2-squre.py"""
    def __init__(self, size=0):
        """Initialization function for square.
        parameters: size.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Area of the object.
        Method: area.
        Instance: self
        """
        return (self.__size * self.__size)
