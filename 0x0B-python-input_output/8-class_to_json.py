#!/usr/bin/python3
"""Defines a function that returns dictionary description with simple data"""
import json


def class_to_json(obj):
    """
    Args:
        obj: instance of class
    """
    return obj.__dict__
