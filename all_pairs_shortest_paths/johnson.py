from graph import Edge
from graph import Graph
from graph import Vertex
from graph import initialize_single_source
from graph import relax

import copy
import heapq


def bellman_ford(graph, s):
    initialize_single_source(graph, s)

    vertices = graph.vertices
    edges = graph.edges
    for i in range(len(vertices) - 1):
        for edge in edges:
            u = vertices[edge.start]
            v = vertices[edge.end]
            weight = edge.weight
            relax(u, v, weight)

    for edge in edges:
        u = vertices[edge.start]
        v = vertices[edge.end]
        weight = edge.weight
        if v.distance > u.distance + weight:
            return True

    return False


def dijkstra(graph, s):
    vertices = graph.vertices
    edges = graph.edges

    initialize_single_source(graph, s)

    vertices_list = list(vertices.values())
    heapq.heapify(vertices_list)

    while len(vertices_list):
        u = heapq.heappop(vertices_list)
        i = int(u.name)
        adjacencies = graph.adjacency_list[u.name]
        for e in adjacencies:
            v = vertices[e.end]
            j = int(v.name)
            weight = e.weight
            relax(u, v, weight)

            heapq.heapify(vertices_list)


def johnson(graph):
    vertices = graph.vertices
    edges = graph.edges
    vertices_new = copy.deepcopy(vertices)
    edges_new = copy.deepcopy(edges)

    vertices_new['s'] = Vertex('s')
    for i in graph.vertices.keys():
        edges_new.append(Edge('s', i, 0))

    graph_new = Graph(vertices_new, edges_new)

    print("--- extended graph ---")
    graph_new.print_graph()

    print("--- Bellman-Ford algorithm ---")
    has_cycle = bellman_ford(graph_new, vertices_new['s'])
    if has_cycle:
        print("Graph has a cycle.")

        return

    h = {}
    for v in vertices_new.values():
        h[v.name] = v.distance

    for edge_new in edges_new:
        start = edge_new.start
        end = edge_new.end
        if start == 's':
            edge_new.weight = h[start] - h[end]
        else:
            edge_new.weight = graph.edges_dict[f"{start}-{end}"] + \
                h[start] - h[end]

    print("--- update extended graph ---")
    graph_new.print_graph()

    del vertices_new['s']

    D = [[0 for _ in range(len(vertices))]
         for _ in range(len(vertices))]

    print("--- Dijstra's algortihm ---")
    for u in vertices_new.values():
        print(f"start vertex = {u.name}")

        dijkstra(graph_new, u)

        for v in vertices_new.values():
            i = int(u.name)
            j = int(v.name)
            D[i - 1][j - 1] = v.distance

    print("--- intermidate result ---")
    print_matrix(D)

    for i in range(len(D)):
        for j in range(len(D)):
            D[i][j] = D[i][j] + h[str(j + 1)] - h[str(i + 1)]

    return D


def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end=' ')

        print('')


if __name__ == '__main__':
    vertices = {}
    for i in "12345":
        vertices[i] = Vertex(i)

    edges = []
    edges.append(Edge('1', '2', 3))
    edges.append(Edge('1', '3', 8))
    edges.append(Edge('1', '5', -4))
    edges.append(Edge('2', '4', 1))
    edges.append(Edge('2', '5', 7))
    edges.append(Edge('3', '2', 4))
    edges.append(Edge('4', '1', 2))
    edges.append(Edge('4', '3', -5))
    edges.append(Edge('5', '4', 6))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- Johnson's algorithms ---")
    D = johnson(graph)

    print("--- result ---")
    print_matrix(D)
