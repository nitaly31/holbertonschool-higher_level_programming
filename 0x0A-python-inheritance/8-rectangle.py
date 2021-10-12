#!/usr/bin/python3
''' Rectangle '''


BaseGeometry = __import__("7-base_geometry.py").BaseGeometry

class Rectangle(BaseGeometry):
    ''' class Rectangle that inherits from BaseGeometry '''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.___width = width
        self.__height = height
