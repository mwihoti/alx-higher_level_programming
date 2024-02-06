#!/usr/bin/python3
"""
Defines a function writes a string to text file
"""


def write_file(filename="", text=""):
    """
    writes string to a text file
    """
    with open(filename, "w", encoding="utf-8") as t:
        return t.write(text)
