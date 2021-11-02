"""
0-1 Knapsack Problem
--------------------
Given an array of items, each with a value and a weight.

Return the maximum total value attained by choosing a subset of items that do not exceed
the weight limit.

"""

from functools import lru_cache
from typing import Dict, List


def knapsack_rec(items: List[Dict[str, int]], max_weight: int) -> int:
    """
    Recursive solution to the 0-1 knapsack problem with memoization.

    Uses an LRU cache to memoize the values of recursive function calls to compute
    V[i, W], the max value obtained in a knapsack considering items up to i with total
    weight <= W.

    Recursion:
    V[i, W] = V[i - 1, W]               if w > W    (can't take item i)
            = max(                      else        (the greater of taking or leaving i)
                V[i - 1, W - w] + v,
                V[i - 1, W]
            )

    where item i has weight w and value v.

    Time  : O(nW)
    Space : O(m), where m is the maxsize of the memoization table
    """

    @lru_cache(maxsize=128)
    def V(i, W):
        if i < 0:
            return 0
        v, w = items[i]["value"], items[i]["weight"]
        return max(V(i - 1, W - w) + v if w <= W else 0, V(i - 1, W))

    return V(len(items) - 1, max_weight)


def knapsack(items: List[Dict[str, int]], max_weight: int) -> int:
    """
    Iterative dynamic programming solution to the 0-1 knapsack problem.

    Creates the same table of values V[i, W] as above, completely filling out all
    values.

    Recursion:
    V[i, W] = V[i - 1, W]               if w > W    (can't take item i)
            = max(                      else        (the greater of taking or leaving i)
                V[i - 1, W - w] + v,
                V[i - 1, W]
            )

    where item i has weight w and value v.

    Time  : O(nW)
    Space : O(nW)
    """
    V = [[0 for _ in range(max_weight + 1)] for _ in range(len(items) + 1)]
    for i, item in enumerate(items, 1):
        v, w = item["value"], item["weight"]
        for W in range(max_weight + 1):
            V[i][W] = max(V[i - 1][W - w] + v if w <= W else 0, V[i - 1][W])
    return V[len(items)][max_weight]


def unbounded_knapsack(items: List[Dict[str, int]], max_weight: int) -> int:
    """
    Iterative dynamic programming solution to the unbounded knapsack problem.

    In the unbounded variation of the problem, any number of each item i can be taken.

    Recursion:
    V[i, W] = max(V[i - 1, W], V[i, W - w] + v)     for items[i] with weight w, value v

    where only the previous i - 1 row is needed for each iteration.

    Time  : O(nW)
    Space : O(W)
    """
    V = [0] * (max_weight + 1)
    for item in items:
        for W in range(item["weight"], max_weight + 1):
            V[W] = max(V[W], V[W - item["weight"]] + item["value"])
    return V[max_weight]


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


def test_unbounded_knapsack():
    items = [
        {"weight": 3, "value": 5},
        {"weight": 1, "value": 1},
        {"weight": 2, "value": 3},
    ]
    assert unbounded_knapsack(items, 2) == 3
    assert unbounded_knapsack(items, 6) == 10
    assert unbounded_knapsack(items, 8) == 13
    assert unbounded_knapsack(items, 10) == 16
