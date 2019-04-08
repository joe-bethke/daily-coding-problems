"""
This problem was asked by Facebook.
Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input,
write a function that shuffles a deck of cards represented as an array using only swaps.
It should run in O(N) time.
Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""
from random import randint
from copy import deepcopy


def solve(cards, randomizer=randint, k=52):
    card_order = [card for card in cards]
    for idx in range(52):
        replace_idx = (idx + randint(1, k)) % 52
        cards[idx], cards[replace_idx] = cards[replace_idx], cards[idx]
    return deepcopy(cards)

cards = list(range(52))
shuffles = list()
for _ in range(100000):
    shuffle = solve(cards)
    assert shuffle not in shuffles, (shuffle, next(s for s in shuffles if s == shuffle))
    shuffles.append(shuffle)

