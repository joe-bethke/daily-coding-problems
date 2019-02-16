"""
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""
from itertools import combinations
from random import randint
from timeit import timeit

x = [10, 15, 3, 7]
k = 17


def n_squared(lis, value):
    # return n in map(sum, combinations(lis, 2))  # slower as the whole map objects is created
    return any(sum(combo) == value for combo in combinations(lis, 2))  # stops once condition is True


def n(lis, value):
    s = set(lis)
    return any(value - i in s for i in lis)


def test(f, value=100):
    if value > 100000:
        raise ValueError("Too high to test!")
    lis = list()
    while not f(lis, value):
        lis = [randint(0, 100000) for _ in range(100000)]


test(n, value=1421)  # fast AF
# test(n_squared)  # super slow
