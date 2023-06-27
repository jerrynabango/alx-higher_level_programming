#!/usr/bin/python3
"""Printing a square"""


class Square:
    """Defines a square based on 4-square.py"""
    def __init__(self, size=0):
        """Initilization of a square.
        instance: size.
        """
        self.size = size

    def area(self):
        """Area for the square.
        private attribute: __size
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
        private attribute: self.__size.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """Square print
        private attribute: __size
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
