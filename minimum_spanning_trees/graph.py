from collections import defaultdict

import enum


class Color(enum.Enum):

    WHITE = 'white'
    GRAY = 'gray'
    BLACK = 'black'


class Vertex:

    def __init__(self, name):
        self.name = name
        self.color = Color.WHITE
        self.predecessor = None
        self.distance = 0

    def __lt__(self, other):
        return self.distance < other.distance


class Edge:

    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = defaultdict(list)

        self.__initialize_graph()

    def print_graph(self):
        for vertex in self.vertices.values():
            print(vertex.name, ": ", end='')
            adjacencies = self.adjacency_list[vertex.name]
            for i, (adjacency, weight) in enumerate(adjacencies):
                print(f"{adjacency}({weight})", end=' -> ' if i <
                      len(adjacencies) - 1 else '')

            print('')

    def __initialize_graph(self):
        for edge in self.edges:
            start = edge.start
            end = edge.end
            weight = edge.weight
            self.adjacency_list[start].append((end, weight))
