#!/usr/bin/python3
"""Max integer"""


def max_integer(list=[]):
    """max integer"""

    if len(list) == 0:
        return None
    result = list[0]
    for i in range(1, len(list)):
        if list[i] > result:
            result = list[i]
    return result
