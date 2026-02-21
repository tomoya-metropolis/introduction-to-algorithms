class Element:

    def __init__(self, is_leaf=True):
        self.keys = []
        self.n = 0
        self.is_leaf = is_leaf
        self.children = []


class Tree:

    def __init__(self, min_degree=2):
        self.root = Element()
        self.min_degree = min_degree

    def insert(self, key):
        if self.root.n == 2 * self.min_degree - 1:
            s = Element()

            s.children.append(self.root)
            s.is_leaf = False
            self.root = s

            self.__split_child(s, 0)
            self.__insert_non_full(s, key)
        else:
            self.__insert_non_full(self.root, key)

    def contains(self, key):
        return self.__contains_internal(self.root, key)

    def remove(self, key):
        self.__remove_internal(self.root, key)

    def print_tree(self):

        def print_tree_internal(r, space_size=0):
            print('  ' * space_size, r.keys)

            for child in r.children:
                print_tree_internal(child, space_size=space_size+1)

        print_tree_internal(self.root)

    def __insert_non_full(self, x, key):
        if x.is_leaf:
            i = x.n - 1
            while i >= 0 and key < x.keys[i]:
                i -= 1

            i += 1
            x.keys.insert(i, key)
            x.n = len(x.keys)
        else:
            i = x.n - 1
            while i >= 0 and key < x.keys[i]:
                i -= 1

            i += 1
            if x.children[i].n == 2 * self.min_degree - 1:
                self.__split_child(x, i)
                if key > x.keys[i]:
                    i += 1

            self.__insert_non_full(x.children[i], key)

    def __split_child(self, x, i):
        y = x.children[i]
        z = Element()

        key_to_lift = y.keys[self.min_degree - 1]

        z.keys = y.keys[self.min_degree:]
        z.n = len(z.keys)
        y.keys = y.keys[:self.min_degree - 1]
        y.n = len(y.keys)

        z.is_leaf = y.is_leaf
        if not y.is_leaf:
            z.children = y.children[self.min_degree:]
            y.children = y.children[:self.min_degree]

        x.keys.insert(i, key_to_lift)
        x.n = len(x.keys)
        x.children.insert(i + 1, z)

    def __contains_internal(self, x, key):
        i = 0
        while i < x.n and key > x.keys[i]:
            i += 1

        if i < x.n and x.keys[i] == key:
            return x
        else:
            if x.is_leaf:
                return None
            else:
                return self.__contains_internal(x.children[i], key)

    def __remove_internal(self, x, key):
        i = 0
        while i < x.n and key > x.keys[i]:
            i += 1

        if i < x.n and x.keys[i] == key:
            if x.is_leaf:
                x.keys.pop(i)
                x.n = len(x.keys)
            else:
                if x.children[i].n >= self.min_degree:
                    y = x.children[i]
                    key_to_lift = y.keys[-1]

                    y.keys = y.keys[:-1]
                    y.n = len(y.keys)

                    x.keys[i] = key_to_lift
                elif x.children[i + 1].n >= self.min_degree:
                    y = x.children[i + 1]
                    key_to_lift = y.keys[0]

                    y.keys = y.keys[1:]
                    y.n = len(y.keys)

                    x.keys[i] = key_to_lift
                else:
                    y = x.children[i]
                    z = x.children[i + 1]

                    y.keys.append(x.keys[i])
                    y.keys.extend(z.keys)
                    y.n = len(y.keys)

                    if not y.is_leaf:
                        y.children.extend(z.children)

                    x.keys.pop(i)
                    x.n = len(x.keys)
                    if x.n == 0:
                        self.root = y

                    self.__remove_internal(y, key)
        else:
            if x.children[i].n == self.min_degree - 1:
                if i > 0 and x.children[i - 1].n >= self.min_degree:
                    y = x.children[i]
                    z = x.children[i - 1]
                    key_to_lift = z.keys[-1]
                    key_to_lower = x.keys[i - 1]

                    z.keys.pop(-1)
                    z.n = len(z.keys)
                    x.keys[i - 1] = key_to_lift
                    y.keys.insert(0, key_to_lower)
                    y.n = len(y.keys)

                    if not y.is_leaf:
                        y.children.insert(0, z.children[-1])
                        z.children = z.children[:-1]
                elif i < x.n and x.children[i + 1].n >= self.min_degree:
                    y = x.children[i]
                    z = x.children[i + 1]
                    key_to_lift = z.keys[0]
                    key_to_lower = x.keys[i]

                    z.keys.pop(0)
                    z.n = len(z.keys)
                    x.keys[i] = key_to_lift
                    y.keys.append(key_to_lower)
                    y.n = len(y.keys)

                    if not y.is_leaf:
                        y.children.append(z.children[0])
                        z.children = z.children[1:]
                else:
                    if i > 0 and x.children[i - 1].n == self.min_degree - 1:
                        y = x.children[i]
                        z = x.children[i - 1]

                        z.keys.append(x.keys[i - 1])
                        z.keys.extend(y.keys)
                        z.n = len(z.keys)

                        if not y.is_leaf:
                            z.children.extend(y.children)

                        x.keys.pop(i - 1)
                        x.n = len(x.keys)
                        x.children.pop(i)
                        if x.n == 0:
                            self.root = z

                        i -= 1
                    elif i < x.n and x.children[i + 1].n == self.min_degree - 1:
                        y = x.children[i]
                        z = x.children[i + 1]

                        y.keys.append(x.keys[i])
                        y.keys.extend(z.keys)
                        y.n = len(y.keys)

                        if not y.is_leaf:
                            y.children.extend(z.children)

                        x.keys.pop(i)
                        x.n = len(x.keys)
                        x.children.pop(i + 1)
                        if x.n == 0:
                            self.root = y

            self.__remove_internal(x.children[i], key)


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
        print("1:insert 2:remove 3:print > ", end='')
        op = int(input())

        if op == 1:
            print("input key > ", end='')
            key = int(input())

            t.insert(key)
        elif op == 2:
            print("input key > ", end='')
            key = int(input())

            x = t.contains(key)
            if not x:
                print(f"{key} is not found in the tree.")
            else:
                t.remove(key)
        elif op == 3:
            t.print_tree()
        else:
            print("invalid operation")
