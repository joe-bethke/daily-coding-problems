"""
This problem was asked by Google.
The edit distance between two strings refers to the minimum number of character insertions, deletions,
and substitutions required to change one string to the other.
For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
Given two strings, compute the edit distance between them.
"""


def solve(base, edit):
    return sum([1 for base_char, edit_char in zip(base, edit) if base_char != edit_char]) + abs(len(edit) - len(base))

print(solve("kitten", "sitting"))
print(solve("sitting", "kitten"))
print(solve("", "abcdef"))
print(solve("dog", "cat"))
print(solve("car", "cat"))