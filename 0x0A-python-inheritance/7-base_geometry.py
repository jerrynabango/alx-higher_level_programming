#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """base class for Geometry"""
    def area(self):
        """ raises an Exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """value validator"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
