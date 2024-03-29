#!/usr/bin/python3
"""
Inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle which inherits
    from BaseGeometry
    """
    def __init__(self, width, height):
        """
        initializes the method

        Args:
            height: "height"
            width: "width"
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        method to get area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        method that returns string
        """
        st = "[" + str(self.__class__.__name__) + "] "
        st += str(self.__width) + "/" + str(self.__height)
        return st
