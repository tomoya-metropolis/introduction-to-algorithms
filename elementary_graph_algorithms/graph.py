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
        self.distance = 0
        self.predecessor = None


class Edge:

    def __init__(self, start, end):
        self.start = start
        self.end = end


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
            for i, adjacency in enumerate(adjacencies):
                print(adjacency, end=' -> ' if i < len(adjacencies) - 1 else '')

            print('')

    def __initialize_graph(self):
        for edge in self.edges:
            start = edge.start
            end = edge.end
            self.adjacency_list[start].append(end)
