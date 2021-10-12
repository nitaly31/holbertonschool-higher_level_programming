#!/usr/bin/python3
''' Same class or inherit from  '''


def is_kind_of_class(obj, a_class):
    ''' The object is an instance of, or if the object is an instance of
    a class that inherited from '''
    return isinstance(obj, a_class)
