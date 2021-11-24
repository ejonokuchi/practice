"""
Kahn's algorithm
----------------
Simple method for topological sorting.

"""


from collections import deque
from typing import List, Tuple


def find_topo_order(edges: List[Tuple[int, int]], n: int) -> List[int]:
    """
    Returns a valid topological sort of the vertices, given the directed edges.

    Builds a graph G to represent the dependencies as a DAG, and count the in-degree of
    each vertex, i.e. the number of inbound edges. Then run BFS from each vertex without
    a parent, and add each vertex to the ordering after its last inbound edge is
    accounted for.

    Time  : O(V + E)
    Space : O(V + E)

    where V is n, the number of vertices, and E is the number of edges.
    """
    G = {i: [] for i in range(n)}
    in_degrees = {i: 0 for i in range(n)}
    for u, v in edges:
        G[u].append(v)
        in_degrees[v] += 1

    ordering = []
    queue = deque([u for u in range(n) if in_degrees[u] == 0])
    while len(queue) > 0:
        u = queue.popleft()
        ordering.append(u)
        for v in G[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                queue.append(v)

    return ordering


def test_find_topo_order():
    """
    Graph:

       4       2
     ↙   ↘     ↓
    0     1    3
     ↘   ↙
       5

    """
    n = 6
    edges = [
        (4, 0),
        (4, 1),
        (2, 3),
        (0, 5),
        (1, 5),
    ]
    ordering = find_topo_order(edges, n)

    # Ensure topological invariant is met
    for u, v in edges:
        assert ordering.index(u) < ordering.index(v)
