import numpy as np
import time


def count_neighbors(grid, row, col):
    area = grid[row-1:row+2, col-1:col+2]
    return np.sum(area) - grid[row, col]

def get_next_grid(grid):
    grid_with_border = np.pad(grid, 1, mode="constant")
    new_grid = np.zeros_like(grid)
    
    for i in range(1, grid_with_border.shape[0] - 1):
        for j in range(1, grid_with_border.shape[1] - 1):
            # Getting the number of neighbors
            neighbors = count_neighbors(grid_with_border, i, j)

            if grid_with_border[i, j] == 1:  # If the cell is alive
                if neighbors == 2 or neighbors == 3:  # Stay alive
                    new_grid[i - 1, j - 1] = 1
            else:  # If the cell is dead
                if neighbors == 3:  # It becomes alive
                    new_grid[i - 1, j - 1] = 1

    return new_grid