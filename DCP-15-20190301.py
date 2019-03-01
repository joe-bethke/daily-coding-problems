"""
This problem was asked by Facebook.
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
import random


def stream():
    for i in range(random.randint(1000, 100000)):
        yield i


def solve(stream):
    value = None
    for idx, stream_value in enumerate(stream):
        if idx == 0:
            value = stream_value
        elif random.randint(1, idx + 1) == 1:
            value = stream_value
    return value


print(solve(stream()))
