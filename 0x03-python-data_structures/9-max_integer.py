#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = 0
    if len(my_list) == 0:
        return None
    else:
        for element in my_list:
            if max_int < element:
                max_int = element
        return max_int
