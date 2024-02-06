#!/usr/bin/python3
"""
Defines a function that appends a string at the end of text file
"""


def append_write(filename="", text=""):
    """
    Args:
        filename: name of the file
        text(str): text to append
    """
    with open(filename, "a", encoding="utf-8") as ap:
        return ap.write(text)
