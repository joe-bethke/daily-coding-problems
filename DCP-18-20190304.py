"""
This problem was asked by Google.
Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space.
You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.
"""


def solve(numbers, k):
    if k <= 0 or k > len(numbers):
        raise ValueError("k param must be: 1 <= k <= len(numbers)")
    return [max(numbers[low:high]) for low, high in zip(range((len(numbers) - k) + 1), range(k, len(numbers) + 1))]


def print_solve(numbers, k):
    for low, high in zip(range((len(numbers) - k) + 1), range(k, len(numbers) + 1)):
        print(max(numbers[low:high]))


print(solve([10, 5, 2, 7, 8, 7], 5))
print(solve([-3, -5, -6, float('inf'), 44, 34, 0, 0, 0, -1, float('-inf'), 14234], 7))
