#!/usr/bin/python3
"""
Class square that inherits rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initaliazes square
        """
        super().__init__(size, size, id, x, y)

        @property
        def size(self):
            """
            gets size of square
            """
            return self.width

        @size.setter
        def size(self, value):
            self.width = value
            self.height = value

        def __str__(self):
            """
            prints square repreesntaion
            """
            return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                    self.y, self.width)
        
