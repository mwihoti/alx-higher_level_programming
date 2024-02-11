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
        super().__init__(size, size, x, y, id)

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

    def update(self, *args, **kwargs):
        """
        Update the class Square by adding the public method
        def update(self, *args, **kwargs) that assigns attributes
        """
        if args and len(args) != 0:
            l = 0
            for arg in args:
                if l == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif l == 1:
                    self.size = arg
                elif l == 2:
                    self.x =arg
                elif l == 3:
                    self.y = arg
                l += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    def to_dictionary(self):
        """
         returns the dictionary representation of a Square
         """
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }


    def __str__(self):
        """
        prints square repreesntaion
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width)
        
