class Element:

    __slots__ = ['data', 'next', 'prev']

    def __init__(self, data):
        self.data = data
        self.next = self.prev = None


class LinkedList:

    __slots__ = ['size', 'head', 'tail']

    def __init__(self):
        self.size = 0
        self.head = self.tail = None

    def append(self, z):
        self.size += 1

        if not self.head:
            self.head = z
        else:
            self.tail.next = z
        z.prev = self.tail
        self.tail = z

    def contains(self, data):
        p = self.head
        while p and p.data != data:
            p = p.next

        return p

    def remove(self, z):
        self.size -= 1

        if z.next:
            z.next.prev = z.prev
        else:
            self.tail = z.prev
        if z.prev:
            z.prev.next = z.next
        else:
            self.head = z.next

        z = None

    def print_list(self):
        print(f"size = {self.size}")

        print("--- from head to tail ---")
        p = self.head
        while p:
            print(p.data, end=' -> ' if p.next else '')

            p = p.next

        print('')

        print("--- from tail to head ---")
        p = self.tail
        while p:
            print(p.data, end=' <- ' if p.prev else '')

            p = p.prev

        print('')


if __name__ == '__main__':
    ll = LinkedList()

    while True:
        print("1:append 2:remove 3:print > ", end='')
        op = int(input())

        if op == 1:
            print("input data > ", end='')
            data = int(input())

            ll.append(Element(data))
        elif op == 2:
            print("input data > ", end='')
            data = int(input())

            z = ll.contains(data)
            if not z:
                print(f"{data} is not found in the list.")
            else:
                ll.remove(z)
        elif op == 3:
            ll.print_list()
        else:
            print("invalid operation")
