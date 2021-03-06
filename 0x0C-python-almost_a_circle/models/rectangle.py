#!/usr/bin/python3
''' First Rectangle '''


from models.base import Base


class Rectangle(Base):
    ''' Class Rectangle inherits from Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Class constructor
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
        Width getter. the value of the width and
        private instance attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Width setter. Method that calculates width
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        Height getter. The value of the width and
        private instance attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Height setter. Method that calculates the height
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        x getter
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        x setter
        '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        y getter
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        y setter
        '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        Returns the area value of the Rectangle instance
        '''
        return self.__width * self.__height

    def display(self):
        '''
        Prints in stdout the Rectangle instance with the character "#"
        '''
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"
        print(rectangle, end='')

    def __str__(self):
        '''
        Overriding the __str__ method
        '''
        return("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        '''
        Assigns an argument to each attribute
        **kwargs must be skipped if *args exists and is not empty.
        Each key in this dictionary represents an attribute to the instance
        '''
        args_list = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            for i in range(len(args)):
                setattr(self, args_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        Method that returs a dictionary with properties
        '''
        key_list = ["id", "width", "height", "x", "y"]
        value_list = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(key_list, value_list))
