"""
Implement locking in a binary tree.
A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
Design a binary tree node class with the following methods:
is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false.
Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false.
Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like.
You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes.
Each method should run in O(h), where h is the height of the tree.
"""


def lock_operation(caller):
    def operation(func):
        def decorator(self, *args, **kwargs):
            print(caller.format(self.value))
            func_return = func(self, *args, **kwargs)
            print("{n} is {l}".format(n=self.value, l="Locked" if self.is_locked else "Unlocked"))
            print("--------")
            return func_return
        return decorator
    return operation


class Node:

    def __init__(self, value, left=None, right=None, parent=None, is_locked=False):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.is_locked = is_locked

    def __repr__(self):
        return "{s}: left: {l}, right: {r}".format(s=self.value,
                                                   l=self.left.value if self.left is not None else None,
                                                   r=self.right.value if self.right is not None else None)

    @lock_operation("Locking {}...")
    def lock(self):
        if self.is_locked:
            return True
        node_locked = False
        node = self
        while node is not None and node.parent:
            if node.parent.is_locked:
                self.is_locked = False
                return self.is_locked
            else:
                node = node.parent
        node = self
        queue = [node]
        while queue:
            enqueue = list()
            for child_node in queue:
                if child_node is not None:
                    if child_node.is_locked:
                        self.is_locked = False
                        return self.is_locked
                    else:
                        enqueue.append(child_node.left)
                        enqueue.append(child_node.right)
            queue = enqueue
        self.is_locked = True
        return self.is_locked

    @lock_operation("Unlocking {}...")
    def unlock(self):
        self.is_locked = False
        return self.is_locked



root = Node("A")
root.left = Node("B", parent=root)
root.right = Node("C", parent=root)
root.left.left = Node("D", parent=root.left)
root.left.right = Node("E", parent=root.left)
root.right.right = Node("F", parent=root.right)

root.lock()
root.lock()
root.left.lock()
root.unlock()
root.left.lock()
root.right.lock()
root.left.unlock()
root.right.unlock()
root.right.right.lock()
root.right.lock()
