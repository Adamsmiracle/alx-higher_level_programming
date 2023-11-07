#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in my_list.reversed():
        print("{i}".format(i))
