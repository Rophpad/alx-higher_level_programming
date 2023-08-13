#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0] == 0):
        print("".format())
    for i in range(len(matrix)):
        idx = 0
        for element in matrix[i]:
            if (idx < len(matrix[i] - 1)):
                print("{}".format(element), end=' ')
            else:
                print("{}".format(element), end='\n')
                idx += 1
