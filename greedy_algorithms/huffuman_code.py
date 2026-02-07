import heapq


class Element:

    __slots__ = ['ch', 'frequency', 'left', 'right']

    def __init__(self, ch, frequency):
        self.ch = ch
        self.frequency = frequency
        self.left = self.right = None

    def __str__(self):
        return f"{self.ch}({self.frequency})"

    def __lt__(self, other):
        return self.frequency < other.frequency


def huffman(characters):
    elements = list(characters.values())

    heapq.heapify(elements)

    while len(elements) > 1:
        x = heapq.heappop(elements)
        y = heapq.heappop(elements)
        z = Element('', x.frequency + y.frequency)
        z.left = x
        z.right = y

        heapq.heappush(elements, z)
        heapq.heapify(elements)

    return heapq.heappop(elements)


def print_tree(root):

    def print_tree_internal(r, space_size=0):
        if r.left:
            print_tree_internal(r.left, space_size=space_size+1)

        print('  ' * space_size, r)

        if r.right:
            print_tree_internal(r.right, space_size=space_size+1)

    print_tree_internal(root)


if __name__ == '__main__':
    characters = {}

    characters['a'] = Element('a', 45)
    characters['b'] = Element('b', 13)
    characters['c'] = Element('c', 12)
    characters['d'] = Element('d', 16)
    characters['e'] = Element('e', 9)
    characters['f'] = Element('f', 5)

    print(" ch |", end='')
    for ch in characters.keys():
        print(f"{ch:^3}|", end='')
    print('')
    print('freq|', end='')
    for elem in characters.values():
        print(f"{elem.frequency:^3}|", end='')
    print('')

    root = huffman(characters)
    print("--- result ---")
    print_tree(root)
