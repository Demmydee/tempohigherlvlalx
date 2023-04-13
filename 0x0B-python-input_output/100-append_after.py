#!/usr/bin/python3
"""A function that inserts line of text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text to a file after each line containing a specific string.
    Args:
        filename : Name of file.
        search_string : String to search for in the file.
        new_string : String to insert.
    """
    txt = ""
    with open(filename) as read_file:
        for line in read_file:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, mode="w") as write_file:
        write_file.write(txt)
