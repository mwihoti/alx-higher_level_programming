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
    if len_lists == 0:
        return None
    if len_lists == 1:
        return lists[0]
    if len_lists == 2:
        return max(lists)

    left = 0
    right = len_lists - 1
    while left < right:
        mid = (left + right) // 2
        if lists[mid] < lists[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return lists[left]
