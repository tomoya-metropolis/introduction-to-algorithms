from graph import Edge
from graph import Graph
from graph import Vertex

import heapq


def make_set(vertices):
    sets = {}
    for v in vertices.values():
        sets[v.name] = list()
        sets[v.name].append(v.name)

    return sets


def find_set(sets, name):
    for set in sets.values():
        if name in set:
            return set[0]

    return None


def union(sets, u, v):
    parent_of_u = find_set(sets, u)
    parent_of_v = find_set(sets, v)

    if not parent_of_u or not parent_of_v:
        return

    if parent_of_u < parent_of_v:
        sets[parent_of_u].extend(sets[parent_of_v])
        if v in sets:
            del sets[v]
    else:
        sets[parent_of_v].extend(sets[parent_of_u])
        if u in sets:
            del sets[u]


def kruskal(graph):
    vertices = graph.vertices
    edges = graph.edges

    sets = make_set(vertices)

    heapq.heapify(edges)

    results = []
    while len(edges) > 0:
        edge = heapq.heappop(edges)
        print(
            f"popped : start = {edge.start}, end = {edge.end}, weight = {edge.weight}")

        u = find_set(sets, edge.start)
        v = find_set(sets, edge.end)
        if u != v:
            print(f"union {u} and {v}.")
            union(sets, u, v)

            results.append(edge)

    return results


if __name__ == '__main__':
    vertices = {}
    for name in "abcdefghi":
        vertices[name] = Vertex(name)

    edges = []
    edges.append(Edge('a', 'b', 4))
    edges.append(Edge('a', 'h', 8))
    edges.append(Edge('b', 'a', 4))
    edges.append(Edge('b', 'c', 8))
    edges.append(Edge('b', 'h', 11))
    edges.append(Edge('c', 'b', 8))
    edges.append(Edge('c', 'd', 7))
    edges.append(Edge('c', 'f', 4))
    edges.append(Edge('c', 'i', 2))
    edges.append(Edge('d', 'c', 7))
    edges.append(Edge('d', 'e', 9))
    edges.append(Edge('d', 'f', 14))
    edges.append(Edge('e', 'd', 9))
    edges.append(Edge('e', 'f', 10))
    edges.append(Edge('f', 'c', 4))
    edges.append(Edge('f', 'd', 14))
    edges.append(Edge('f', 'e', 10))
    edges.append(Edge('f', 'g', 2))
    edges.append(Edge('g', 'f', 2))
    edges.append(Edge('g', 'h', 1))
    edges.append(Edge('g', 'i', 6))
    edges.append(Edge('h', 'a', 8))
    edges.append(Edge('h', 'b', 11))
    edges.append(Edge('h', 'g', 1))
    edges.append(Edge('h', 'i', 7))
    edges.append(Edge('i', 'c', 2))
    edges.append(Edge('i', 'g', 6))
    edges.append(Edge('i', 'h', 7))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- Kruskal's algorithm ---")
    results = kruskal(graph)

    print("--- results ---")
    total = 0
    for edge in results:
        print(f"start = {edge.start} end = {edge.end} weight = {edge.weight}")
        total += edge.weight
    print(f"total = {total}")
