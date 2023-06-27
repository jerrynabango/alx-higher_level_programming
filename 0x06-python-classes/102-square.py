#!/usr/bin/python3
"""Compare 2 squares"""


class Square:
    """Defines a square based on 4-square.py"""
    def __init__(self, size=0):
        """Initialization of the square.
        instance: self.size
        """
        self.size = size

    @property
    def size(self):
        """
        @property: Defines the method(Getter for specific attribute).
        private attribute: __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """
        Area of the square
        """
        return self.__size * self.__size  # return self.__size **2

    def __gt__(self, other):
        """Identify if square is greater than another"""
        return self.area() > other.area()

    def __le__(self, other):
        """Identify the square is less or equal to another"""
        return self.area() <= other.area()

    def __lt__(self, other):
        """Identify if the square is less or equal to another"""
        return self.area() < other.area()

    def __eq__(self, other):
        """Identify if the square is equal to another"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Identify if square is not equal to another"""
        return self.area() != other.area()

    def __ge__(self, other):
        """Identify if square is greater or equal to another"""
        return self.area() >= other.area()
