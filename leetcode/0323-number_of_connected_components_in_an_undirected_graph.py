#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#
# algorithms
# Medium (59.72%)
# Total Accepted:    195K
# Total Submissions: 326.5K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
# You have a graph of n nodes. You are given an integer n and an array edges
# where edges[i] = [ai, bi] indicates that there is an edge between ai and bi
# in the graph.
#
# Return the number of connected components in the graph.
#
#
# Example 1:
#
#
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
#
#
# Example 2:
#
#
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.
#
#
#

from collections import deque
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Builds a graph and runs DFS from each node to propagate its color to each of the
        nodes connected to it.

        Time  : O(V + E)
        Space : O(V + E)
        """
        G = {i: set() for i in range(n)}
        for v, w in edges:
            G[v].add(w)
            G[w].add(v)

        colors = list(range(n))

        visited = set()
        queue = deque(range(n))
        while len(queue) > 0:
            v = queue.pop()
            if v in visited:
                continue
            visited.add(v)
            for w in G[v]:
                colors[w] = colors[v]
                queue.append(w)

        return len(set(colors))
