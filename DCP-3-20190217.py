"""
This problem was asked by Google.
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.
For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
from json import loads, dumps, JSONDecoder


class Node:

    class JSONDecodeNodeTree:
        pass

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.val

    @staticmethod
    def deserialize(serialized_tree):
        return loads(serialized_tree)

    @property
    def binaries(self):
        return self.left, self.right

    @property
    def hierarchy(self):
        n = 0
        hierarchy = {n: (self.val, )}
        queue = [self.binaries]
        while queue:
            n += 1
            hierarchy[n] = list()
            enqueue = list()
            for binaries in queue:
                if binaries != (None, None):
                    hierarchy[n].append(binaries)
                    enqueue.extend([node.binaries for node in binaries if node])
            queue = enqueue
        return hierarchy

    @property
    def serialized(self):
        return dumps(str(self.hierarchy))


node = Node('root', left=Node('left', left=Node('left.left')), right=Node('right', left=Node("right.left"), right=Node("right.right")))
print(node.serialized)
print(Node.deserialize(node.serialized))

"""
tree:
        root
          |
    left-----right
      |
left---
"""

# def serialize(root):
#     def get_nodes(node):
#         return {'val': node.val, 'left': node.left, 'right': node.right}

#     n = 0
#     hierarchy = {n: root}
#     node = root
#     while node.left or node.right:
#         n += 1
#         hierarchy[n] = {'left': node}
