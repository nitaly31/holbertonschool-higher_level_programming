#!/usr/bin/python3
'''
Print square
size is the size length of the square
'''


def print_square(size):
    ''' Function that prints a square with the character "#" '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
