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

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        JSON string to file
        writes the JSON string representation of list_objs to a file
        '''
        filename = "{}.json".format(cls.__name__)
        list_dict = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())
        lists = cls.to_json_string(list_dict)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        '''
        JSON string to dictionary
        returns the list of the JSON string representation json_string
        json_string is a string representing a list of dictionaries
        '''
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Dictionary to Instance
        returns an instance with all attributes already set
        **dictionary can be thought of as a double pointer to a dictionary
        '''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
        File to instances
        returns a list of instances
        the type of these instances depends on cls
        (current class using this method)
        '''
        filename = cls.__name__ + ".json"
        result = []
        try:
            with open(filename, encoding="utf-8") as file:
                obj_list = cls.from_json_string(file.read())
                for dictionary in obj_list:
                    result.append(cls.create(**dictionary))
                return result
        except:
            return result
