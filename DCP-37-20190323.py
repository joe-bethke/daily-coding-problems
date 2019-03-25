""""
This problem was asked by Google.
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
You may also use a list or array to represent a set
"""
from itertools import combinations


def solve(item_set):
    power_set = [set(combo) for i in range(len(item_set) + 1) for combo in combinations(item_set, i)]
    print(power_set)
    return power_set

solve({1, 2, 3})
