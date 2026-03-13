from collections import deque
from graph import Color
from graph import Edge
from graph import Graph
from graph import Vertex


def breadth_first_search(graph, s):
    s.color = Color.GRAY

    print(f"{s.name} color : Gray")

    queue = deque()
    queue.append(s)
    while len(queue):
        u = queue.popleft()
        adjacencies = graph.adjacency_list[u.name]
        for adjacency in adjacencies:
            v = vertices[adjacency]
            if v.color == Color.WHITE:
                print(f"{v.name} color : Gray")
                print(f"{v.name} distance : {u.distance + 1}")

                v.color = Color.GRAY
                v.predecessor = u
                v.distance = u.distance + 1

                queue.append(v)

        print(f"{u.name} color : Black")


def print_path(s, v, v_name):
    if not v:
        return
    else:
        print_path(s, v.predecessor, v_name)
        print(v.name, end=' -> ' if v.name != v_name else '')


if __name__ == '__main__':
    vertices = {}
    vertices['s'] = Vertex('s')
    vertices['r'] = Vertex('r')
    vertices['v'] = Vertex('v')
    vertices['u'] = Vertex('u')
    vertices['t'] = Vertex('t')
    vertices['y'] = Vertex('y')
    vertices['w'] = Vertex('w')
    vertices['x'] = Vertex('x')
    vertices['z'] = Vertex('z')

    edges = []
    edges.append(Edge('s', 'r'))
    edges.append(Edge('s', 'v'))
    edges.append(Edge('s', 'u'))
    edges.append(Edge('r', 's'))
    edges.append(Edge('r', 't'))
    edges.append(Edge('r', 'w'))
    edges.append(Edge('v', 's'))
    edges.append(Edge('v', 'y'))
    edges.append(Edge('v', 'w'))
    edges.append(Edge('u', 's'))
    edges.append(Edge('u', 't'))
    edges.append(Edge('u', 'y'))
    edges.append(Edge('t', 'r'))
    edges.append(Edge('t', 'u'))
    edges.append(Edge('y', 'v'))
    edges.append(Edge('y', 'u'))
    edges.append(Edge('w', 'r'))
    edges.append(Edge('w', 'v'))
    edges.append(Edge('w', 'x'))
    edges.append(Edge('w', 'z'))
    edges.append(Edge('x', 'y'))
    edges.append(Edge('x', 'w'))
    edges.append(Edge('x', 'z'))
    edges.append(Edge('z', 'w'))
    edges.append(Edge('z', 'x'))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- breadth first searc ---")
    breadth_first_search(graph, vertices['s'])

    print("--- result ---")
    for v in vertices.values():
        print(f"{v.name} ({v.distance}) : ", end='')
        print_path(vertices['s'], v, v.name)
        print('')
