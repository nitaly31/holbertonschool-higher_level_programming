#!/usr/bin/python3
"""Class Square"""

class Square:

    """Private instance attribute: size
    size must be an integer
    The size is greater than or equal to 0
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = int(size)
