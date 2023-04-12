#!/usr/bin/python3
"""A Function that returns True if the object is the same as specified class"""


def is_same_class(obj, a_class):
    """This returns True if obj is exactly an instance of a_class, and False if not
     Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
