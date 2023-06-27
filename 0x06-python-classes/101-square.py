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

    @size.setter
    def size(self, value):
        """Size of the square"""
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

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
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Area of the square.
        instance: self.size
        """
        return self.size * self.size  # return self.__size **2

    def my_print(self):
        """
        Print the Square to stdout using '#'
        """
        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                for i in range(self.position[1]):
                    print('\n', end="")
            for i in range(self.size):
                print("{}{}".format(' ' * self.position[0], '#' * self.size))

    def __str__(self):
        """
        String representation of instances
        """
        string = ""
        if self.size == 0:
            return string
        else:
            if self.position[1] > 0:
                for i in range(self.position[1]):
                    string += '\n'
            for i in range(self.size):
                string += ' ' * self.position[0]
                string += '#' * self.size
                string += '\n'
            return string[:-1]
