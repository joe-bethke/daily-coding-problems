"""
This problem was asked by Facebook.
Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once.
You must buy before you can sell it.
For example, given [9, 11, 8, 5, 7, 10], you should return 5,
since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""
from random import randint


def lazy(func):
    def dec(*args, **kwargs):
        f = func(*args, **kwargs)
        print(f)
        return f
    return dec


@lazy
def solve(arr):
    """This does not handle all cases - works on the given test case though. works in linear time"""
    buy_index = 0
    sell_index = -1
    for index, (start_price, end_price) in enumerate(zip(arr, reversed(arr))):
        selling_index = -(index + 1)
        if start_price < arr[buy_index] and index < sell_index % len(arr):
            buy_index = index
        if end_price > arr[sell_index] and selling_index % len(arr) > buy_index:
            sell_index = selling_index
    return arr[sell_index] - arr[buy_index]


@lazy
def easy_solve(arr):
    """polynomial time, works always"""
    return max((sell_price - buy_price for buy_index, buy_price in enumerate(arr) for sell_price in arr[buy_index:]),
               default=0)

try:
    arr = [4, 100, 1, 90]
    s = solve(arr)
    es = easy_solve(arr)
    assert s == es, f"Edge case! solve() was off by {es - s}"
except AssertionError:
    print(f"solve() was off by {es - s}")


arr = [randint(1, 100000) for _ in range(1000)]
s = solve(arr)
es = easy_solve(arr)
assert s == es, f"Edge case! solve() was off by {es - s}"


arr = [randint(1, 100000000) for _ in range(100000)]
s = solve(arr)
es = easy_solve(arr)  # this arr is too large to solve in a short amount of time
assert s == es, f"Edge case! solve() was off by {es - s}"
