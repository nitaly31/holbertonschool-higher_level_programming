#!/usr/bin/python3
''' And now, the Square! '''


from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Class Square inherits from Rectangle '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Class constructor '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' Size getter '''
        return self.width

    @size.setter
    def size(self, value):
        ''' Size setter '''
        self.width = value
        self.height = value

    def __str__(self):
        ''' The overloading __str__ method '''
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))
