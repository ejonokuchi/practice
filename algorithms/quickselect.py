"""
Quickselect
-----------
Given a list of integers, find the kth lowest element (0 < k <= n).

"""

import random
from typing import List


def quickselect(A: List[int], k: int) -> int:
    """
    Returns an element of rank k from an unsorted list.

    Time  :
    Space :
    """
    pass


def quickselect_inplace(A: List[int], k: int) -> int:
    """
    Returns an element of rank k from an unsorted list, in-place (constant memory).

    Time  :
    Space :
    """
    pass


def test_quickselect_1():
    A = [random.randint(0, 100000) for _ in range(1000)]
    k = 514
    assert quickselect(A, k) == sorted(A)[k - 1]
    assert quickselect_inplace(A, k) == sorted(A)[k - 1]


def test_quickselect_2():
    A = [random.randint(0, 100000) for _ in range(1000)]
    k = 10
    assert quickselect(A, k) == sorted(A)[k - 1]
    assert quickselect_inplace(A, k) == sorted(A)[k - 1]
