#!/usr/bin/python3
"""Low memory cost"""


class LockedClass:
    """
    Prevents user from creating new instance attributes,
    except if it's called first_name.
    """
    __slots__ = 'first_name'
