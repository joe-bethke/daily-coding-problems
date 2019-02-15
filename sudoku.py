import itertools
from random import sample, choice
import numpy as np
import unittest


class Sudoku:

    _block_indices = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    _valid_axis = set(range(1, 10))

    def __init__(self, array):
        if not len(array) == 9 and not all(len(row) == 9 for row in array):
            raise ValueError("Sudokus must be of the shape (9, 9)")
        self._index_combinations = [itertools.product(row_indices, column_indices)
                                    for row_indices, column_indices in
                                    itertools.product(self._block_indices, self._block_indices)]
        self._array = np.array(array)
        self._columns = self._array.transpose()
        self._blocks = np.array([[self._array[x][y] for x, y in combination]
                                 for combination in self._index_combinations])

    def __repr__(self):
        return self.array.__repr__()

    def __str__(self):
        return self.array.__str__()

    def __iter__(self):
        return iter(self.array)

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, item, value):
        self[item] = value

    @classmethod
    def random_sudoku(cls):
        # Randomly generate a sudoku - may not be valid
        return Sudoku([sample(cls._valid_axis, 9) for _ in range(9)])

    @classmethod
    def random_valid_sudoku(cls):
        # Randomly generate a valid sudoku
        # I don't think this is the only way to make a valid sudoku...
        initial_row = sample(cls._valid_axis, 9)
        sudoku = [initial_row]
        for row_number in range(1, 9):
            offset = (3 * row_number) % 9
            offset += int(row_number / 3)
            sudoku.append(initial_row[offset:] + initial_row[:offset])
        return Sudoku(sudoku)

    @property
    def array(self):
        # Makes the array read-only
        return self._array

    @property
    def columns(self):
        # array column values become rows
        return self._columns

    @property
    def blocks(self):
        # The 3x3 blocks of the 9x9 array
        return self._blocks

    @property
    def is_valid(self):
        # The sudoku is valid - no repeated integers accross all rows, columns and blocks
        return all(all(set(row) == self._valid_axis for row in axis) for axis in (self, self.columns, self.blocks))


class TestSudoku(unittest.TestCase):

    def test_random_valid_sudoku_is_valid(self):
        sudoku = Sudoku.random_valid_sudoku()
        # print(sudoku)
        self.assertTrue(sudoku.is_valid)

    def test_random_sudoku(self):
        sudoku = Sudoku.random_sudoku()
        # print(sudoku)
        self.assertIsInstance(sudoku, Sudoku)


if __name__ == "__main__":
    unittest.main()
