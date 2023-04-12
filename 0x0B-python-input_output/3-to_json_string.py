#!/usr/bin/python3
"""A function that returns the JSON representation of an object."""
import json


def to_json_string(my_obj):
    """This returns the JSON representation of an object(string)."""
    return json.dumps(my_obj)
