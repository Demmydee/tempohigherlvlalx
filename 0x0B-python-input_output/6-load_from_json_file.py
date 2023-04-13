#!/usr/bin/python3
"""Calls a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """A function that creates an object from a JSON file."""
    with open(filename) as a_file:
        return json.load(a_file)
