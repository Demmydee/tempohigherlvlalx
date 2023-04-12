#!/usr/bin/python3
"""Defines object attributes lookup function"""


def lookup(obj):
    """A function that returns a list of available attributes"""
    return (dir(obj))
