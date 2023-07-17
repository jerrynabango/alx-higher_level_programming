#!/usr/bin/python3
"""First Rectangle"""
from .base import Base


class Rectangle(Base):
    """Defines a rectangle with a specified dimensions"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def _validate(attr, value):
        """Validate a value against a given attribute value"""
        if type(value) != int:
            raise TypeError(f'{attr} must be an integer')
        if (attr == 'width' or attr == 'height') and value <= 0:
            raise ValueError(f'{attr} must be > 0')
        if (attr == 'x' or attr == 'y') and value < 0:
            raise ValueError(f'{attr} must be >= 0')
        return value

    @property
    def width(self):
        """Getter for private width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Defines the setter for the width attribute
        private attribute: __width
        """
        self.__width = self._validate('width', value)

    @property
    def height(self):
        """Getter for private height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Defines the setter for the height attribute
        private attribute: __height
        """
        self.__height = self._validate('height', value)

    @property
    def x(self):
        """Getter for private x"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Defines setter for the x attribute
        private attribute: __x
        """
        self.__x = self._validate('x', value)

    @property
    def y(self):
        """Getter for private y"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Defines setter for the y attribute
        private attribute: __y
        """
        self.__y = self._validate('y', value)

    def area(self):
        """Calculates area of the object"""
        return (self.width * self.height)

    def display(self):
        """Displays the Rectangle instance"""
        print("\n" * self.y, end="")
        for w in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def update(self, *args, **kwargs):
        """Update the current state of the widget"""
        attr = ('id', 'width', 'height', 'x', 'y')
        if args and len(args) > 0:
            for rect in range(len(args)):
                if rect > 0 and rect <= 4:
                    setattr(self, attr[rect], args[rect])
                elif rect == 0:
                    super().__init__(args[rect])
        else:
            for key, value in kwargs.items():
                if key in attr:
                    if key == 'id':
                        super().__init__(value)
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Indicates a string representation of a dictionary"""
        return """[{}] ({}) {}/{} - {}/{}""".format(self.__class__.__name__,
                                                    self.id, self.x, self.y,
                                                    self.width, self.height)

    def to_dictionary(self):
        """Converts to a dictionary"""
        return {'x': self.x, 'y': self.y,
                'id': self.id, 'width': self.width, 'height': self.height}
