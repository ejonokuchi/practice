"""
K-means
-------
Simple spatial clustering algorithm based on Euclidean distance.

Standard libraries and numpy only.

"""

import numpy as np


def k_means_cluster(X: np.ndarray, k: int, max_iter: int = 100) -> np.ndarray:
    """
    Groups observations into k clusters based on Euclidean distance.

    Randomly initialize k clusters by choosing k observations at random.
    Then repeat the following until convergence:
    • Assign each data point to the nearest cluster
    • Re-compute the centroid of each cluster

    Time  : O(knm)
    Space : O(km + n)

    where (n, m) is the shape of the data matrix, and k is the number of clusters.

    Notes
    -----
    K-means is very sensitive to random initialization—for stable clustering, it's best
    to repeat several times with random starting values, and choose the clustering with
    the least within-cluster variance.

    Gaussian Mixture Models are preferred if the clusters are overlapping, or clusters
    have different variances.
    """
    n, m = X.shape

    # Random initialization of k clusters
    cluster_idxs = np.random.choice(a=n, size=k, replace=False)
    centroids = X[cluster_idxs]

    # Repeat until convergence
    prev_centroids = centroids
    for _ in range(max_iter):
        # Assign points to the nearest cluster centroid
        Y = np.full(n, -1, dtype=np.int32)
        for i in range(n):
            centroid_distances = np.linalg.norm(centroids - X[i], axis=1)
            Y[i] = np.argmin(centroid_distances)

        # Recompute cluster centroids
        centroids = np.array(
            [np.mean(X[Y == cluster_idx], axis=0) for cluster_idx in range(k)]
        )
        if np.all(centroids == prev_centroids):
            break

    return Y


def test_k_means_cluster():
    X = np.array(
        [
            [7, 9],
            [9, 6],
            [8, 8],
            [3, 4],
            [1, 0],
            [1, 2],
            [2, 2],
        ]
    )
    Y = np.array([0, 0, 0, 1, 1, 1, 1])

    clustering_is_correct = []
    for _ in range(10):
        clusters = k_means_cluster(X, k=2)
        clustering_is_correct.append(
            np.all(clusters == Y) or np.all(clusters == (-Y + 1))
        )

    assert any(clustering_is_correct)
