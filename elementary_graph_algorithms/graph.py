import enum


class Color(enum.Enum):

    WHITE = 'white'
    GRAY = 'gray'
    BLACK = 'black'


class Vertex:

    __slots__ = ['name', 'predecessor', 'color', 'distance']

    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.color = Color.WHITE
        self.distance = 0


class Edge:

    __slots__ = ['start', 'end']

    def __init__(self, start, end):
        self.start = start
        self.end = end


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = {v: [] for v in vertices.keys()}
        self.__initialize_graph()

    def print_graph(self):
        for vertex in self.vertices.values():
            print(vertex.name, ' :', self.adjacency_list[vertex.name])

    def __initialize_graph(self):
        for edge in self.edges:
            self.adjacency_list[edge.start].append(edge.end)
