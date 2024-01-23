#!/usr/bin/python3

"""Defines how we get Area of a square"""


class Square:
    """Represents class Square"""
    def __init__(self, size=0):
        """Initialization of attributes

        args:
            size - used to get area of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size * self.__size
