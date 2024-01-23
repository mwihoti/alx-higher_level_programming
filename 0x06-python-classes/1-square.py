#!/usr/bin/python3

"""Class Square with private size instance"""


class Square:
    """Square body"""
    def __init__(self, size):
        """initializes a square.

        Args:
            size (int): size of square.
        """
        self.__size = size
