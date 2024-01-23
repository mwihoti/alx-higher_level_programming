#!/usr/bin/python3

"""cordinates of a square"""


class Square:
    def __init__(self, size=0, position=0):
        """Initializing atrtribute
        args:
            position - square position
            size- to be int"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrive private size attribute"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """property setter
        args:
            value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve private position instance"""
        return(self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(elem, int) for elem in value) or
                not all(elem >= 0 for elem in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
