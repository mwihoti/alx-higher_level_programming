#!/usr/bin/python3

"""Accessing and updating private attribue"""


class Square:
    def __init__(self, size=0):
        """Initializing atrtribute
        args:
            size- to be int"""
        self.size = size

    @property
    def size(self):
        """retrive private size attribute"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """property setter
        args:
            value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
