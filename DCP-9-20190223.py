"""
This problem was asked by Airbnb.
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?
"""
from hypothesis import given
from hypothesis.strategies import lists


# @given(lists([-1, 0, 1, 10]))
def solve(lis):
    if not len(lis) % 2:
        # odd length - insert a 0 at the middle of the list
        lis[len(lis) // 2: len(lis) // 2] = [0]
    return max((sum([value for idx, value in enumerate(lis) if not idx % 2 and value > 0]),
                sum([value for idx, value in enumerate(lis) if idx % 2 and value > 0])))

x = [2, 4, 6, 7, 5]
y = [5, 1, 1, 5]
z = [10, -1, -1, 4, 5, 11]

print(solve(x))
print(solve(y))
print(solve(z))

