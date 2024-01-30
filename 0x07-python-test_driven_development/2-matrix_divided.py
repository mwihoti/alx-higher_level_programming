#!/usr/bin/python3
"""Define maxtrix division"""


def matrix_divided(matrix, div):
    """ Divide all elements of a matrix.

    Args:
    matrix(list): list in int or float
    div (int/float): the divisor

    Raises:
        TypeError: if matrix not a list
        TypeError: matrix is not regular
        TypeError: if matrix anything rather than int and float
        TypeError: if div is not a number

    Returns:
        New matrix list
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(col == len_rows[0] for col in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(col / div, 2) for col in row] for row in matrix]

    return new_matrix
