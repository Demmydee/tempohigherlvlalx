#!/usr/bin/python3
"""Defines Python class-to-JSON function."""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization of\n
an object with simple data structure."""

    return obj.__dict__
