#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_int = my_list[0]
        for element in my_list[1:]:
            if max_int < element:
                max_int = element
        return max_int
