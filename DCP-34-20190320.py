"""
This problem was asked by Quora.
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere
in the word. If there is more than one palindrome of minimum length that can be made,
return the lexicographically earliest one (the first one alphabetically).
For example, given the string "race", you should return "ecarace",
since we can add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three letters,
but "ecarace" comes first alphabetically.
As another example, given the string "google", you should return "elgoogle"
"""
from itertools import combinations


def is_palindrome(string):
    length = len(string)
    first = string[:(length // 2) + 1] if length % 2 else string[:length // 2]
    second = "".join(reversed(string[(len(string) // 2):]))
    # print(first, second)
    return first == second


def solve(string):
    if is_palindrome(string):
        return string
    length = len(string)
    # Create a list of all possible palindrome combinations
    # Sort the list, first by order, than alphabetically
    # return the first value in the list (fewest characters, first alphabetically)
    return sorted((character_combination
                   for addition in combinations(range(length + 1), r=2)
                   for character_combination in ((string + "".join(reversed(string[slice(*addition)]))),
                                                 ("".join(reversed(string[slice(*addition)])) + string),
                                                 (string + string[slice(*addition)]),
                                                 (string[slice(*addition)] + string))
                   if string in character_combination and is_palindrome(character_combination)),
                  key=lambda char_combo: (len(char_combo), char_combo))[0]

print(solve("goog"))
print(solve("race"))
print(solve("google"))
print(solve("afdasdfasd"))
print(solve("fasdkfasjdfhasdfjasdfasdfasdfasdfjarqwerqwerw"))
print(solve("zzrz"))
