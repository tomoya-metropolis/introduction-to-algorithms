class Element:

    __slots__ = ['data', 'next']

    def __init__(self, data):
        self.data = data
        self.next = None


class StackEmptyExceptipn(Exception):

    pass


class Stack:

    __slots__ = ['size', 'head']

    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, z):
        self.size += 1

        z.next = self.head
        self.head = z

    def pop(self):
        if self.size == 0:
            raise StackEmptyExceptipn

        self.size -= 1

        popped = self.head
        result = popped.data
        self.head = popped.next
        popped = None

        return result

    def print_stack(self):
        print(f"size = {self.size} : ", end='')

        p = self.head
        while p:
            print(p.data, end=' -> ' if p.next else '')
            p = p.next

        print('')


if __name__ == '__main__':
    s = Stack()

    while True:
        print("1:push 2:pop 3:print > ", end='')
        op = int((input()))

        if op == 1:
            print("input data > ", end='')
            data = int(input())

            s.push(Element(data))
        elif op == 2:
            try:
                result = s.pop()
                print(f"popped data = {result}")
            except StackEmptyExceptipn:
                print("stack is empty.")
        elif op == 3:
            s.print_stack()
        else:
            print("invalid operation")
