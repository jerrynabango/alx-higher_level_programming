#!/usr/bin/python3
"""Print Square instance"""


class Square:
    """Defines a square based on 6-square.py"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the Square.
        instance: self.size, self.position"""
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
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
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
        else:
            if self.position[1] > 0:
                instance = 0
            while instance < self.position[1]:
                print('\n', end="")
                instance += 1
        instance = 0
        while instance < self.size:
            print("{}{}".format(' ' * self.position[0], '#' * self.size))
            instance += 1

    def __str__(self):
        """Conversion to node"""
        square = ""
        if self.size == 0:
            return square
        else:
            instance = 0
        while instance < self.position[1]:
            square += '\n'
            instance += 1

        instance = 0
        while instance < self.size:
            square += ' ' * self.position[0]
            square += '#' * self.size
            square += '\n'
            instance += 1

        return square[:-1]
