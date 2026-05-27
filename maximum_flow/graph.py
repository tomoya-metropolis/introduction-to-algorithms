import enum
from collections import defaultdict


class Color(enum.Enum):

    WHITE = 'white'
    GRAY = 'gray'
    BLACK = 'black'


class Vertex:

    def __init__(self, name):
        self.name = name
        self.precessor = None
        self.color = Color.WHITE


class Edge:

    def __init__(self, start, end, capacity, flow=0):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = flow
        self.reverse = None

    @property
    def residual_capacity(self):
        return self.capacity - self.flow


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = defaultdict(list)
        self.__initialize_graph()

    def print_graph(self):
        for vertex in self.vertices.values():
            print(vertex.name, ': ', end='')

            adjacencies = self.adjacency_list[vertex.name]
            for i, edge in enumerate(adjacencies):
                print(f"{edge.end} ({edge.capacity})",
                      end=' -> ' if i < len(adjacencies) - 1 else '')
            print('')

    def __initialize_graph(self):
        for edge in self.edges:
            reverse = Edge(edge.end, edge.start, 0)
            edge.reverse = reverse
            reverse.reverse = edge
            self.adjacency_list[edge.start].append(edge)
            self.adjacency_list[edge.end].append(reverse)
