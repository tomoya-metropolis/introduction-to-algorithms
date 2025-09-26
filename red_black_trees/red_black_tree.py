import enum


class Color(enum.Enum):

    RED = 'red'
    BLACK = 'black'


class Element:

    __slots__ = ['key', 'left', 'right', 'parent', 'color']

    def __init__(self, key, color=Color.RED):
        self.key = key
        self.left = self.right = self.parent = None
        self.color = color


class Tree:

    __slots__ = ['size', 'height', 'root']

    def __init__(self):
        self.size = 0
        self.height = 0
        self.root = None

    def put(self, z):
        self.size += 1

        x, y = self.root, None

        while x:
            y = x
            x = x.left if z.key < x.key else x.right

        z.parent = y
        if not y:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

        self.height = self.__get_height()

    def contains(self, key):
        p = self.root

        while p and p.key != key:
            p = p.left if key < p.key else p.right

        return p

    def remove(self, z):
        self.size -= 1

        if not z.left:
            self.__transplant(z, z.right)
        elif not z.right:
            self.__transplant(z, z.left)
        else:
            y = self.successor(z)
            if y != z.right:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y

        z = None

        self.height = self.__get_height()

    def successor(self, z):
        if z.right:
            p = z.right
            while p.left:
                p = p.left

            return p
        else:
            p, q = z, z.parent
            while q and p == q.right:
                p = q
                q = q.parent

            return q

    def print_tree(self):

        def print_tree_internal(r, space_size=0):
            if r.left:
                print_tree_internal(r.left, space_size=space_size+1)

            print('    ' * space_size, r.key)

            if r.right:
                print_tree_internal(r.right, space_size=space_size+1)

        print(f"size = {self.size}, height = {self.height}")

        if self.root:
            print_tree_internal(self.root)

    def __transplant(self, p, q):
        if not p.parent:
            self.root = q
        elif p == p.parent.left:
            p.parent.left = q
        else:
            p.parent.right = q

        if q:
            q.parent = p.parent

    def __get_height(self):

        def get_height_internal(r):
            if not r:
                return -1

            height_of_left = get_height_internal(r.left)
            height_of_right = get_height_internal(r.right)

            return height_of_left + 1 if height_of_left > height_of_right else height_of_right + 1

        if not self.root:
            return 0

        return get_height_internal(self.root)


if __name__ == '__main__':
    t = Tree()

    t.put(Element(8))
    t.put(Element(3))
    t.put(Element(10))
    t.put(Element(1))
    t.put(Element(6))
    t.put(Element(14))
    t.put(Element(4))
    t.put(Element(7))
    t.put(Element(13))

    while True:
        print("1:put 2:remove 3:print  4:successor > ", end='')
        op = int((input()))

        if op == 1:
            print("input key > ", end='')
            key = int(input())

            t.put(Element(key))
        elif op == 2:
            print("input key > ", end='')
            key = int(input())

            z = t.contains(key)
            if not z:
                print(f"{key} is not found in the tree.")
            else:
                t.remove(z)
        elif op == 3:
            t.print_tree()
        elif op == 4:
            print("input key > ", end='')
            key = int(input())

            z = t.contains(key)
            if not z:
                print(f"{key} is not found in the tree.")
            else:
                succ = t.successor(z)
                if not succ:
                    print("successor is none.")
                else:
                    print(f"successor = {succ.key}")
        else:
            print("invalid operation")
