"""
0-1 Knapsack Problem
--------------------
Given an array of items, each with a value and a weight.

Return the maximum total value attained by choosing a subset of items that do not exceed
the weight limit.

"""

from typing import Dict, List


def knapsack_rec(items: List[Dict[str, int]], max_weight: int) -> int:
    """
    Recursive solution to the 0-1 knapsack problem with memoization.

    Time  :
    Space :
    """
    pass


def knapsack(items: List[Dict[str, int]], max_weight: int) -> int:
    """
    Iterative dynamic programming solution to the 0-1 knapsack problem.

    Time  :
    Space :
    """
    pass


def test_knapsack_rec():
    items = [
        {"weight": 10, "value": 5},
        {"weight": 17, "value": 25},
        {"weight": 8, "value": 2},
        {"weight": 9, "value": 9},
        {"weight": 12, "value": 7},
    ]
    assert knapsack_rec(items, 8) == 2
    assert knapsack_rec(items, 9) == 9
    assert knapsack_rec(items, 13) == 9
    assert knapsack_rec(items, 17) == 25


def test_knapsack():
    items = [
        {"weight": 10, "value": 5},
        {"weight": 17, "value": 25},
        {"weight": 8, "value": 2},
        {"weight": 9, "value": 9},
        {"weight": 12, "value": 7},
    ]
    assert knapsack(items, 8) == 2
    assert knapsack(items, 9) == 9
    assert knapsack(items, 13) == 9
    assert knapsack(items, 17) == 25
