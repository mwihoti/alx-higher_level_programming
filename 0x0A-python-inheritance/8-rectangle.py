#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Rectangle module that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    class rectangle
    """

    def __init__(self, width, height):
        """
        Args:
        width: width
        height: "height"
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
