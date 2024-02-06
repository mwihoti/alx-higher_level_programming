#!/usr/bin/python3
"""Defines function that creates an object from JSON File"""
import json


def load_from_json_file(filename):
    """
    creates object from a JSON file
    """
    with open(filename) as jfile:
        return json.load(jfile)
