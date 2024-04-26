#!/bin/bash/python3
"""
script that takes in a letter and sends a POST request to http://0.0.0.0:5000/\
        search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[1]
