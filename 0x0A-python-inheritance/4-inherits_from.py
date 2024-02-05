#!/usr/bin/python3

"""
checks if the object is an instance of a class inherited directly or indirectly
"""


def inherits_from(obj, a_class):
    """
    returns True if object is an instance of a class thats is inherited from a class
    """

    return False if type(obj) is a_class else isinstance(obj, a_class)
