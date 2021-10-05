#!/usr/bin/python3
''' Real definition of a rectangle '''


class Rectangle:
    ''' Defines a rectangle '''

    def __init__(self, width=0, height=0):
        ''' Instantiation with optional width and height '''
        self.height = height
        self.width = width

    @property
    def width(self):
        ''' method that returns the value of the width and
        private instance attribute '''

        return self.__width

    @width.setter
    def width(self, value):
        ''' method that calculates width  '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' method that returns the value of the height and
        private instance attribute '''
        return self.__height

    @height.setter
    def height(self, new_height):
        ''' method that calculates the height '''
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        if new_height < 0:
            raise ValueError("height must be >= 0")
        self.__height = new_height

    def area(self):
        ''' Area of rectangle '''
        return self.__width * self.__height

    def perimeter(self):
        ''' Perimeter of rectangle '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        result += '\n'.join("#" * self.__width
                            for j in range(self.__height))
        return result

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
