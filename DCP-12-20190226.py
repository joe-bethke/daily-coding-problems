"""
This problem was asked by Amazon.
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""
from itertools import combinations, combinations_with_replacement, permutations


def solve_onetwos(steps, inputs={1, 2}):
    # only works with ones and twos
    num_inputs_by_input = {i: steps // i for i in inputs}
    full_inputs = [i for i, n in num_inputs_by_input.items() for _ in range(n)]
    solutions = list()
    for number_of_inputs in range(steps + 1):
        for offset in range(len(full_inputs)):
            ins = full_inputs[offset:(number_of_inputs + offset)]
            solutions.extend([permutation for permutation in set(permutations(ins, number_of_inputs)) if sum(permutation) == steps])
    return solutions


def solve(steps, inputs={1, 2}):
    # Incredibly slow when steps > 8
    # works with all inputs
    num_inputs_by_input = {i: steps // i for i in inputs}
    full_inputs = [i for i, n in num_inputs_by_input.items() for _ in range(n)]
    all_permutations = [set(permutations(full_inputs, n)) for n in range(1, steps + 1)]
    return set([tuple(permutation)
                for n_permutations in all_permutations
                for permutation in n_permutations
                if sum(permutation) == steps])

print(solve_onetwos(4))
print(solve(7, inputs={1, 3, 4}))

