#!/usr/bin/python3
""" Size validation """


class Square:
    """ Defines a square based on 1-square.py """

    def __init__(self, size=0):
        """Intilization of the square.
        parameter: size.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
