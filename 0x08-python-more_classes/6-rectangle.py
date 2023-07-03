#!/usr/bin/python3
"""How many instances"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width, height):
        """
        Initializes a rectangle
        instance: width, height
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """"
        Getter method for width
        private attribute: __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width
        private attribute: __width
        """
        if type(value) is not int:  # Identify the data type if its an integer
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """"
        Getter method for height
        private attribute: __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height
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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """prints rectangle using #"""
        string = ""  # empty string
        if self.__width != 0 and self.__height != 0:
            for rectangle in range(self.height - 1):
                string += ("#" * self.width) + "\n"
            string += "#" * self.width
        return string

    def __repr__(self):
        """String representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Called when the rectangle has been removed"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
