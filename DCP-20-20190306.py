"""
This problem was asked by Google.
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""


class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return str((self.value, self.next.value))

    @property
    def values(self):
        return (self.value, self.next.value if self.next else None)


class NodeLinkedList:

    def __init__(self, node):
        self.ll = [node]
        while node.next:
            self.ll.append(node.next)
            node = node.next
        self._values = [node.values for node in self]

    def __iter__(self):
        return iter(self.ll)

    def __str__(self):
        return " -> ".join(str(node.value) for node in self)

    @property
    def values(self):
        return [node.values for node in self]

    def find_intersection_node(self, nll):
        return next((node for node in nll if node in self), None)

    def find_intersection_node_value_based(self, nll):
        # Not constant space
        return next((node for node in nll if node.values in self.values), None)


intersecting_node = Node(8, next_node=Node(10))
a = NodeLinkedList(Node(3, next_node=Node(7, next_node=intersecting_node)))
b = NodeLinkedList(Node(99, next_node=Node(1, next_node=intersecting_node)))
print(a)
print(b)
print(a.find_intersection_node(b))
print(b.find_intersection_node(a))
print(a.find_intersection_node_value_based(b))
print(b.find_intersection_node_value_based(a))
