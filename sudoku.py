import itertools
from random import sample, choice
import numpy as np
import unittest


class Sudoku:

    """
    A 9x9 array
    Can check if the sudoku is solved correctly
    Blank spaces in sudoku should be filled with -1
    A filled sudoku represents a sudoku with all values filled in
    A solved sudoku is a filled sudoku where all rows, column, and blocks contain only 1 of each value between 1 and 9
    """

    _block_indices = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    _valid_axis = set(range(1, 10))

    def __init__(self, array):
        if not len(array) == 9 and not all(len(row) == 9 for row in array):
            raise ValueError("Sudokus must be of the shape (9, 9)")
        self._index_combinations = np.array([list(itertools.product(row_indices, column_indices))
                                             for row_indices, column_indices in
                                            itertools.product(self._block_indices, self._block_indices)])
        self._array = np.array(array)

    def __repr__(self):
        return self.rows.__repr__()

    def __str__(self):
        return self.rows.__str__()

    def __iter__(self):
        return iter(self._array)

    def __getitem__(self, item):
        return self._array[item]

    def __setitem__(self, item, value):
        self[item] = value

    @classmethod
    def blank_sudoku(cls):
        return Sudoku([[-1 for _ in range(9)] for _ in range(9)])

    @classmethod
    def random_filled_sudoku(cls):
        # Randomly generate a sudoku - may not be valid
        return Sudoku([sample(cls._valid_axis, 9) for _ in range(9)])

    @classmethod
    def random_solved_sudoku(cls):
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
    def index_loop(self):
        for column in range(9):
            for row in range(9):
                yield row, column

    @property
    def rows(self):
        return self._array

    @property
    def columns(self):
        return self._array.transpose()

    @property
    def blocks(self):
        """
        block indices:
           0 1 2 3 4 5 6 7 8   column indices
           _____ _____ _____
        0 |     |     |     |
        1 |  0  |  1  |  2  |   block indices
        2 |_____|_____|_____|
        3 |     |     |     |
        4 |  3  |  4  |  5  |
        5 |_____|_____|_____|
        6 |     |     |     |
        7 |  6  |  7  |  8  |
        8 |_____|_____|_____|
        row indices
        """
        return np.array([[self._array[x][y] for x, y in combinations] for combinations in self._index_combinations])

    @property
    def is_filled(self):
        # Check if there are any blanks (-1) in the sudoku
        return not any(-1 in row for row in self)

    @property
    def is_solved(self):
        # The sudoku is correct - no repeated integers accross all rows, columns and blocks
        if not self.is_filled:
            return False
        return all(all(set(row) == self._valid_axis for row in axis) for axis in (self, self.columns, self.blocks))

    def block_index(self, row, column):
        return int(column // 3 + ((row // 3) * 3))

    def row_column_block(self, row, column):
        return self[row], self.columns[column], self.block_index(row, column)

    def affected_blocks(self, row, column):
        return {self.block_index(row, n) for n in range(9)} + {self.block_index(n, column) for n in range(9)}

    def solve(self):
        while not self.is_solved:
            solveable = False  # If no value is changed in this loop - the sudoku in not solveable
            for row_idx, column_idx in self.index_loop:
                row = self[row_idx]
                column = self.columns[column_idx]
                blocks = self.affected_blocks(row_idx, column_idx)
                
                possible_inputs = self._valid_axis - set(np.concatenate([row, column, block]))
                if len(possible_inputs) == 1:
                    # Fill in the spot with the value in the set
                    assert self[row_idx][column_idx] == -1
                    value = next(iter(possible_inputs))
                    self[row_idx][column_idx] = value
                    print(value, "At {r},{c}".format(r=row_idx, c=column_idx))
                    solveable = True
            if not solveable:
                raise ValueError("This sudoku is not solveable!")
        return self


class TestSudoku(unittest.TestCase):

    def test_random_solved_sudoku_is_solved(self):
        sudoku = Sudoku.random_solved_sudoku()
        # print(sudoku)
        self.assertTrue(sudoku.is_solved)

    def test_random_filled_sudoku(self):
        sudoku = Sudoku.random_filled_sudoku()
        # print(sudoku)
        self.assertIsInstance(sudoku, Sudoku)

    def test_solve(self):
        # sudoku = Sudoku.random_solved_sudoku()
        # sudoku[0][0] = -1
        # sudoku = Sudoku.random_filled_sudoku()
        sudoku = Sudoku([[3,  -1, -1,     9, -1, -1,     2, -1, -1],
                         [-1,  5, -1,    -1, -1,  1,    -1,  7, -1],
                         [-1, -1,  8,    -1,  4, -1,    -1, -1,  6],

                         [ 9, -1, -1,     7, -1, -1,     4, -1, -1],
                         [-1, -1, -1,    -1,  6, -1,    -1, -1, -1],
                         [-1, -1,  2,    -1, -1,  5,    -1,  1, -1],

                         [ 4, -1, -1,    -1,  8, -1,    -1, -1, -1],
                         [-1, -1,  7,     3, -1, -1,    -1, -1, -1],
                         [-1,  1, -1,    -1, -1, -1,    -1, -1,  5]])
        self.assertTrue(sudoku.solve().is_solved)


if __name__ == "__main__":
    unittest.main()
