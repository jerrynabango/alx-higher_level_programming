#!/usr/bin/python3
"""Read definition of a rectangle"""


class Rectangle:
    """defines a rectangle
    private attributes: __width, __height"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width
        private attribute: __width"""
        if type(value) is not int:  # Identify the data type if its an integer
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter method for height
        private attribute: __height"""
        if type(value) is not int:  # Identify the data type if its an integer
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
