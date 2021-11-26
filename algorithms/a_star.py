"""
A* Search
---------
Heuristic-based search for the shortest path in a graph.

See https://en.wikipedia.org/wiki/A*_search_algorithm

"""

import heapq
from typing import List, Tuple


class MinHeap:
    """
    Min-heap implementation supporting updates to existing elements in constant time.

    Maintains a standard heap and a dictionary of current values for each element,
    allowing duplicates in the heap.

    Parameters
    ----------
    elements : [(int, int)]
        List of elements as (x, value).

    Methods
    -------
    add(x : int, value: float) ->  None
        Adds x to the heap, and updates its value in the dictionary.
        The heap may contain multiple copies of x.
    pop() -> (int, float)
        Returns the minimum element from the heap. Pops from the heap until an element
        is found with a value matching its current value in the dictionary.
    """

    def __init__(self, elements: List[Tuple[int, float]]):
        self.heap = [(val, x) for x, val in elements]
        self.elements = {x: val for x, val in elements}
        heapq.heapify(self.heap)

    def __len__(self) -> int:
        """Returns the number of elements."""
        return len(self.elements)

    def __contains__(self, x: int) -> bool:
        """Returns True if x is an element of the MinHeap."""
        return x in self.elements

    def add(self, x: int, value: float):
        """Adds an element x to the MinHeap and updates the value in the dictionary."""
        if x in self.elements and self.elements[x] == value:
            return
        self.elements[x] = value
        heapq.heappush(self.heap, (value, x))
        return

    def pop(self) -> Tuple[int, float]:
        """Returns the minimum valid element from the heap."""
        val, x = heapq.heappop(self.heap)
        while x not in self.elements or self.elements[x] != val:
            val, x = heapq.heappop(self.heap)
        del self.elements[x]
        return x, val


def find_shortest_path(
    grid: List[List[float]],
    src: Tuple[int, int],
    dst: Tuple[int, int],
) -> List[Tuple[int, int]]:
    """
    Finds the shortest path in a grid via A-star heuristic search.

    Let grid[i, j] = 0      if location (i, j) is blocked and cannot be traversed
                   = c      if passing through location (i, j) has cost c, c > 0

    A* proceeds as follows:
    • Choose the frontier node u with the minimum estimated cost to the destination.
    • For each neighbor v of u:
        • If the path to v through u is better than the current path to v:
            • Record u as the predecessor of v in the shortest known path to v.
            • Estimate the cost from v to the destination with heuristic function h(v).
            • Add v to the frontier with its estimated cost.

    Time  : O(E), or O(b^d)
    Space : O(V), or O(b^d)

    where V is the number of vertices (nm), E is the number of edges (4nm), b is the
    branching factor (4), and d is the solution depth, or path length.
    """
    n, m = len(grid), len(grid[0])

    def _h(v: Tuple[int, int]) -> float:
        """Heuristic function for path selection. Estimates cost from v --> dst as the
        cost of going through v plus the manhattan distance between v to dst.
        """
        return grid[v[0]][v[1]] + abs(dst[0] - v[0]) + abs(dst[1] - v[1])

    # prev[u] is the predecessor of u in shortest known path to u
    prev = dict()
    # cost[u] is the cost of the shortest path from src --> u
    cost = {(i, j): float("inf") for i in range(n) for j in range(m)}

    prev[src] = src
    cost[src] = 0
    queue = MinHeap([(src, _h(src))])
    while len(queue) > 0:
        # Choose the frontier node with the minimum estimated cost to the destination
        u, _ = queue.pop()
        if u == dst:
            # Build path by traversing predecessors
            path = [dst]
            u = dst
            while u != prev[u]:
                u = prev[u]
                path.append(u)
            return path[::-1]

        # Explore neighbors
        r, c = u
        for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if not (0 <= i < n and 0 <= j < m) or grid[i][j] == 0:
                continue
            v = (i, j)
            # If the path to neighbor v through u is better than the existing path to v
            cost_to_v_through_u = cost[u] + grid[r][c]
            if cost_to_v_through_u < cost[v]:
                prev[v] = u
                cost[v] = cost_to_v_through_u
                est_cost_to_dst = cost[v] + _h(v)
                queue.add(x=v, value=est_cost_to_dst)
    return None


def test_find_shortest_path():
    grid = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 5, 1],
        [1, 1, 5, 1, 1],
        [1, 5, 1, 1, 1],
        [5, 1, 1, 1, 1],
    ]
    src = (0, 0)
    dst = (4, 4)
    shortest_path = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 4),
    ]

    path = find_shortest_path(grid, src, dst)
    assert all(x == y for x, y in zip(path, shortest_path))


def test_find_shortest_path_2():
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 9, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]
    src = (2, 1)
    dst = (2, 3)
    find_shortest_path(grid, src, dst)

    shortest_path = [(2, 1), (2, 2), (2, 3)]

    path = find_shortest_path(grid, src, dst)
    assert all(x == y for x, y in zip(path, shortest_path))


def test_find_shortest_path_3():
    grid = [
        [1, 20, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 20, 1],
    ]
    src = (0, 0)
    dst = (4, 4)
    shortest_path = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (4, 1),
        (4, 2),
        (3, 2),
        (2, 2),
        (1, 2),
        (0, 2),
        (0, 3),
        (0, 4),
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 4),
    ]

    path = find_shortest_path(grid, src, dst)
    assert all(x == y for x, y in zip(path, shortest_path))


def test_find_shortest_path_none():
    grid = [
        [1, 1, 1, 1, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1],
        [0, 1, 1, 1, 1],
    ]
    src = (0, 0)
    dst = (4, 4)
    find_shortest_path(grid, src, dst)

    path = find_shortest_path(grid, src, dst)
    assert path is None
