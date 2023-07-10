#!/usr/bin/python3
"""My Integer"""


class MyInt(int):
    """Inherits from int"""
    def __eq__(self, other):
        """Identify if two integers are  the same"""
        return int(self) != other

    def __ne__(self, other):
        """Identify two integers if they are not in the same equal"""
        return int(self) == other
