#!/usr/bin/python3
"""Defines pascals Triangle"""


def pascal_triangle(n):
    """
    represents pascal Triangle
    """
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) != n:
        t = tr[-1]
        tm = [1]
        for i in range(len(t) - 1):
            tm.append(t[i] + t[i + 1])
        tm.append(1)
        tr.append(tm)
    return tr
