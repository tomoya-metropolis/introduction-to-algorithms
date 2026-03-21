from graph import Edge
from graph import Graph
from graph import Vertex

import heapq
import sys


def prim(graph, r):
    vertices = graph.vertices
    vertices_list = list(vertices.values())
    edges = graph.edges

    for u in vertices_list:
        u.distance = sys.maxsize

    r.distance = 0

    heapq.heapify(vertices_list)

    while len(vertices_list) > 0:
        u = heapq.heappop(vertices_list)

        adjacencies = graph.adjacency_list[u.name]
        for (v_name, distance) in adjacencies:
            v = vertices[v_name]

            if v in vertices_list and v.distance > distance:
                print(
                    f"Update : target = {u.name}, adjacency = {v_name}, distance = {v.distance} -> {distance}")
                v.distance = distance
                v.predecessor = u
                vertices_list.remove(v)
                heapq.heappush(vertices_list, v)


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

    print("--- Prim's algorithms ---")
    prim(graph, vertices['a'])

    print("--- result ---")
    total = 0
    for v in vertices.values():
        print(f"{v.name}: predecessor = {v.predecessor.name if v.predecessor else '-'}, distance = {v.distance}")

        total += v.distance
    print(f"total = {total}")
