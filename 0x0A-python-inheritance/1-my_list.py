#!/usr/bin/python3
""" a class MyList that inherits from list"""


class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
