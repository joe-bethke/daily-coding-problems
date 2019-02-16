"""
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""
from random import randint
import math

x = [1, 2, 3, 4, 5]


def product(lis):
    product = 1 if lis else 0
    for i in lis:
        product *= i
    return product


def solve(*args):
    x = [product(args[n + 1:] + args[:n]) for n in range(len(args))]
    print(x)
    return x


solve(0)
solve(1, 2)
solve(3, 2, 1)
solve(1, 2, 3, 4, 5)
solve(*[randint(0, 20) for _ in range(6)])
solve(0, 1, 0, 0, 0)
solve(0, 1, 2, 3, 4)
solve(0, 1, 2, 3, 0)
solve(1, 2, 0, 0, 4)