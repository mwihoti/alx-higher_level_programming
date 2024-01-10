#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = matrix.copy()

    for i in range(len(matrix)):
        mat[i] = list(map(lambda x: x**2, matrix[i]))

    return (mat)
