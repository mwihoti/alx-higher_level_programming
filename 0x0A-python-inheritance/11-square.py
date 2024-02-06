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

        def area(self):
            """
            print area
            """
            return self.__Size ** 2

        def __str__(self):
            return "[Square] {}/{}".format(self.__size, self.__size)
