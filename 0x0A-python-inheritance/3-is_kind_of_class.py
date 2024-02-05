#!/usr/bin/python3

"""
checks if the object is a class instance
"""


def is_kind_of_class(obj, a_class):
    """
    returns true if the object is an instance of an
    object or a class inherited from a class
    """

    return isinstance(obj, a_class)
