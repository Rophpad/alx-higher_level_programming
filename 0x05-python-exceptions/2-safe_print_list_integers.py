#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = not_int = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            i += 1
            if i == x:
                print('')
                return i
        except (TypeError, ValueError):
            i += 1
            not_int += 1
            if i == x:
                print('')
                return (i - not_int)
