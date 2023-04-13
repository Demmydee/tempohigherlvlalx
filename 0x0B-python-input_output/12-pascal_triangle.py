#!/usr/bin/python3
"""Pascal triangle function."""


def pascal_triangle(n):
    """A function that returns a list of lists of integers representing
    the pascal's triangle.
    Args:
        n : List of Integers.
    """
    if n <= 0:
        return []

    i = [[1]]
    while len(i) != n:
        j = i[-1]
        k = [1]
        for x in range(len(j) - 1):
            k.append(j[x] + j[x + 1])
        k.append(1)
        i.append(k)
    return i
