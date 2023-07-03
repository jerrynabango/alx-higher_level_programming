#!/usr/bin/python3
"""A square is a rectangle"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """Returns new rectangle instance with width == height == size"""
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
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
        string = ""
        if self.__width != 0 and self.__height != 0:
            for rectangle in range(self.height - 1):
                string += str(self.print_symbol) * self.width + "\n"
            string += str(self.print_symbol) * self.width
        return string

    def __repr__(self):
        """String representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Called when the rectangle has been removed"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles with their instances."""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return

    @classmethod
    def square(cls, size=0):
        """Returns new rectangle instance with width == height == size"""
        return cls(size, size)
