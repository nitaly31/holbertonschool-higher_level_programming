#!/usr/bin/python3
''' Divide a matrix  '''


def matrix_divided(matrix, div):
    ''' function that divides all elements of a matrix  '''
    j = 0
    for y in matrix:
        if type(matrix) is not list or type(matrix[j]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        for x in matrix[j]:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        j += 1

    size = len(matrix[0])
    j = 0
    for y in matrix:
        lenght = len(matrix[j])
        if lenght != size:
            raise TypeError("Each row of the matrix must have the same size")
        j += 1

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    NewMatrix = []
    i = 0
    for y in matrix:
        NewMatrix.append([])
        for x in matrix[i]:
            NewMatrix[i].append(round((x / div), 2))
        i += 1
    return (NewMatrix)
