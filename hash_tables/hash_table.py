class Element:

    __slots__ = ['key', 'next', 'prev']

    def __init__(self, key):
        self.key = key
        self.next = self.prev = None


class Hashtable:

    __slots__ = ['bucket_size', 'tables']

    def __init__(self, bucket_size=13):
        self.bucket_size = bucket_size
        self.tables = [None for _ in range(self.bucket_size)]

    def put(self, z):
        hash_val = self.__calculate_hash_value(z.key)

        if self.tables[hash_val]:
            self.tables[hash_val].prev = z
        z.next = self.tables[hash_val]
        self.tables[hash_val] = z

    def contains(self, key):
        hash_val = self.__calculate_hash_value(key)

        p = self.tables[hash_val]
        while p and p.key != key:
            p = p.next

        return p

    def remove(self, z):
        hash_val = self.__calculate_hash_value(key)

        if z.next:
            z.next.prev = z.prev
        if z.prev:
            z.prev.next = z.next
        else:
            self.tables[hash_val] = z.next

        z = None

    def print_hash_table(self):
        for i in range(self.bucket_size):
            print(i, ': ', end='')

            p = self.tables[i]
            while p:
                print(p.key, end=' -> ' if p.next else '')

                p = p.next

            print('')

    def __calculate_hash_value(self, key):
        return key % self.bucket_size


if __name__ == '__main__':
    ht = Hashtable()

    for i in range(1, 101):
        ht.put(Element(i))

    ht.print_hash_table()

    while True:
        print("1:put 2:remove 3:print > ", end='')
        op = int(input())

        if op == 1:
            print("input key > ", end='')
            key = int(input())

            ht.put(Element(key))
        elif op == 2:
            print("input key > ", end='')
            key = int(input())

            z = ht.contains(key)
            if not z:
                print(f"{key} is not found in the hash table.")
            else:
                ht.remove(z)
        elif op == 3:
            ht.print_hash_table()
        else:
            print("invalid operation")
