#!/usr/bin/python3
"""Returns ana object represented by a JSON string."""
import json


def from_json_string(my_str):
    """Returns a python data structure object represented\n
by a JSON string."""

    return json.loads(my_str)
