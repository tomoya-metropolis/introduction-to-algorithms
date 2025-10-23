import heapq


class Element:
    
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = self.right = self.parent = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __str__(self):
        return f"{self.ch}({self.freq})"
    

def print_tree(root):

    def print_tree_internal(r, space_size=0):
        if r.left:
            print_tree_internal(r.left, space_size=space_size+1)

        print('    ' * space_size, r)

        if r.right:
            print_tree_internal(r.right, space_size=space_size+1)

    if root:
        print_tree_internal(root)


def huffman(elements):
    heapq.heapify(elements)

    while len(elements) > 1:
        x = heapq.heappop(elements)
        y = heapq.heappop(elements)
        print(x, y)

        z = Element('', 0)
        z.left = x
        z.right = y
        z.freq = x.freq + y.freq
        heapq.heappush(elements, z)

    return heapq.heappop(elements)


if __name__ == '__main__':
    frequencies = [45, 13, 12, 16, 9, 5]
    characters = ['a', 'b', 'c', 'd', 'e', 'f']

    elements = []
    for freq, ch in zip(frequencies, characters):
        elements.append(Element(ch, freq))

    root = huffman(elements)
    print_tree(root)
