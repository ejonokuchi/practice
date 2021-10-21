"""
Breadth-First Search (BFS)
--------------------------
Given a graph as an adjacency list, return the path from the source to the target,
traversing in a breadth-first manner.

"""

from typing import Dict, List


def breadth_first_search(G: Dict[str, List[str]], src: str, dst: str) -> List[str]:
    """
    Returns the path from the source to the destination, or None if no such path exists.

    Time  :
    Space :
    """
    pass


def test_breadth_first_search_one_path():
    G = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["E"],
        "E": [],
    }
    assert breadth_first_search(G, "A", "E") == ["A", "B", "C", "D", "E"]


def test_breadth_first_search_split_path():
    G = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
        "D": [],
        "E": ["D"],
    }
    assert breadth_first_search(G, "A", "E") == ["A", "B", "C", "D", "E"]
