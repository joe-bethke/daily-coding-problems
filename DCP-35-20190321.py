"""
This problem was asked by Google.
Given an array of strictly the characters 'R', 'G', and 'B',
segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last.
You can only swap elements of the array.
Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""


def solve(rgbs):
    counts = {"R": 0, "G": 0, "B": 0}
    sorter = {"R": list(), "G": list(), "B": list()}
    for value in rgbs:
        counts[value] += 1
    return [rgb for rgb in ("R", "G", "B") for _ in range(counts[rgb])]


def solve_inplace(rgbs):
    counts = {"R": 0, "G": 0, "B": 0}
    for value in rgbs:
        counts[value] += 1
    for idx, value in enumerate(rgbs):
        rgbs[idx] = ("R" if idx < counts["R"] else
                     "G" if counts["R"] <= idx < (counts["G"] + counts["R"]) else
                     "B")
    print(rgbs)

print(solve(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
solve_inplace(['G', 'B', 'R', 'R', 'B', 'R', 'G'])
