#!/usr/bin/python3
"""Defines class student that defines a student"""


class Student:
    """class student """
    def __init__(self, first_name, last_name, age):
        """
        initializes student

        Args:
            first_name: first name of student
            last_name: last name of the student
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dictionary representation of a student"""
        return self.__dict__
