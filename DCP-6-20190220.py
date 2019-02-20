"""
This problem was asked by Google.
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and
dereference_pointer functions that converts between nodes and memory addresses.
"""


class XOR:

    def __init__(self, value, both=tuple()):
        self.value = value
        self.both = both

    def __repr__(self):
        return str(self.value)

    def link(self, steps):
        i = 0 if steps < 0 else 1
        link = self
        for _ in range(abs(steps)):
            if not link.both:
                raise ValueError("The links ended before the given number of steps could be completed.")
            link = link.both[i]
        return link


class LinkedList:

    def __init__(self, lis):
        xors = [XOR(value) for value in lis]
        pushed_forw = [xors[-1]] + xors[0:-1]
        pushed_back = xors[1:] + [xors[0]]
        self._linked_list = list()
        for both, xor in zip(zip(pushed_forw, pushed_back), xors):
            xor.both = both
            self._linked_list.append(xor)

    def __str__(self):
        fstr = "{idx}: {val}"
        return "\n".join([" --> ".join([fstr.format(idx=(idx - 1) if idx != 0 else (len(self._linked_list) - 1),
                                                    val=xor.both[0]),
                                        fstr.format(idx=idx,
                                                    val=xor.value),
                                        fstr.format(idx=(idx + 1) if idx < len(self._linked_list) - 1 else 0,
                                                    val=xor.both[-1])])
                          for idx, xor in enumerate(self._linked_list)])

    def __iter__(self):
        return iter(self._linked_list)

    def __getitem__(self, idx):
        return self._linked_list[idx]

    def add(self, element):
        new_xor = XOR(element, both=(self._linked_list[-1], self._linked_list[0]))  # create the new xor
        self._linked_list[-1].both = (self._linked_list[-2], new_xor)  # change current last xor
        self._linked_list.append(new_xor)  # add the new xor to the list
        self._linked_list[0].both = (self._linked_list[-1], self._linked_list[1])  # update the first xor

    def get(self, idx):
        return self.__getitem__(idx)  # same as __getitem__


test = [x**2 for x in range(10)]
ll = LinkedList(test)
ll.add(100)
ll.add(121)
print(ll)
xor_4 = ll.get(4)
print(xor_4)
print(xor_4.link(-4))
print(ll[0:2])
print(ll.get(slice(0, 2)))