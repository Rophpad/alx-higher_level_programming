#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = 0
    if my_list == []:
        return None
    else:
        for element in my_list:
            if max_int < element:
                max_int = element
        return max_int
