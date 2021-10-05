#!/usr/bin/python3
"""Class Square"""


class Square:

    """Private instance attribute: size
    size must be an integer
    The size is greater than or equal to 0
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object
        """
            self.__size = size
            self.__position = position

    def area(self):
        """that returns the current square area
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """to retrieve it
        """

        return self.__size

    @size.setter
    def size(self, value):
        """to set it
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):

        return self.__position

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object
        """
        if type(position) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if 

    def my_print(self):
        """Printing a square
        """

        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print(''.join('#' for i in range(self.size)))
