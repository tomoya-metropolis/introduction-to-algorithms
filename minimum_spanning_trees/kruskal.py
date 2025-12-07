from graph import Edge
from graph import Graph
from graph import Vertex

import heapq


def find_parent(sets, ch):
    for s in sets.values():
        if ch in s:
            return s

    return None


def union(sets, u, v):
    s = find_parent(sets, u)
    t = find_parent(sets, v)
    if u < v:
        s.extend(t)
        del t
    else:
        t.extend(s)
        del u


def kruskal(graph):
    vertices = graph.vertices
    edges = graph.edges

    sets = {}
    for v in vertices.values():
        sets[v.name] = list()
        sets[v.name].append(v.name)

    heapq.heapify(edges)

    results = []
    while len(edges):
        edge = heapq.heappop(edges)
        start, end, weight = edge.start, edge.end, edge.weight
        if find_parent(sets, start) != find_parent(sets, end):
            print(f"start = {start}, end={end}, weight={weight}")

            union(sets, start, end)
            results.append((start, end, weight))

    return results


if __name__ == '__main__':
    vertices = {}
    for name in 'abcdefghi':
        vertices[name] = Vertex(name)

    edges = list()
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

    print("--- Kruslal's algorithm ---")
    results = kruskal(graph)

    print("--- minimum spanning tree ---")
    weight = 0
    for (s, e, w) in results:
        print(f"start = {s}, end = {e}, weight = {w}")
        weight += w
    print(f"total = {weight}")
