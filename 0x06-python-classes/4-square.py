#!/usr/bin/python3
"""Access & update private attribute"""


class Square:
    """Defines a square based on 3-squre.py"""
    def __init__(self, size=0):
        """Initialization function for square.
        parameter: size.
        instance: self.size
        """
        self.size = size

    def area(self):
        """
        Area of the square
        private attribute: self.__size
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        @property: Defines the method(Getter for specific attribute).
        private attribute: __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        @size.setter: Defines the setter for the property.
        private attribute: __size.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
