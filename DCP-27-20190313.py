"""
This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
"""

openers = ("(", "[", "{")
closers = (")", "]", "}")
opener_to_closer = dict(zip(openers, closers))


def is_valid(s):
    closer_order = list()
    for char in s:
        if char in openers:
            closer_order.append(opener_to_closer[char])
        if char in closers:
            if closer_order and char == closer_order[-1]:
                closer_order.pop(-1)
            else:
                return False
    return not closer_order  # If the closer order is empty, return True

print(is_valid("([])[]({})"))
print(is_valid("([)]"))
print(is_valid("((()"))
print(is_valid("]]]"))
print(is_valid("ab[]ad[]d{fasdf(fasdf)fa}"))
print(is_valid("ab[]ad[]d{fasdf(fasdf)fa"))