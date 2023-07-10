#!/usr/bin/python3
"""Full rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initilize the Rectangle """
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """Area of the Rectangle"""
        area = self.__width * self.__height
        return area

    def __str__(self):
        """str representation of the Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
