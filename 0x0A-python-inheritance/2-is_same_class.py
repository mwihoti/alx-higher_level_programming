#!/usr/bin/python3
"""
checks if module is instance of the specifiend class
"""


def is_same_class(obj, a_class):
    """
    Returns true if the object is exactly an instance of specified class
    """

    return type(obj) is a_class
