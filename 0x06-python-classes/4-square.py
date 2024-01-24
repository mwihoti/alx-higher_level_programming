#!/usr/bin/python3

"""Accessing and updating private attribue"""


class Square:
    """The class to create square"""

    def __init__(self, size=0):
        """Initializing atrtribute

        args:
            size(int) - to be int
        """
        self.size = size

    @property
    def size(self):
        """getter - retrive private size attribute"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """setter - property setter
        args:
            value
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Get area of the square

        Returns:
            Area of the square(int)
        """
        return self.__size * self.__size
