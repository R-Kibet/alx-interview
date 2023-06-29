#!/usr/bin/python3
""" pascal triangle"""


def pascal_triangle(n):
    """main  function of the project"""

    lst = [[1]*(i+1) for i in range(n)]

    if (n <= 0):
        return []

    for i in range(n):
        for j in range(1, i):
            lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
    return lst
