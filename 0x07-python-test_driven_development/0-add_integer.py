#!/usr/bin/python3

"""
Define integer addition
"""


def add_integer(a, b=98):
    """
    method add_integers.


    Args:
        a(int): first integer
        b(int): second integer


    Returns:
        int: sum of two integers
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
