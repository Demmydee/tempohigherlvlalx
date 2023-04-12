#!/usr/bin/python3
"""This function appends a string to a text file"""


def append_write(filename="", text=""):
    """This function appends a string to text file(UTF8) \n
        and prints the number of characters added
    Args:
        filename: File to be written.
        text: Lines of Strings to be added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
