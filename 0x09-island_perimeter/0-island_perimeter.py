#!/usr/bin/python3
"""
finding island perimeter
"""


def island_perimeter(grid):
    """ function to calculate the perimeter"""
    visit = set()

    def dfs(i, j):
        """ depth first search function """

        # first case chack out of bounds
        if i >= len(grid) or j >= len(grid[0]) or \
           i < 0 or j < 0 or grid[i][j] == 0:
            return 1

        # if visit same position
        if (i, j) in visit:
            return 0

        visit.add((i, j))
        # dfs moves in 4 directions
        perimeter = dfs(i, j + 1)
        perimeter += dfs(i + 1, j)
        perimeter += dfs(i, j - 1)
        perimeter += dfs(i - 1, j)

        return perimeter

    # find a section that is not wwater so we start search
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # check if its not 0
            if grid[i][j]:
                return dfs(i, j)
