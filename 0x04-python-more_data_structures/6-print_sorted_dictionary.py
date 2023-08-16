#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for _key in sorted(a_dictionary):
        print("{}: {}".format(_key, a_dictionary[_key]))
