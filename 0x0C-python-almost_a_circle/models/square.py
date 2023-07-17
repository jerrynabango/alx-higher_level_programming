#!/usr/bin/python3
"""Square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Indicates a string representation of a dictionary"""
        return """[{}] ({}) {}/{} - {}""".format(self.__class__.__name__,
                                                 self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Getter for the size of the object"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Defines setter for the instance size
        Instance: width, height
        """
        self.width = self._validate('width', value)
        self.height = self.width

    def update(self, *args, **kwargs):
        """updates the size of the image with the given parameters"""
        attr = ('id', 'size', 'x', 'y')
        if args and len(args) > 0:
            for squre in range(len(args)):
                if squre > 0 and squre <= 3:
                    setattr(self, attr[squre], args[squre])
                elif squre == 0:
                    self.__init__(self.size, self.x, self.y, args[squre])
        else:
            for key, value in kwargs.items():
                if key in attr:
                    if key == 'id':
                        self.__init__(self.size, self.x, self.y, value)
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        """Converts to a dictionary"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}
