from graph import Edge
from graph import Graph
from graph import Vertex
from graph import initialize_single_source
from graph import print_path
from graph import relax

import heapq


def dijkstra(graph, s):
    initialize_single_source(graph, s)

    vertex_list = list(graph.vertices.values())
    heapq.heapify(vertex_list)

    while len(vertex_list) > 0:
        u = heapq.heappop(vertex_list)
        print(f"target: {u.name}")

        adjacencies = graph.adjacency_list[u.name]
        for (name, weight) in adjacencies:
            v = vertices[name]
            relax(u, v, weight)

            heapq.heapify(vertex_list)


if __name__ == '__main__':
    vertices = {}
    for name in "styxz":
        vertices[name] = Vertex(name)

    edges = []
    edges.append(Edge('s', 't', 10))
    edges.append(Edge('s', 'y', 5))
    edges.append(Edge('t', 'y', 2))
    edges.append(Edge('t', 'x', 1))
    edges.append(Edge('y', 't', 3))
    edges.append(Edge('y', 'x', 9))
    edges.append(Edge('y', 'z', 2))
    edges.append(Edge('x', 'z', 4))
    edges.append(Edge('z', 's', 7))
    edges.append(Edge('z', 'x', 6))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- Dijkstra algorithms ---")
    dijkstra(graph, vertices['s'])

    print("--- result ---")
    for v in vertices.values():
        print(f"{v.name} ({v.distance}) : ", end='')
        print_path(v, v.name)
        print('')
