#!/usr/bin/python3
''' Only sub class of '''


def inherits_from(obj, a_class):
    ''' the object is an instance of a class that inherited
    (directly or indirectly) from the specified class '''
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
