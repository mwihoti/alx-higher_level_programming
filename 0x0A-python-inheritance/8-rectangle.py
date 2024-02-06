#!/usr/bin/python3
# BaseGeometry class is imported from another module

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
==============================
Class Rectangle
===================================
"""

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
