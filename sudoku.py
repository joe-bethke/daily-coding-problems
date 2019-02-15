import itertools
from random import sample
import numpy as np

perfect_sudoku = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [4, 5, 6, 7, 8, 9, 1, 2, 3],
                           [7, 8, 9, 1, 2, 3, 4, 5, 6],
                           [2, 3, 4, 5, 6, 7, 8, 9, 1],
                           [5, 6, 7, 8, 9, 1, 2, 3, 4],
                           [8, 9, 1, 2, 3, 4, 5, 6, 7],
                           [3, 4, 5, 6, 7, 8, 9, 1, 2],
                           [6, 7, 8, 9, 1, 2, 3, 4, 5],
                           [9, 1, 2, 3, 4, 5, 6, 7, 8]])

# all combinations of indices in a sudoku array
index_combinations = [list(itertools.product(*block))
                      for block in
                      itertools.product([[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[0, 1, 2], [3, 4, 5], [6, 7, 8]])]

good_axis = set(range(1, 10))


def check_sudoku(original_sudoku):
    reshaped_sudoku = original_sudoku.transpose()
    sudoku_blocks = [[original_sudoku[x][y] for x, y in combination] for combination in index_combinations]
    return all(all(set(axis) == good_axis for axis in sudoku)
               for sudoku in (original_sudoku, reshaped_sudoku, sudoku_blocks))


print(check_sudoku(perfect_sudoku))
row_length = list(range(1, 10))
sudoku = np.array([sample(row_length, 9) for __ in range(9)])
print(sudoku)
for x in range(1000000):
    sudoku = np.array([sample(row_length, 9) for __ in range(9)])
    if check_sudoku(sudoku):
        print(x)
