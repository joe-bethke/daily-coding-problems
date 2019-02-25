"""
This problem was asked by Twitter.
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
import string
from random import choice, randint


def solve(s, a):
    search_s = s.lower()
    yield from [result for result in a if result.lower().startswith(search_s)]
    # yield from [result for result in preprocessing(s, a) if result.lower().startswith(search_s)]


def preprocessing(s, a):
    # this doesn't seem faster...
    if not s or not a:
        raise ValueError("Either the given string or word list is empty.")
    alphabet_dict = {char: list() for char in string.ascii_lowercase}
    for word in a:
        if word:
            alphabet_dict[word.lower()[0]].append(word)
    return alphabet_dict[s.lower()[0]]


x = ["".join(choice(string.ascii_letters) for _ in range(randint(0, 12))) for _ in range(1000)]
# print(x)
# print(list(solve('a', x)))
solve('a', x)