Module matrix_divided
======================

Using matrix_divided:
divide each element of a matriz and return a new.

    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided

Checking docstring for module:
        >>> __import__('2-matrix_divided').__doc__ != None
        True

Check docstring for function:
        >>> len(matrix_divided.__doc__) > 0
        True

Should return new matrix:
    >>> matrix = [[1, 2, 0], [4, 5, 5]]
    >>> matrix_divided(matrix, 1)
    [[1.0, 2.0, 0.0], [4.0, 5.0, 5.0]]

Divided by 0:
    >>> matrix = [[1, 2, 0], [4, 5, 5]]
    >>> matrix_divided(matrix, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero

Divided by 0 and diff lenght:
    >>> matrix = [[1, 2, 0], [4, 5]]
    >>> matrix_divided(matrix, 0)
    Traceback (most recent call last):
    ...
    TypeError: Each row of the matrix must have the same size

divided by decimal matriz:
    >>> matrix = [[1, 2],[1, 3]]
    >>> matrix_divided(matrix, 1.33333)
    [[0.75, 1.5], [0.75, 2.25]]

Checking divide with another type than int or float:
    >>> matrix = [[1, 2],[1, 3]]
    >>> matrix_divided(matrix, "Hello")
    Traceback (most recent call last):
    ...
    TypeError: div must be a number

Checking what happens when user pass tuple or set:
    >>> matrix = [[1, 2], {1, 3}]
    >>> matrix_divided(matrix, 5)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
