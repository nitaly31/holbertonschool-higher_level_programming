#!/usr/bin/python3
""" Real definition of a rectangle """


class Rectangle:
    """ Defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """

        self.width = width
        self.height = heigth

    @property
    def width(self):
        """ method that returns the value of the width and
        private instance attribute

        """

        return self.__width

    @width.setter
    def width(self, new_width):
        """ method that calculates width  """
        if type(new_width) is not int:
            raise TypeError('width must be an integer')
        if new_width < 0:
            raise ValueError('width must be >= 0')
        self.__width = new_width

    @property
    def height(self):
        """  method that returns the value of the height and
        private instance attribute """
        return self.__heigth

    @height.setter
    def height(self, new_height):
        """ method that calculates the height  """
        if type(new_height) is not int:
            raise TypeError('height must be an integer')
        if new_height < 0:
            raise ValueError('height must be >= 0')
        self.__height = new_height
