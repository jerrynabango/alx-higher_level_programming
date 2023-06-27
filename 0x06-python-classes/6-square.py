#!/usr/bin/python3

"""Coordinates of a square"""


class Square:
    """Defines a square based on 5-square.py"""

    def __init__(self, size=0, position=(0, 0)):
        """Initilization of a square.
        instance: size & position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        @property: Defines the method(Getter for specific attribute).
        private attribute: __size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        @size.setter: Defines the setter for the property.
        private attribute: self.__size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        @property: Defines the method(Getter for specific attribute).
        private attribute: __position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square"""
        if self.size == 0:
            print("")
            return

        else:
            if self.position[1] > 0:
                for square in range(self.position[1]):
                    print('\n', end="")
            for square in range(self.size):
                print("{}{}".format(' ' * self.position[0], '#' * self.size))
