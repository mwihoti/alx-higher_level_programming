#!/usr/bin/python3
"""
Define Class Base
"""


class Base:

    """
    class base with a private class
    _nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes base
        Args:
            id(int): base id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
