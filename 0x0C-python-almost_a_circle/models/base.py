#!/usr/bin/python3
''' Base class '''


import json


class Base:
    ''' The first class Base '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Class constructor

        If id is not None, assign the public instance attribute id with this
        argument value - you can assume

        otherwise, increment __nb_objects and assign the new value to the
        public instance attribute id
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Dictionary to JSON string
        JSON is one of the standard formats for sharing data representation.
        returns the JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
