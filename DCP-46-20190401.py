"""
This problem was asked by Amazon.
Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.
For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
"""


def is_palindrome(string):
    return len(string) >= 2 and "".join(reversed(string)) == string


def solve(string):
    # Create a generator of all substrings of length >= 2, with larger substrings first
    substrings = (string[start:start + offset]
                  for offset in range(len(string), 1, -1)
                  for start in range(1 + len(string) - offset))
    return next((substring for substring in substrings if is_palindrome(substring)), None)


print(solve("adsfasdfasdfaafasdfasdfasdf"))
print(solve("aabcdcb"))
print(solve("bananas"))
print(solve('cdaaio'))
print(solve("abcdefghijklmnopqrstuvwxyz"))
print(solve("racecar"))
print(solve("asdfasdfasdfasdfasdfaaaaaaaaaaaa"))
