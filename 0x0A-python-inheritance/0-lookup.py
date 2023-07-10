#!/usr/bin/python3
"""
Function that returns the list of available attributes and
methods of an object
"""


def lookup(obj):
    """list of objeccts that are available"""
    return dir(obj)
