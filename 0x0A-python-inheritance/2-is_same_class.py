#!/usr/bin/python3
''' Exact same object '''


def is_same_class(obj, a_class):
    '''The object is exactly an instance of the specified class '''
    return type(obj) is a_class
