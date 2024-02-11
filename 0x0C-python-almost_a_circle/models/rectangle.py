#!/usr/bin/python3
"""
Defines Rectangle that inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes Rectangle
        Args:
            width (int) : rectangle width
            height (int) : rectangle height
            x (int): x coordinate
            y (int): y coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def height(self):
        """
        gets rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """
        gets rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """
        gets x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        gets value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Area of rectactangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints # character
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
       """
       Prints rectangle with a formatted output
       """
       return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
               self.y, self.width, self.height)
