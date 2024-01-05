#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for m in range(len(matrix)):
            for mat in range(len(matrix[m])):
                if mat != len(matrix[m])- 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[m][mat]), end=endspace)
            print()
