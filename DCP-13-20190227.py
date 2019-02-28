"""
This problem was asked by Amazon.
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def solve(s, k):
    subs = list()
    for i, char in enumerate(s):
        sub = char
        next_chars = s[i + 1:]
        for next_char in next_chars:
            if len(set(sub)) <= k:
                sub += next_char
            if len(set(sub)) > k:
                sub = sub[:-1]
                break
        subs.append(sub)
    solution = max((sub for sub in subs), key=lambda s: len(s))
    print(solution)
    return solution

solve('abcbaasdfasdfsffffff', 5)
solve('abcdeabcdfeabcdeabcdef', 5)
