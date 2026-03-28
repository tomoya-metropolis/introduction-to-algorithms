from graph import Edge
from graph import Graph
from graph import Vertex
from graph import initialize_single_source
from graph import print_path
from graph import relax


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
            return False

    return True


if __name__ == '__main__':
    vertices = {}
    for name in "styxz":
        vertices[name] = Vertex(name)

    edges = []
    edges.append(Edge('s', 't', 6))
    edges.append(Edge('s', 'y', 7))
    edges.append(Edge('t', 'y', 8))
    edges.append(Edge('t', 'x', 5))
    edges.append(Edge('t', 'z', -4))
    edges.append(Edge('y', 'x', -3))
    edges.append(Edge('y', 'z', 9))
    edges.append(Edge('x', 't', -2))
    edges.append(Edge('z', 's', 2))
    edges.append(Edge('z', 'x', 7))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- Bellnam-Ford algorithms ---")
    has_no_cycle = bellman_ford(graph, vertices['s'])

    print("--- result ---")
    print(f"has no cycle = {has_no_cycle}")
    if has_no_cycle:
        for v in vertices.values():
            print(f"{v.name} ({v.distance}): ", end='')
            print_path(v, v.name)
            print('')
