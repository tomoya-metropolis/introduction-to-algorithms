from collections import deque
from graph import Color
from graph import Edge
from graph import Graph
from graph import Vertex


def breadth_first_search(graph, s):
    vertices = graph.vertices
    edges = graph.edges

    s.color = Color.GRAY
    s.distance = 0
    s.predecessor = None
    print(f"{s.name} is discovered. distance = {s.distance}")

    queue = deque()
    queue.append(s)

    while queue:
        u = queue.popleft()
        print(f"targte vertex = {u.name}")

        for v_name in graph.adjacency_list[u.name]:
            v = vertices[v_name]
            if v.color == Color.WHITE:
                v.color = Color.GRAY
                v.distance = u.distance + 1
                v.predecessor = u
                print(
                    f"{v.name} is discovered. distance = {v.distance} / predecessor = {v.predecessor.name}")

                queue.append(v)

        u.color = Color.BLACK
        print(f"{u.name} finished")


def print_path(vertices, s, u):
    if s == u:
        print(u.name, end=' ')
    elif not u.predecessor:
        return
    else:
        print_path(vertices, s, u.predecessor)
        print(u.name, end=' ')


if __name__ == '__main__':
    vertices = {}
    for ch in 'srvwxtuy':
        vertices[ch] = Vertex(ch)
    edges = []
    edges.append(Edge('s', 'r'))
    edges.append(Edge('s', 'w'))
    edges.append(Edge('r', 's'))
    edges.append(Edge('r', 'v'))
    edges.append(Edge('v', 'r'))
    edges.append(Edge('w', 's'))
    edges.append(Edge('w', 'x'))
    edges.append(Edge('w', 't'))
    edges.append(Edge('x', 'w'))
    edges.append(Edge('x', 't'))
    edges.append(Edge('x', 'u'))
    edges.append(Edge('x', 'y'))
    edges.append(Edge('t', 'w'))
    edges.append(Edge('t', 'x'))
    edges.append(Edge('t', 'u'))
    edges.append(Edge('u', 't'))
    edges.append(Edge('u', 'x'))
    edges.append(Edge('u', 'y'))
    edges.append(Edge('y', 'x'))
    edges.append(Edge('y', 'u'))

    graph = Graph(vertices, edges)

    print("--- Graph ---")
    graph.print_graph()

    print("--- breadth first search ---")
    breadth_first_search(graph, vertices['s'])

    print("--- result ---")
    for u in vertices.values():
        print(f"{u.name} ({u.distance}) : ", end='')
        print_path(vertices, vertices['s'], u)
        print('')
