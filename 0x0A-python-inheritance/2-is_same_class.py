#!/usr/bin/python3
"""Function returns True if object is same as specified class"""

def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class, False if not
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
