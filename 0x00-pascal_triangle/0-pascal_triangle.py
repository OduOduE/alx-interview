#!/usr/bin/python3
""" A script that returns a list of lists of integers
representing the Pascals triangle of n.
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascals triangle of n
    """
    if n <= 0:
        return []

    triang = [[1]]

    for numb in range(1, n):
        prevRow = triang[-1]
        currRow = [1]
        for col in range(1, numb):
            currRow.append(prevRow[col-1] + prevRow[col])
        currRow.append(1)
        triang.append(currRow)

    return triang
