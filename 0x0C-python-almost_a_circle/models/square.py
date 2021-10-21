#!/usr/bin/python3
''' And now, the Square! '''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Class Square inherits from Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Class constructor
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
        Size getter
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        Size setter
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''
        The overloading __str__ method
        '''
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        '''
        Assigns attributes
        *args is the list of arguments - no-keyworded arguments
        **kwargs can be thought of as a double pointer to a dictionary:
        key/value (keyworded arguments)
        **kwargs must be skipped if *args exists and is not empty
        '''
        arg_list = ["id", "size", "x", "y"]
        if args and args[0] is not None:
            for i in range(len(args)):
                setattr(self, arg_list[i], arg[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        Method that returs a dictionary with properties
        '''
        key_list = ["id", "size", "x", "y"]
        value_list = [self.id, self.size, self.x, self.y]
        return dict(zip(key_list, value_list))
