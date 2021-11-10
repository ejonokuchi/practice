"""
K-nearest neighbors
-------------------
Classifies new observations based on the majority class of the k-nearest neighbors.

Standard libraries only.

"""

import heapq
import math
from collections import Counter


def compute_distance(A, B):
    """Compute the Euclidean distance between A and B."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(A, B)))


class KNeighborsClassifier:
    """
    Given a set of observations with known classes, classify a new observation based on
    the classes of the nearest k observations.

    Uses a min-heap to find the k smallest distances over all observations, and returns
    the class with the maximum count.

    Time  : O(n log k)
    Space : O(n)

    Notes
    -----
    To optimize for many classifications and infrequent training, a k-d tree can be
    used. This results in the following time complexity:
        train()     : O(n log n)
        classify()  : O(n)
    """

    def __init__(self, k: int = 3):
        self.k = k

    def train(self, X, Y):
        self.X = X
        self.Y = Y

    def classify(self, x):
        distances = [compute_distance(x, neighbor) for neighbor in self.X]
        k_neighbor_heap = []
        for idx, d in enumerate(distances):
            if idx < self.k:
                heapq.heappush(k_neighbor_heap, (-d, idx))
            else:
                heapq.heappushpop(k_neighbor_heap, (-d, idx))

        k_distances, k_neighbor_idxs = zip(*k_neighbor_heap)
        k_neighbor_classes = [self.Y[idx] for idx in k_neighbor_idxs]
        return Counter(k_neighbor_classes).most_common(1)[0][0]


def test_knn():
    X = [
        [7, 7],
        [7, 4],
        [3, 4],
        [1, 4],
    ]
    Y = [0, 0, 1, 1]

    k = 3
    x = [3, 7]
    y = 1
    model = KNeighborsClassifier(k=k)
    model.train(X, Y)
    assert model.classify(x) == y
