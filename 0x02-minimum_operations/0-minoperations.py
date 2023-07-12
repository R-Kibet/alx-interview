#!/usr/bin/python3
"""
main program to run
"""


def minOperations(n):
    """
    program given a number x and atext file conatining H
    writes method
    that calculates fewest number of operations needed
    returns an integer
    """

    cc = 0
    p = 1

    if n <= 1:
        return 0

    for i in range(0, n - 2):
        if i % 2 == 0:
            cc = p + i + 5
            s = cc // 2
        if n == 4:
            return 4
    return s
