#!/usr/bin/python3
"""This function writes a string to a text file"""


def write_file(filename="", text=""):
    """This function writes a string to a text file(UTF8) and prints number of character written
    Args:
        filename: File to be written.
        text: Lines of Strings to be added.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
