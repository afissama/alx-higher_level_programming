#!/usr/bin/python3


"""
This is a simple module which contains one function
perform divison on a given matrix
"""
def matrix_divided(matrix, div):
    """
    Return a new matrix with values divided per div
    >>>matrix_divided([[1,2,3]], 1)
    [[1,2,3]]
    """
    row_len = len(matrix[0])
    for _row in matrix:
        if row_len != len(_row):
            raise TypeError("Each row of the matrix must have the same size")
    try:
        return [([round((val / div), 2) for val in row]) for row in matrix]
    except TypeError:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")
