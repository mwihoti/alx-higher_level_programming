#!/usr/bin/python3

"""Size Validation"""


class Square:
    """Body of class square"""

    def __init__(self, size=0):
        """initializes a square
        args:
            size - size of a square and must be a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
