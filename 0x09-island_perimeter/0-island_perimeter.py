#!/usr/bin/python3
"""
calculate the perimeter of a single island
in a grid, where the grid represented by a
2D array of integers
"""


def island_perimeter(grid):
    """
    create a function that returns the perimeter
    of the island described in grid
    """
    water = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    water += 1
                if j == 0 or grid[i][j - 1] == 0:
                    water += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    water += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    water += 1
    return water