#!/usr/bin/python3
"""A class that inherits from the parent (list) class"""


class MyList(list):
    """A class that inherits from the parent (list) class"""

    def print_sorted(self):
        """Prints a list in ascending and sorted order."""
        print(sorted(self))
