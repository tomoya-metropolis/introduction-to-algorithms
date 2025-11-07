class Element:

    def __init__(self, is_leaf=True):
        self.n = 0
        self.keys = []
        self.is_leaf = is_leaf
        self.children = []


class Tree:

    def __init__(self, min_degree=2):
        self.root = None
        self.min_degree = min_degree

    def insert(self, key):
        if not self.root:
            self.root = Element()

        r = self.root
        if r.n == 2 * self.min_degree - 1:
            s = Element()
            self.root = s
            s.is_leaf = False
            s.children.insert(0, r)

            self.__split_child(s, 0)

            self.__insert_non_full(s, key)
        else:
            self.__insert_non_full(r, key)

    def contains(self, key):

        def __conttains_internal(r, key):
            i = 0
            while i < r.n and r.keys[i] < key:
                i += 1

            if i < r.n and r.keys[i] == key:
                return r
            elif r.is_leaf:
                return None
            else:
                return __conttains_internal(r.children[i], key)

        return __conttains_internal(self.root, key)

    def remove(self, key):

        def __remove_internal(x, key):
            i = 0
            while i < x.n and x.keys[i] < key:
                i += 1

            if i < x.n and x.keys[i] == key:
                if x.is_leaf:
                    # case 1
                    x.keys.remove(key)
                    x.n -= 1
                else:
                    if x.children[i].n >= self.min_degree:
                        # case 2 - a
                        y = x.children[i]
                        replaced = y.keys[-1]
                        x.keys[i] = replaced
                        y.keys = y.keys[:-1]
                        y.n -= 1
                    elif x.children[i + 1].n >= self.min_degree:
                        # case 2 - b
                        y = x.children[i + 1]
                        replaced = y.keys[0]
                        x.keys[i] = replaced
                        y.keys = y.keys[1:]
                        y.n -= 1
                    else:
                        # case 2 - c
                        y = x.children[i]
                        z = x.children[i + 1]
                        y.keys += x.keys
                        y.n += x.n
                        y.keys += z.keys
                        y.n += z.n
                        if not y.is_leaf:
                            y.children += z.children

                        y.keys.remove(key)
                        x.n -= 1
                        if x.n == 0:
                            self.root = y
            else:
                if x.children[i].n == self.min_degree - 1:
                    if i > 0 and x.children[i - 1].n >= self.min_degree:
                        # case 3 - a - 1
                        y = x.children[i]
                        z = x.children[i - 1]
                        key_to_up = z.keys[-1]
                        key_to_dwon = x.keys[i - 1]

                        x.keys[i - 1] = key_to_up
                        z.keys = z.keys[:-1]
                        z.n -= 1
                        y.keys.insert(0, key_to_dwon)
                        y.n += 1
                        if not y.is_leaf:
                            children_to_move = z.children[-1]
                            z.children = z.children[:-1]
                            y.children.insert(0, children_to_move)

                        # recursive call
                        __remove_internal(x, key)
                    elif i < x.n and x.children[i + 1].n >= self.min_degree:
                        # case 3 - 1 - b
                        y = x.children[i]
                        z = x.children[i + 1]
                        key_to_up = z.keys[0]
                        key_to_down = x.keys[i]

                        x.keys[i] = key_to_up
                        z.keys = z.keys[1:]
                        z.n -= 1
                        y.keys.append(key_to_down)
                        y.n += 1
                        if not y.is_leaf:
                            children_to_move = z.children[0]
                            z.children = z.children[1:]
                            y.children.append(children_to_move)

                        # recursive call
                        __remove_internal(x, key)
                    elif i > 0 and x.children[i - 1].n == self.min_degree - 1:
                        # case 3 - 2 - a
                        y = x.children[i]
                        z = x.children[i - 1]
                        key_to_down = x.keys[i - 1]

                        z.keys.append(key_to_down)
                        z.n += 1
                        z.keys.extend(y.keys)
                        z.n += y.n

                        if not z.is_leaf:
                            z.children.extend(y.children)

                        x.keys.pop(i - 1)
                        x.n -= 1
                        x.children.pop(i - 1)
                        if x.n == 0:
                            self.root = z

                        # recursive call
                        __remove_internal(z, key)
                    elif i < x.n and x.children[i + 1].n == self.min_degree - 1:
                        # case 3 - 3 - b
                        y = x.children[i + 1]
                        z = x.children[i]
                        key_to_down = x.keys[i]

                        z.keys.append(key_to_down)
                        z.n += 1
                        z.keys.extend(y.keys)
                        z.n += y.n

                        if not z.is_leaf:
                            z.children.extend(y.children)

                        x.keys.pop(i)
                        x.n -= 1
                        x.children.pop(i)
                        if x.n == 0:
                            self.root = z

                        # recursive call
                        __remove_internal(z, key)
                else:
                    __remove_internal(x.children[i], key)

        __remove_internal(self.root, key)

    def print_tree(self):

        def print_tree_internal(r, space_size=0):
            print(space_size * '  ', r.keys)

            if not r.is_leaf:
                for c in r.children:
                    print_tree_internal(c, space_size=space_size+1)

        if self.root.keys:
            print_tree_internal(self.root)

    def __split_child(self, x, i):
        y = x.children[i]
        key_to_up = y.keys[self.min_degree - 1]
        z = Element()
        z.keys = y.keys[self.min_degree:]
        z.is_leaf = y.is_leaf
        z.n = len(z.keys)
        y.keys = y.keys[:self.min_degree - 1]
        y.n = len(y.keys)

        if not y.is_leaf:
            z.children = y.children[self.min_degree:]
            y.children = y.children[:self.min_degree]

        x.keys.insert(i, key_to_up)
        x.n += 1
        x.children.insert(i + 1, z)

    def __insert_non_full(self, x, key):
        if x.is_leaf:
            i = x.n - 1
            while i >= 0 and x.keys[i] > key:
                i -= 1

            x.keys.insert(i + 1, key)
            x.n += 1
        else:
            i = x.n - 1
            while i >= 0 and x.keys[i] > key:
                i -= 1

            i += 1

            if x.children[i].n == 2 * self.min_degree - 1:
                self.__split_child(x, i)
                if x.keys[i] < key:
                    i += 1

            self.__insert_non_full(x.children[i], key)


if __name__ == '__main__':
    t = Tree()

    t.insert(5)
    t.insert(9)
    t.insert(3)
    t.insert(7)
    t.insert(1)
    t.insert(2)
    t.insert(8)
    t.insert(6)
    t.insert(0)
    t.insert(4)

    while True:
        print("1:put 2:remove 3:print > ", end='')
        op = int((input()))

        if op == 1:
            print("input key > ", end='')
            key = int(input())

            t.insert(key)
        elif op == 2:
            print("input key > ", end='')
            key = int(input())

            z = t.contains(key)
            if not z:
                print(f"{key} is not found in the tree.")
            else:
                t.remove(key)
        elif op == 3:
            t.print_tree()
        else:
            print("invalid operation")
