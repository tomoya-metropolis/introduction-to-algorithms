from collections import deque
from graph import Color
from graph import Edge
from graph import Graph
from graph import Vertex


time = 0


def depth_first_search(graph):
    vertices = graph.vertices

    for u in vertices.values():
        if u.color == Color.WHITE:
            depth_first_search_internal(graph, u)


def depth_first_search_internal(graph, u):
    vertices = graph.vertices
    adjacency_list = graph.adjacency_list

    global time
    time += 1

    u.color = Color.GRAY
    u.start = time
    print(f"{u.name} is discovered. start = {u.start}")

    adjacencies = adjacency_list[u.name]
    for adjacency in adjacencies:
        v = vertices[adjacency]
        if v.color == Color.WHITE:
            v.predecessor = u
            depth_first_search_internal(graph, v)

    time += 1
    u.color = Color.BLACK
    u.finish = time
    print(f"{u.name} finished. finish = {u.finish}")


def get_paths(u):
    paths = []
    while u:
        paths.append(u.name)

        u = u.predecessor

    paths.reverse()

    return paths


if __name__ == '__main__':
    vertices = {}
    for ch in 'uvyxwz':
        vertices[ch] = Vertex(ch)
    edges = []
    edges.append(Edge('u', 'v'))
    edges.append(Edge('u', 'x'))
    edges.append(Edge('v', 'y'))
    edges.append(Edge('y', 'x'))
    edges.append(Edge('x', 'v'))
    edges.append(Edge('w', 'y'))
    edges.append(Edge('w', 'z'))
    edges.append(Edge('z', 'z'))

    graph = Graph(vertices, edges)

    print("--- Graph ---")
    graph.print_graph()

    print("--- depth first search ---")
    depth_first_search(graph)

    print("--- result ---")
    for u in vertices.values():
        print(f"{u.name} ({u.start} / {u.finish}) : ", end=' ')
        paths = get_paths(u)
        print(' -> '.join(paths))
