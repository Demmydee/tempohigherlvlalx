#!/usr/bin/python3
"""This function reads a text file"""


def read_file(filename=""):
    """This function reads a text file(UTF8) and prints to stdout
    Args:
        filename: File to be read
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
