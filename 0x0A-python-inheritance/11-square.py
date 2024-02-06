#!/usr/bin/python3
"""
defines square#2
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square that inherits from Rectangle
    """
    def __init__(self, size):

        """
        method initializer
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
