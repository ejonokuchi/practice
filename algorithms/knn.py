"""
K-nearest neighbors
-------------------
Classifies new observations based on the majority class of the k-nearest neighbors.

Standard libraries and numpy only.

"""

import heapq
from collections import Counter

import numpy as np


class KNeighborsClassifier:
    """
    Given a set of observations with known classes, classify a new observation based on
    the classes of the nearest k observations.

    Uses a max-heap to find the k smallest distances over all observations, and returns
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

    def train(self, X: np.ndarray, Y: np.ndarray):
        """Records the input data to compute distances for inference."""
        self.n, self.m = X.shape
        assert Y.shape == (self.n,)
        self.X = X
        self.Y = Y

    def classify(self, x: np.ndarray) -> int:
        """Computes distances to all points, uses a max-heap to find the k smallest
        distances, and returns the majority class.

        Time  : O(n log k)
        Space : O(n)
        """
        assert x.shape == (self.m,)

        distances = np.linalg.norm(self.X - x, axis=1)
        k_neighbor_heap = [(-d, idx) for idx, d in enumerate(distances[: self.k])]
        heapq.heapify(k_neighbor_heap)
        for idx, d in enumerate(distances[self.k :], self.k):
            heapq.heappushpop(k_neighbor_heap, (-d, idx))

        k_distances, k_neighbor_idxs = zip(*k_neighbor_heap)
        k_neighbor_classes = self.Y[list(k_neighbor_idxs)]
        return Counter(k_neighbor_classes).most_common(1)[0][0]


def test_knn():
    X = np.array(
        [
            [7, 7],
            [7, 4],
            [3, 4],
            [1, 4],
        ]
    )
    Y = np.array([0, 0, 1, 1])

    k = 3
    x = np.array([3, 7])
    y = 1
    model = KNeighborsClassifier(k=k)
    model.train(X, Y)
    assert model.classify(x) == y
