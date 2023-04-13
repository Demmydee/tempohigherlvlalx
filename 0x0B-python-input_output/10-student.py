#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """Defines a Student by public instance attributes."""

    def __init__(self, first_name, last_name, age):
        """Initializes student.
        Args:
            first_name (str): First name of student.
            last_name (str): Last name of student.
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student instance.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
