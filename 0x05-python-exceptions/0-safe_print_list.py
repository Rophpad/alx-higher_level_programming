#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while True:
        if i < x:
            try:
                print(my_list[i], end='')
                i += 1
                if i == x:
                    raise IndexError
            except IndexError:
                print('')
                print("nb_print: {}".format(i))
                break
        else:
            print("nb_print: {}".format(i))
            break
