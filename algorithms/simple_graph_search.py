"""
Simple Graph Search
-------------------
Given a graph as an adjacency list, return the path from the source to the target.

Implementations for Breadth-First Search (BFS) and Depth-First Search (DFS).

"""

from collections import deque
from typing import Dict, List


def breadth_first_search(G: Dict[str, List[str]], src: str, dst: str) -> List[str]:
    """
    Returns the shortest path from the source to the destination, or None if no such
    path exists.

    Time  : O(V + E)
    Space : O(V + E)
    """
    if src == dst:
        return []

    visited = dict()
    queue = deque([(src, None)])

    # traverse graph
    while len(queue) > 0:
        node, previous = queue.popleft()
        if node not in visited:
            visited[node] = previous  # record predecessor
            if node == dst:
                break
            queue.extend((v, node) for v in G[node] if v not in visited)
    if dst not in visited:
        return None

    # build path
    path = deque([])
    node = dst
    while node is not None:
        path.appendleft(node)
        node = visited[node]
    return list(path)


def depth_first_search(G: Dict[str, List[str]], src: str, dst: str) -> List[str]:
    """
    Returns the path from the source to the destination, or None if no such path exists.

    Same as BFS but with pop-right instead of pop-left.

    Time  : O(V + E)
    Space : O(V + E)
    """
    if src == dst:
        return []

    visited = dict()
    queue = deque([(src, None)])

    # traverse graph
    while len(queue) > 0:
        node, previous = queue.pop()
        if node not in visited:
            visited[node] = previous  # record predecessor
            if node == dst:
                break
            queue.extend((v, node) for v in G[node] if v not in visited)
    if dst not in visited:
        return None

    # build path
    path = deque([])
    node = dst
    while node is not None:
        path.appendleft(node)
        node = visited[node]
    return list(path)


def test_no_path():
    G = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": [],
        "E": [],
    }
    assert breadth_first_search(G, "A", "E") is None
    assert depth_first_search(G, "A", "E") is None


def test_null_path():
    G = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["E"],
        "E": [],
    }
    assert breadth_first_search(G, "A", "A") == []
    assert depth_first_search(G, "A", "A") == []


def test_one_path():
    G = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["E"],
        "E": [],
    }
    assert breadth_first_search(G, "A", "E") == ["A", "B", "C", "D", "E"]
    assert depth_first_search(G, "A", "E") == ["A", "B", "C", "D", "E"]


def test_split_path():
    G = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
        "D": [],
        "E": ["D"],
    }
    assert breadth_first_search(G, "A", "E") == ["A", "C", "E"]
    assert depth_first_search(G, "A", "E") == ["A", "C", "E"]


def test_cycle_path():
    G = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["B", "E"],
        "E": [],
    }
    assert breadth_first_search(G, "A", "E") == ["A", "B", "C", "D", "E"]
    assert depth_first_search(G, "A", "E") == ["A", "B", "C", "D", "E"]
