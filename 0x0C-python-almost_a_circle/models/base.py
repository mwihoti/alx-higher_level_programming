#!/usr/bin/python3
"""
Define Class Base
"""
import json


class Base:

    """
    class base with a private class
    _nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes base
        Args:
            id(int): base id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
         returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        returns JSON string representation of list_objs to a file:
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsfile:
            if list_objs is None:
                jsfile.write("[]")
            else:
                list_dict = [k.to_dictionary() for k in list_objs]
                jsfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """

        if dictionary and dictionary != ():
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsfile:
                list_dict = Base.from_json_string(jsfile.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
