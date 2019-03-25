"""
This problem was asked by Facebook.
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is
unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second,
and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
"""


def solve(walls):
    fill = 0
    for n in range(2, len(walls)):
        fill_to = min(walls[0:(n + 1)])
        height = walls[n - 1]
        if fill_to > height:
            fill += (fill_to - height)
    print(fill)
    return fill

assert solve([2, 1, 2]) == 1, "Example Case"
assert solve([3, 0, 1, 3, 0, 5]) == 8, "Example Case"
assert solve([3, 0, 1, 3, 0]) == 5, "Fill based on inner heights"
assert solve([0, 2, 5, 2, 0]) == 0, "All falls from center"
assert solve([1, 5, 4, 5, 1]) == 1, "Fill based on inner heights"
