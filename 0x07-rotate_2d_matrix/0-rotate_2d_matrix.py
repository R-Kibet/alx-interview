#!/usr/bin/python3

"""
rotating a 2D matrix using in place method
"""


def rotate_2d_matrix(matrix):

    """
    program that transforms the matrix
    """
    lft = 0
    r = len(matrix) - 1

    while lft < r:
        for i in range(r - 1):
            top = lft
            bottom = r

            """save the topleft"""
            topLeft = matrix[top][lft + i]

            """move bottom left into top left"""
            matrix[top][lft + i] = matrix[bottom - i][lft]

            """move bottom right into bottom left"""
            matrix[bottom - i][lft] = matrix[bottom][r - i]

            """move top right to bottom right """
            matrix[bottom][r - i] = matrix[top + i][r]

            """move top left into top right"""
            matrix[top + i][r] = topLeft

            """update pointers"""
            lft += 1
            r -= 1
