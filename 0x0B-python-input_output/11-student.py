#!/usr/bin/python3
"""Defines a class Student."""


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
        """Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes name contained
        in the list must be retrieved.
        Args:
            attrs (list): Attributes to represent.
        """
        if (type(attrs) == list and
                all(type(nums) == str for nums in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.
        Args:
            json: A dictionary key/value that replaces attributes.
        """
        for i, j in json.items():
            setattr(self, i, j)
