#!/usr/bin/python3
"""
Python script that list 10 commits of  repository
"""
import sys
import requests


if __name__ == "__main__":
    api = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    r = requests.get(api)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
