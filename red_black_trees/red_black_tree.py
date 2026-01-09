import enum


class Color(enum.Enum):

    RED = 'red'
    BLACK = 'black'


class Element:

    __slots__ = ['key', 'left', 'right', 'parent', 'color']

    def __init__(self, key, color=Color.BLACK):
        self.key = key
        self.left = self.right = self.parent = None
        self.color = color

    def __str__(self):
        return f"{self.key}({self.color.value})"


sentinel = None


def nil():
    global sentinel

    if not sentinel:
        sentinel = Element(-1)

    return sentinel


class Tree:

    __slots__ = ['root', 'size', 'height']

    def __init__(self):
        self.root = nil()
        self.size = self.height = 0

    def put(self, z):
        self.size += 1

        x, y = self.root, nil()
        while x != nil():
            y = x
            x = x.left if z.key < x.key else x.right

        z.parent = y
        z.left = z.right = nil()
        if y == nil():
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

        self.height = self.__calculate_height()

    def contains(self, key):
        p = self.root
        while p and p.key != key:
            p = p.left if key < p.key else p.right

        return p

    def successor(self, z):
        if z.right:
            x = z.right
            while x.left:
                x = x.left

            return x
        else:
            x, y = z, z.parent
            while y and x == y.right:
                x = y
                y = x.parent

            return y

    def remove(self, z):
        self.size -= 1

        if not z.left:
            self.__transplant(z, z.right)
        elif not z.right:
            self.__transplant(z, z.left)
        else:
            y = self.successor(z)
            if y.parent != z:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y

        z = None

        self.height = self.__calculate_height()

    def print_tree(self):

        def print_tree_internal(r, space_size=0):
            if r.left != nil():
                print_tree_internal(r.left, space_size=space_size+1)

            print('    ' * space_size, r)

            if r.right != nil():
                print_tree_internal(r.right, space_size=space_size+1)

        print(f"size = {self.size} / height = {self.height}")

        if self.root != nil():
            print_tree_internal(self.root)

    def __rotate_left(self, x):
        y = x.right

        x.right = y.left
        if y.left != nil():
            y.left.parent = x

        y.parent = x.parent
        if x.parent == nil():
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def __rotate_right(self, x):
        y = x.left

        x.left = y.right
        if y.right != nil():
            y.right.parent = x

        y.parent = x.parent
        if x.parent == nil():
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y

    def __transplant(self, x, y):
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        if y:
            y.parent = x.parent

    def __calculate_height(self):

        def calculate_height_internal(r):
            if r == nil():
                return -1

            height_of_left = calculate_height_internal(r.left)
            height_of_right = calculate_height_internal(r.right)

            return height_of_left + 1 if height_of_left > height_of_right else height_of_right + 1

        if self.root != nil():
            return 0

        return calculate_height_internal(self.root)


if __name__ == '__main__':
    t = Tree()

    while True:
        print("1:put 2:remove 3:print 4:successor > ", end='')
        op = int(input())

        if op == 1:
            print("input key > ", end='')
            key = int(input())

            t.put(Element(key, color=Color.RED))
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
