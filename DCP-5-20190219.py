"""
This problem was asked by Jane Street.
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def tup(*args):
    return tuple(args)


def car(pair):
    return pair(tup)[0]


def cdr(pair):
    return pair(tup)[-1]


a = tuple([1, 2, tuple(), tup])  # 3
b = set([tup, tup, cdr, car])  # 4

print(cons(a, b)(tup))
print(car(cons(a, b)))
print(cdr(cons(a, b)))
