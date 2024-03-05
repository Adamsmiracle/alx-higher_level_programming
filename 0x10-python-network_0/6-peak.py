#!/usr/bin/python3

"""
Finds the the peak element of the list
"""


def find_peak(list_of_integers):
    """ finds the peak element of the list"""
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return (list_of_integers[-1])
