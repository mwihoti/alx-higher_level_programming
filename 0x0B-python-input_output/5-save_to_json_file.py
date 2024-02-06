#!/usr/bin/python3
"""Defines a function that writes an object to a text file using json"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
    my_obj(str): text
    filename: file
    """
    with open(filename, "w", encoding="utf-8") as obj:
        json.dump(my_obj, obj)
