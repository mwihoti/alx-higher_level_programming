#!/usr/bin/python3
"""Defines function that returns object from json"""
import json


def from_json_string(my_str):
    """
    Args:
        my_str: text string
    """
    return json.loads(my_str)
