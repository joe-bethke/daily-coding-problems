"""
This problem was asked by Apple.
Implement a queue using two stacks.
Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
enqueue, which inserts an element into the queue, and dequeue, which removes it.
"""


class Queue:

    def __init__(self, incoming=list(), outgoing=list()):
        self.incoming = incoming
        self.outgoing = outgoing

    def enqueue(self, element):
        self.incoming.append(element)

    def dequeue(self):
        if not self.outgoing:
            while self.incoming:
                self.outgoing.append(self.incoming.pop())
        return self.outgoing.pop()


q = Queue()
for i in range(10):
    q.enqueue(i)
for i in range(10):
    print(q.dequeue())
