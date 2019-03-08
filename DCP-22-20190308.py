"""
This problem was asked by Microsoft.
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""
from random import randint
import re
from itertools import permutations, combinations


def solve_permutations(words, sentence):
    # handles duplicates
    return [word_combination
            for i in range(len(words) + 1)
            for word_combination in permutations(words, i)
            if "".join(word_combination) == sentence]


def solve_combinations(words, sentence):
    # handles duplicates
    # Does not handle substrings that may occur in several places throughout the sentence
    words = sorted(words, key=lambda word: sentence.index(word))
    start = next(idx for idx in range(len(words)) if sum(map(len, words[-idx:])) >= len(sentence))
    return [word_combination
            for i in range(start, len(words) + 1)
            for word_combination in combinations(words, i)
            if "".join(word_combination) == sentence]


def solve_faster_for_small_subs(words, sentence):
    # slightly faster for long word lists
    # Does not handle duplicates
    word_indices = {word: list(sub.start() for sub in re.finditer(word, sentence)) for word in words}
    multiple_words = [(word, index) for word, indices in word_indices.items() for index in indices]
    sorted_words_indices = sorted([word_index for word_index in multiple_words], key=lambda word_index: word_index[1])
    words = [word[0] for word in sorted_words_indices]
    start = next(idx for idx in range(len(words)) if sum(map(len, words[-idx:])) >= len(sentence))
    return [word_combination
            for i in range(start, len(words) + 1)
            for word_combination in combinations(words, i)
            if "".join(word_combination) == sentence]


thequickbrownfox = solve_permutations(['quic', 'k', 'he', 't', 'the', 'quick', 'brown', 'fox'], 'thequickbrownfox')
bedbathandbeyond = solve_permutations(['ath', 'b', 'beyond', 'bed', 'bath', 'bedbath', 'and', 'beyond'], 'bedbathandbeyond')
print(thequickbrownfox)
print(bedbathandbeyond)

# mystring = "microsoft"
# words = [mystring[randint(1, len(mystring)):randint(1, len(mystring))] for _ in range(100)]
# mystring_solved = solve(words, mystring)
# print(mystring_solved)
