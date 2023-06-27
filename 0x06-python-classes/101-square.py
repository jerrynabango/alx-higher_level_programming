#!/usr/bin/python3
"""Print Square instance"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the Square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        @property: Defines the method(Getter for specific attribute).
        private attribute: __size
        """
        return self.__size

    @property
    def position(self):
        """
        @property: Defines the method(Getter for specific attribute).
        private attribute: __position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Position of the attribute"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        """Size of the square"""
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Area of the square.
        instance: self.size
        """
        return self.size * self.size  # return self.__size **2

    def my_print(self):
        """print the square"""
        if self.size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Conversion to node"""
        square = ""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")