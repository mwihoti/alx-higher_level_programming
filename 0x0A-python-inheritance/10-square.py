#!/usr/bin/python3
"""
module 10-square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class square
    """

    def __init__(self, size):
        """
        Method initializers
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
