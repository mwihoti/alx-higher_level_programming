#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers.
    """
    lists = list_of_integers
    len_lists = len(lists)
    for i in range(1, len_lists - 1):
        if (len_lists[i - 1] <= len_lists[i] >= len_lists[i + 1]):
            return (len_lists[i])
    return (None)
