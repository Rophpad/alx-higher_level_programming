#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    for element in my_list:
        if not(element % 2):
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list
