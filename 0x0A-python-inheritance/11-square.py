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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
