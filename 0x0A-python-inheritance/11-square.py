#!/usr/bin/python3
"""Square #2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square """
    def __init__(self, size):
        """Initilize the Rectangle"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Area of the Square"""
        area = self.__size * self.__size
        return area

    def __str__(self):
        """string representation of the Square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
