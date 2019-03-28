"""
This problem was asked by Google.
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.
Integers can appear more than once in the list. You may assume all numbers in the list are positive.
For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""
from random import randint
from itertools import combinations


def solve(numbers, value):
    return next((subset for n in range(1, len(numbers)) for subset in combinations(numbers, n) if sum(subset) == value),
                None)


print(solve([12, 1, 61, 5, 9, 2], 24))
print(solve([12, 1, 61, 5, 9, 2, 24], 24))
print(solve([randint(0, 10) for _ in range(100)], 54))
