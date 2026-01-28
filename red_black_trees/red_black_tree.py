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

        self.__fix_after_insertion(z)

        self.height = self.__calculate_height()

    def contains(self, key):
        p = self.root
        while p != nil() and p.key != key:
            p = p.left if key < p.key else p.right

        return p

    def successor(self, z):
        if z.right != nil():
            x = z.right
            while x.left != nil():
                x = x.left

            return x
        else:
            x, y = z, z.parent
            while y != nil() and x == y.right:
                x = y
                y = x.parent

            return y

    def remove(self, z):
        self.size -= 1

        y = z
        color_of_y = y.color
        if z.left == nil():
            x = z.right
            self.__transplant(z, z.right)
        elif z.right == nil():
            x = z.left
            self.__transplant(z, z.left)
        else:
            y = self.successor(z)
            color_of_y = y.color
            x = y.right
            if y.parent != z:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            else:
                x.parent = y

            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if color_of_y == Color.BLACK:
            self.__fix_after_deletion(x)

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

    def __fix_after_insertion(self, z):
        while z.parent.color == Color.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == Color.RED:
                    # case 1
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        # case 2
                        z = z.parent
                        self.__rotate_left(z)
                    # case 3
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.__rotate_right(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == Color.RED:
                    # case 1
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        # case 2
                        z = z.parent
                        self.__rotate_right(z)
                    # case 3
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.__rotate_left(z.parent.parent)

        self.root.color = Color.BLACK

    def __fix_after_deletion(self, x):
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    # case 1
                    x.parent.color = Color.RED
                    w.color = Color.BLACK
                    self.__rotate_left(x.parent)
                    w = x.parent.right

                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    # case 2
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        # case 3
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self.__rotate_right(w)
                        w = x.parent.right
                    # case 4
                    w.color = x.parent.color
                    w.right.color = Color.BLACK
                    x.parent.color = Color.BLACK
                    self.__rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    # case 1
                    x.parent.color = Color.RED
                    w.color = Color.BLACK
                    self.__rotate_right(x.parent)
                    w = x.parent.left

                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    # case 2
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        # case 3
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self.__rotate_left(w)
                        w = x.parent.left
                    # case 4
                    w.color = x.parent.color
                    w.left.color = Color.BLACK
                    x.parent.color = Color.BLACK
                    self.__rotate_right(x.parent)
                    x = self.root

        x.color = Color.BLACK

    def __transplant(self, x, y):
        if x.parent == nil():
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.parent = x.parent

    def __calculate_height(self):

        def calculate_height_internal(r):
            if r == nil():
                return -1

            height_of_left = calculate_height_internal(r.left)
            height_of_right = calculate_height_internal(r.right)

            return height_of_left + 1 if height_of_left > height_of_right else height_of_right + 1

        if self.root == nil():
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
            if z == nil():
                print(f"{key} is not found in the tree.")
            else:
                t.remove(z)
        elif op == 3:
            t.print_tree()
        elif op == 4:
            print("input key > ", end='')
            key = int(input())

            z = t.contains(key)
            if z == nil():
                print(f"{key} is not found in the tree.")
            else:
                succ = t.successor(z)
                if succ == nil():
                    print("successor is none.")
                else:
                    print(f"successor = {succ.key}")
        else:
            print("invalid operation")
