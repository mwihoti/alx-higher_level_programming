#!/usr/bin/python3
"""
Defines function that reads a text file
"""


def read_file(filename=""):
    """
    print textfile to stdout
    """
    with open(filename, encoding='utf-8') as txt:
        print(txt.read(), end="")
