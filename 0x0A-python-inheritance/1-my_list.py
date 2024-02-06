#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """Class with method print_sorted"""

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        elements of the list will be of type int
        """

        print(sorted(self))
