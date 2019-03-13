"""
This problem was asked by Google
Given a singly linked list and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass.
"""


class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return str((self.value, self.next.value if self.next else None))


class NodeLinkedList:

    def __init__(self, node):
        self.ll = [node]
        while node.next:
            self.ll.append(node.next)
            node = node.next

    def __iter__(self):
        return iter(self.ll)

    def __getitem__(self, index):
        return self.ll[index]

    def __setitem__(self, index, item):
        self[index] = item

    def __len__(self):
        return len(self.ll)

    def __str__(self):
        return " -> ".join(str(node.value) for node in self)

    def remove_node_from_end(self, idx_from_end):
        if idx_from_end > len(self) or idx_from_end < 1:
            raise ValueError("Given Index must be smaller than the number of nodes in this Linked List and > 1")
        # remove_idx = len(self) - idx_from_end
        # for idx, node in enumerate(self):
        #     if idx == remove_idx:
        #         if idx > 0:
        #             self[idx - 1].next = node.next
        #             self.ll.remove(node)
        #             return
        remove_node = self[-idx_from_end]
        if idx_from_end != len(self):
            # this is not the first element of the linked list, update the next value of the previous element
            self[-(1 + idx_from_end)].next = remove_node.next
        self.ll.remove(remove_node)  # 1 pass


a = NodeLinkedList(Node(3, next_node=Node(7, next_node=Node(8, next_node=Node(10)))))
# print(a)
# a.remove_node_from_end(4)
# print(a)
nodes = list()
current = Node(0)
for value in range(1, 10000000):
    nodes.append(current)
    node = Node(value)
    current.next = node
    current = node
ll = NodeLinkedList(nodes[0])
print(ll[0])
ll.remove_node_from_end(1)
# print(ll[0])