from collections import defaultdict


class Element:

    __slots__ = ['data', 'next', 'prev']

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class List:

    __slots__ = ['head', 'tail']

    def __init__(self):
        self.head = None
        self.tail = None

    def parent_element(self):
        return self.head

    def merge(self, other):
        parent_of_self = self.parent_element()
        parent_of_other = other.parent_element()

        if parent_of_self.data < parent_of_other.data:
            other.tail.prev = self.tail
            if self.tail:
                self.tail.next = other.head
            self.tail = other.tail
            other = None
        else:
            other.tail.next = self.head
            if self.head:
                self.head.prev = other.tail
            self.head = other.head
            other = None

    def print_list(self):
        p = self.head
        while p:
            print(p.data, end=' -> ' if p.next else '\n')

            p = p.next


def make_set(ch):
    l = List()
    l.head = l.tail = Element(ch)

    return l


def union_set(disjoint_set, x, y):
    x.merge(y)
    del disjoint_set[y.head.data]


def print_set(disjoint_set):
    for k, v in disjoint_set.items():
        print(k, ': ', end='')
        v.print_list()


if __name__ == '__main__':
    disjoint_set = {}
    for ch in 'abcdefghij':
        disjoint_set[ch] = make_set(ch)

    print("--- after initialization ---")
    print_set(disjoint_set)
    input()

    print("union b and d")
    union_set(disjoint_set, disjoint_set['b'], disjoint_set['d'])
    print_set(disjoint_set)
    input()

    print("union e and g")
    union_set(disjoint_set, disjoint_set['e'], disjoint_set['g'])
    print_set(disjoint_set)
    input()

    print("union a and c")
    union_set(disjoint_set, disjoint_set['a'], disjoint_set['c'])
    print_set(disjoint_set)
    input()

    print("union h and i")
    union_set(disjoint_set, disjoint_set['h'], disjoint_set['i'])
    print_set(disjoint_set)
    input()

    print("union a and b")
    union_set(disjoint_set, disjoint_set['a'], disjoint_set['b'])
    print_set(disjoint_set)
    input()

    print("union e and f")
    union_set(disjoint_set, disjoint_set['e'], disjoint_set['f'])
    print_set(disjoint_set)
    input()
