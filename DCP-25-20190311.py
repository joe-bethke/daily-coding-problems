"""
This problem was asked by Facebook.
Implement regular expression matching with the following special characters:
. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and
returns whether or not the string matches the regular expression.
For example, given the regular expression "ra." and the string "ray", your function should return true.
The same regular expression on the string "raymond" should return false.
Given the regular expression ".*at" and the string "chat", your function should return true.
The same regular expression on the string "chats" should return false.
"""


def match(value, regex):
    if not value:
        return regex == "*"
    wild = False
    for index, char in enumerate(value):
        if len(regex) <= index:
            return wild
        wild = regex[index] == "*"
        if wild:
            index -= 1
        if regex[index] != char and regex[index] != "." and not wild:
            return False
    return True

print(match("ray", "ra."))
print(match("raymond", "ra."))
print(match("chat", ".*at"))
print(match("chats", ".*at"))
print(match("chats", "*"))
print(match("*", "*"))
print(match("ab", ".."))
print(match("", "bad"))
