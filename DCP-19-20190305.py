"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
return the minimum cost which achieves this goal.
"""
import numpy as np
from random import sample, randint


# colors = {'red': 2, 'blue': 3, 'green': 4, 'purple': 2.5}  # cost per surface area unit by color
# houses = [1200, 2500, 1350, 1784, 2010, 3050]  # Surface area to paint by house in the row

# matrix = np.array([[ar * color_cost for color_cost in colors.values()] for ar in houses])
# print(matrix)

costs = {randint(1, 20) for _ in range(10)}
matrix = np.array([list(sample(costs, 4)) for _ in range(4)])
print(matrix)


def solve(matrix):
    row_selections = list()
    for start_row in range(len(matrix)):
        no_select = (None, None)  # indices that cannot be chosen based on previous index choices
        start_idx, last_idx = no_select
        selections = [None] * len(matrix)  # best combination at this start row
        # create the row index order based on the start row
        row_order = list(range(start_row, len(matrix))) + list(range(start_row))
        for row_number in row_order:
            row = matrix[row_number]
            # Sort by the cost in each value of the row
            sorted_values = sorted(enumerate(row), key=lambda x: x[1])
            if row_number == start_row - 1:
                # last row in this iteration
                no_select = (start_idx, last_idx)
            # Pick the best index, cost combination based on cost
            chosen_idx, chosen_cost = min(sorted_values,
                                          key=lambda values: (values[1]
                                                              if values[0] not in no_select else
                                                              float('inf')))
            if row_number == start_row:
                # First selection
                start_idx = chosen_idx
            selections[row_number] = chosen_cost
            last_idx = chosen_idx
            if row_number == len(matrix) - 1:
                # last row in matrix, next row is the top of the matrix
                if start_row == 1:
                    # If we started at row 1, then the top of the matrix still cannot select the start idx
                    no_select = (start_idx, None)
                else:
                    # otherwise, top of matrix has no constraints
                    no_select = (None, None)
            else:
                no_select = (None, last_idx)
        row_selections.append(selections)
    return min(row_selections, key=lambda selection: sum(selection))

solution = solve(matrix)
print(solution)
