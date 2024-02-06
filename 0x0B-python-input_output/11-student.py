#!/usr/bin/python3
"""Defines student"""


class Student:
    """
    represents class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name(str): student first name
            last_name(str): student last name
            age (int): student age

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves dictionary representation of student
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces attributes of student instance
        """
        for m, n in json.items():
            setattr(self, m, n)
