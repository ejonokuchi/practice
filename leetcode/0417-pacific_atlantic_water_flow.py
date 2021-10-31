#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (46.38%)
# Total Accepted:    148K
# Total Submissions: 319.1K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# There is an m x n rectangular island that borders both the Pacific Ocean and
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given an m x n
# integer matrix heights where heights[r][c] represents the height above sea
# level of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring
# cells directly north, south, east, and west if the neighboring cell's height
# is less than or equal to the current cell's height. Water can flow from any
# cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and
# Atlantic oceans.
#
#
# Example 1:
#
#
# Input: heights =
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#
#
# Example 2:
#
#
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
#
#
#
# Constraints:
#
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10^5
#
#
#

from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Runs BFS from each coast to determine the sets of cells with rainflow to each
        coast. Returns the intersection of the two sets.

        Time  : O(nm)
        Space : O(nm)
        """
        n, m = len(heights), len(heights[0])

        def can_flow_to(indices):
            """BFS from a set of indices to all equal or uphill neighbors."""
            visited = set()
            queue = deque(indices)
            while len(queue) > 0:
                r, c = queue.popleft()
                visited.add((r, c))
                for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= i < n
                        and 0 <= j < m
                        and (i, j) not in visited
                        and heights[i][j] >= heights[r][c]
                    ):
                        queue.append((i, j))
            return visited

        pacific_coast = [(i, 0) for i in range(n)] + [(0, j) for j in range(m)]
        atlantic_coast = [(i, m - 1) for i in range(n)] + [(n - 1, j) for j in range(m)]
        return list(can_flow_to(pacific_coast) & can_flow_to(atlantic_coast))

