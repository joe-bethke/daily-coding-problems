"""
This problem was asked by Apple.
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

from time import sleep


def schedule(func, after_milliseconds, *args, **kwargs):
    sleep(after_milliseconds / 1000)  # sleep takes an argument in seconds
    return func(*args, **kwargs)


def test(x, y=1):
    return x**y


print(schedule(test, 10000, 2, y=2))
