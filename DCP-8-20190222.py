"""
This problem was asked by Google.
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class Node:
    def __init__(self, value, left=None, right=None, name=""):
        self.name = name
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "{n}:{v}".format(n=self.name, v=self.value)

    @property
    def children(self):
        return (self.left, self.right)

    @property
    def unival_children(self):
        if self.left and self.right:
            return self.value == self.left.value and self.value == self.right.value
        else:
            return False

    @property
    def unival(self):
        if self.unival_children:
            nodes = [self]
            while nodes:
                nxt = list()
                for node in nodes:
                    if node.children == (None, None):
                        continue
                    if not node.unival_children:
                        return False
                    elif node.unival_children:
                        nxt.extend(node.children)
                nodes = nxt
            return True
        else:
            return False


def solve(node):
    univals = {node: node.unival}
    queue = [node]
    while queue:
        enqueue = list()
        for node in queue:
            for child in node.children:
                if child:
                    univals[child] = child.unival
                    enqueue.append(child)
        queue = enqueue
    return len([node for node, unival in univals.items() if unival])


# x = Node(0, name='x')
# y = Node(0, name='y')
# x = Node(1, name='x')
# y = Node(1, name='y')
# g = Node(1, name='g', left=x, right=y)
g = Node(1, name='g')
h = Node(1, name='h')
e = Node(1, left=h, right=g, name='e')
f = Node(0, name='f')
# I forgot the letter d
c = Node(0, left=e, right=f, name='c')
b = Node(1, name='b')
a = Node(0, left=b, right=c, name='a')

print(solve(a))
