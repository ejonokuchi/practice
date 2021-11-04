"""
Quickselect
-----------
Given a list of integers, find the kth lowest element (0 < k <= n).

"""

import random
from collections import deque
from typing import List


def quickselect(A: List[int], k: int) -> int:
    """
    Returns an element of rank k from an unsorted list.

    Stable selection algorithm.

    Time  : O(n) average, O(n^2) worst
    Space : O(n)
    """
    # Pivot selection
    # Use median-of-three to avoid worst-case where pivot is the min or max.
    if len(A) >= 3:
        idx_sample = random.sample(range(len(A)), 3)
        pivot = sorted(A[idx] for idx in idx_sample)[1]
    else:
        pivot = A[0]

    # Partition
    # Use 3 arrays instead of 2 to cut recursion depth for inputs with many repeats.
    L, M, R = deque([]), deque([]), deque([])
    for x in A:
        if x < pivot:
            L.append(x)
        elif x == pivot:
            M.append(x)
        else:
            R.append(x)

    # Recurse
    if k <= len(L):
        return quickselect(list(L), k)
    elif k <= (len(L) + len(M)):
        return M[k - len(L) - 1]  # stability condition
    else:
        return quickselect(list(R), k - len(L) - len(M))


def test_quickselect_few_repeats():
    for _ in range(100):
        A = [random.randint(0, 100000) for _ in range(100)]
        k = 10
        assert quickselect(A, k) == sorted(A)[k - 1]


def test_quickselect_many_repeats():
    for _ in range(100):
        A = [random.randint(0, 1000) for _ in range(1000)]
        k = 514
        assert quickselect(A, k) == sorted(A)[k - 1]
