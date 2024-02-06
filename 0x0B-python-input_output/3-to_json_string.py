#!/usr/bin/python3
""" Defines function that returns JSON"""


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
