import numpy as np
import time


def count_neighbors(grid, row, col):
    area = grid[row-1:row+2, col-1:col+2]
    return np.sum(area) - grid[row, col]

def get_next_grid(grid):
    grid_with_border = np.pad(grid, 1, mode="constant")
    new_grid = np.zeros_like(grid)