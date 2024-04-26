#!/usr/bin/python3
import urllib.request
import sys
"""
Python script that takes in a URL, sends a request to the URL
"""


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        res = response.info()
        value = res.get('X-Request-Id')
        print(value)
