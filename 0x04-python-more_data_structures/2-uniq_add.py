#!/usr/bin/python3
def uniq_add(my_list=[]):
    _sum = 0
    for num in sorted(set(my_list)):
        _sum += num
    return _sum
