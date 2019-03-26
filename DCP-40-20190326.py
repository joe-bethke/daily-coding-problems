"""
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer,
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""
from collections import Counter


def solve(array):
    return next(i for i, count in Counter(array).items() if count != 3)

print(solve([6, 1, 3, 3, 3, 6, 6]))
print(solve([13, 19, 13, 13]))

