class Element:

    __slots__ = ['data', 'next']

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    __slots__ = ['head', 'tail']

    def __init__(self):
        self.head = self.tail = None

    def print(self):
        p = self.head
        while p:
            print(p.data, end=' -> ' if p.next else '')

            p = p.next

        print('')


def find_set(disjoint_set, x):
    for set in disjoint_set.values():
        p = set.head
        while p and p.data != x:
            p = p.next

        if p:
            return set

    return None


def union(disjoint_set, x, y):
    parent_of_x = find_set(disjoint_set, x)
    parent_of_y = find_set(disjoint_set, y)

    if parent_of_x == parent_of_y:
        return

    parent_of_x.tail.next = parent_of_y.head
    parent_of_x.tail = parent_of_y.tail
    del disjoint_set[y]


def print_set(disjoint_set):
    for k, l in disjoint_set.items():
        print(k, ': ', end='')
        l.print()


if __name__ == '__main__':
    disjoint_set = {}
    for ch in "abcdefghij":
        e = Element(ch)
        ll = LinkedList()
        ll.head = ll.tail = e
        disjoint_set[ch] = ll

    print("--- initial set ---")
    print_set(disjoint_set)

    print("--- union b and d ---")
    union(disjoint_set, 'b', 'd')
    print_set(disjoint_set)

    print("--- union e and g ---")
    union(disjoint_set, 'e', 'g')
    print_set(disjoint_set)

    print("--- union a and c ---")
    union(disjoint_set, 'a', 'c')
    print_set(disjoint_set)

    print("--- union h and i ---")
    union(disjoint_set, 'h', 'i')
    print_set(disjoint_set)

    print("--- union a and b ---")
    union(disjoint_set, 'a', 'b')
    print_set(disjoint_set)

    print("--- union e and f ---")
    union(disjoint_set, 'e', 'f')
    print_set(disjoint_set)

    print("--- union b and c ---")
    union(disjoint_set, 'b', 'c')
    print_set(disjoint_set)
