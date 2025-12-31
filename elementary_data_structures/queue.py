class QueueEmptyException(Exception):

    pass


class Element:

    __slots__ = ['data', 'next']

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    __slots__ = ['size', 'head', 'tail']

    def __init__(self):
        self.size = 0
        self.head = self.tail = None

    def enqueue(self, z):
        self.size += 1

        if not self.head:
            self.head = z
        else:
            self.tail.next = z
        self.tail = z

    def dequeue(self):
        if self.size == 0:
            raise QueueEmptyException

        self.size -= 1

        dequeued = self.head
        result = dequeued.data
        self.head = dequeued.next
        dequeued = None

        return result

    def print_queue(self):
        print(f"size = {self.size} : ", end='')

        p = self.head
        while p:
            print(p.data, end=' -> ' if p.next else '')

            p = p.next

        print('')


if __name__ == '__main__':
    q = Queue()

    while True:
        print("1:enqueue 2:dequeue 3:print > ", end='')
        op = int(input())

        if op == 1:
            print("input data > ", end='')
            data = int(input())

            q.enqueue(Element(data))
        elif op == 2:
            try:
                result = q.dequeue()
                print(f"dequeued = {result}")
            except QueueEmptyException:
                print("queue is empty.")
        elif op == 3:
            q.print_queue()
        else:
            print("invalid operation")
