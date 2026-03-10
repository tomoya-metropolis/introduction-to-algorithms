class DisjointSet:

    __slots__ = ['parent', 'sz']

    def __init__(self, elems):
        self.parent = {}
        self.sz = {}
        for e in elems:
            self.parent[e] = e
            self.sz[e] = 1

    def find(self, elem):
        if self.parent[elem] == elem:
            return elem

        self.parent[elem] = self.find(self.parent[elem])

        return self.parent[elem]

    def issame(self, elem1, elem2):
        return self.find(elem1) == self.find(elem2)

    def union(self, elem1, elem2):
        root1 = self.find(elem1)
        root2 = self.find(elem2)

        if root1 == root2:
            return

        if self.sz[root1] < self.sz[root2]:
            root1, root2 = root2, root1

        self.parent[root2] = root1
        self.sz[root1] += self.sz[root2]

    def print_set(self):
        for ch in self.sz.keys():
            if self.parent[ch] != ch:
                continue

            members = self.__members(ch)
 
            print(members)

    def __members(self, elem):
        root = self.find(elem)

        return [ch for ch in self.sz.keys() if self.find(ch) == root]


if __name__ == '__main__':
    disjoint_set = DisjointSet("abcdefghij")

    print("--- initial set ---")
    disjoint_set.print_set()

    print("--- union b and d ---")
    disjoint_set.union('b', 'd')
    disjoint_set.print_set()

    print("--- union e and g ---")
    disjoint_set.union('e', 'g')
    disjoint_set.print_set()

    print("--- union a and c ---")
    disjoint_set.union('a', 'c')
    disjoint_set.print_set()

    print("--- union h and i ---")
    disjoint_set.union('h', 'i')
    disjoint_set.print_set()

    print("--- union a and b ---")
    disjoint_set.union('a', 'b')
    disjoint_set.print_set()

    print("--- union e and f ---")
    disjoint_set.union('e', 'f')
    disjoint_set.print_set()

    print("--- union b and c ---")
    disjoint_set.union('b', 'c')
    disjoint_set.print_set()
