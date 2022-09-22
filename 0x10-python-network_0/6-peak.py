#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers.
        Args:
            list_of_integers (list): List of integers
    """
    if list_of_integers == []:
        return None

    return max(list_of_integers)