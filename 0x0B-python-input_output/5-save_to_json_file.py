#!/usr/bin/python3
''' Save Object to a file '''


import json


def save_to_json_file(my_obj, filename):
    ''' function that writes an Object to a text file,
    using a JSON representation '''
    with open(filename, 'r', encoding="utf-8") as f:
        json.dumps(my_obj, f)
