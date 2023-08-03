#!/usr/bin/python3
""" n queens chess game program"""

from sys import argv, exit


def nqueens(n):
    """
    puzzle is the challenge of
    placing N non-attacking queens on an N×N chessboard
    N >= 4 must be greater than 4
    N == int must be a numer
    """

    res = []
    board = [-1] * n

    def backtrack(ind):
        """backtrack algorithm"""

        ln = len(board)
        if ind == ln:
            res.append(board[:])
            return
        for i in range(ln):
            board[ind] = i
            if valid(ind):
                backtrack(ind + 1)

    def valid(n):
        """ chack positions is empty and no coalition"""
        for i in range(n):
            if abs(board[i] - board[n]) == n - i:
                return False
            if board[i] == board[n]:
                return False
        return True

    def moves(res):
        """ moves on the board"""
        current = []
        for q in res:
            bord = []
            for row, col in enumerate(q):
                bord.append([row, col])
            current.append(bord)
        return current

    backtrack(0)
    return moves(res)


if __name__ == "__main__":
    if len(argv) < 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)
    else:
        result = nqueens(n)
        for row in result:
            print(row)
