#!/usr/bin/python3

"""
defines base_geometry module
"""


class BaseGeometry:

    """
    class BaseGeometry
    """

    @classmethod
    def area(self):
        """
        area not implemented
        """
        raise Exception("area() is not implemented")

    @classmethod
    def integer_validator(self, name, value):
        """
        validates value

        args:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal  0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
