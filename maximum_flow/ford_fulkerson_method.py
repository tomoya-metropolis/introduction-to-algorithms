from collections import deque

from graph import Edge
from graph import Graph
from graph import Vertex


def find_augmenting_path(graph: Graph, source: str, sink: str) -> list[Edge] | None:
    visited = {source}
    queue = deque([(source, [])])

    while queue:
        current, path = queue.popleft()
        if current == sink:
            return path
        for edge in graph.adjacency_list[current]:
            if edge.end not in visited and edge.residual_capacity > 0:
                visited.add(edge.end)
                queue.append((edge.end, path + [edge]))

    return None


def ford_fulkerson(graph: Graph, source: str, sink: str) -> int:
    max_flow = 0

    while (path := find_augmenting_path(graph, source, sink)) is not None:
        bottleneck = min(edge.residual_capacity for edge in path)
        for edge in path:
            edge.flow += bottleneck
            edge.reverse.flow -= bottleneck
        max_flow += bottleneck

    return max_flow


if __name__ == '__main__':
    vertex_names = ['s', 'v1', 'v2', 'v3', 'v4', 't']
    vertices = {}
    for vertex_name in vertex_names:
        vertices[vertex_name] = Vertex(vertex_name)

    edges = []
    edges.append(Edge('s', 'v1', 16))
    edges.append(Edge('s', 'v2', 13))
    edges.append(Edge('v1', 'v3', 12))
    edges.append(Edge('v2', 'v1', 4))
    edges.append(Edge('v2', 'v4', 14))
    edges.append(Edge('v3', 'v2', 9))
    edges.append(Edge('v3', 't', 20))
    edges.append(Edge('v4', 'v3', 7))
    edges.append(Edge('v4', 't', 4))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("\n--- max flow ---")
    result = ford_fulkerson(graph, 's', 't')
    print(f"max flow: {result}")
