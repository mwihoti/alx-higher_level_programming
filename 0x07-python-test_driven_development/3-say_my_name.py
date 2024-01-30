#!/usr/bin/python3

"""
Prints my name
"""


def say_my_name(first_name, last_name=""):

    """ prints names

    Args:
        first_name(str): prints name
        last_name(str): prints last name

    Raises:
        TypeError: if first_name not a string
        TypeError: if last_name not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
