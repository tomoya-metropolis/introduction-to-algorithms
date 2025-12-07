import enum


class Color(enum.Enum):

    WHITE = 'white'
    GRAY = 'gray'
    BLACK = 'black'


class Vertex:

    __slots__ = ['name', 'predecessor', 'color', 'distance', 'start', 'finish']

    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.color = Color.WHITE
        self.distance = 0
        self.start = 0
        self.finish = 0


class Edge:

    __slots__ = ['start', 'end', 'weight']

    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return (self.start == other.start and self.end == other.end) \
            or (self.start == other.end and self.end == other.start)


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = {v: [] for v in vertices.keys()}
        self.__initialize_graph()

    def print_graph(self):
        for vertex in self.vertices.values():
            print(vertex.name, ': ', end='')
            adjacencies = self.adjacency_list[vertex.name]
            for i, adjacency in enumerate(adjacencies):
                end, weight = adjacency
                print(f"{end}({weight})", end=' -> ' if i <
                      len(adjacencies) - 1 else '')
            print('')

    def __initialize_graph(self):
        for edge in self.edges:
            self.adjacency_list[edge.start].append((edge.end, edge.weight))
