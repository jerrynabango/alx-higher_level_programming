#!/usr/bin/python3
"""Area and Perimeter"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle.
        instances: self.width, self.height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width
        private attribute: __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.
        private attribute: __width
        """
        if type(value) is not int:  # Identify the data type if its an integer
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height
        private attribute: __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.
        private attribute: __height
        """
        if type(value) is not int:  # Identify the data type if its an integer
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """
        Area of the rectangle(widht * height)
        private attribute: __width, __height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Total distance of the rectangle(width + height) * 2
        private attribute: __width, __height
        """
        return (self.__width + self.__height) * 2
