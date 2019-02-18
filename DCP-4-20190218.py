"""
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""


def solve(lis):
    positive_ints = sorted({i for i in lis if i > 0})
    offset = min(positive_ints, default=0)
    return next(((n + offset) for n, i in enumerate(positive_ints) if (n + offset) != i),
                (max(positive_ints, default=0) + 1))


print(solve([3, 4, -1, 1, -2]))
print(solve([1, 2, 0]))
print(solve([1, 2, 3, 4, 7]))
print(solve([0, 0, 0, 0, 0, 0]))
print(solve([-1]))
print(solve([]))
print(solve([123412,34123412,341234,123412341,23423,412,3412341234,434,1234214,129804021]))
print(solve([1, 2, 3, 4, 4, 3, 2, 1]))
