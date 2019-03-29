"""
This problem was asked by Amazon.
Implement a stack that has the following methods:
push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack,
then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack,
then it should throw an error or return null.
Each method should run in constant time.
"""


class Stack(list):

    @property
    def max(self):
        return max(self)

    def push(self, value):
        self.insert(0, value)

    def pop(self):
        return super(Stack, self).pop(0)

stack = Stack(range(3))
stack.pop()
stack.push(3)
m = stack.max
assert m == 3 and stack == [3, 1, 2]

stack = Stack(range(1, 5))
stack.pop()
stack.push(0)
m = stack.max
assert m == 4 and stack == [0, 2, 3, 4], stack

try:
    stack = Stack()
    stack.pop()
except IndexError:
    pass

try:
    stack = Stack()
    stack.max
except ValueError:
    pass
