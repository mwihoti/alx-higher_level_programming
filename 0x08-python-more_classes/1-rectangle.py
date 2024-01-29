#!/usr/bin/python3

"""
Checks Rectangle Width anf height
"""


class Rectangle:
    """
    Rectangle width defined by width and height
    """
    def __init__(self, width, height):
        """
        initializes Reactangle width and height

        args:
            width: width
            height: height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves the width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width instance of a Rectangle instance
        Args:
            value: value of width(int)
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves rectangle heights
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets height for change of rectangle instance
        Args:
            value: height instance
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
