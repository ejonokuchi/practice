#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (51.85%)
# Total Accepted:    1.3M
# Total Submissions: 2.4M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
#
# Example 1:
#
#
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
#
#

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Runs depth-first search from each unvisited land cell to label all connected
        cells. The grid is modified in-place to mark each cell as visited.

        Time  : O(nm)
        Space : O(nm)
        """
        n, m = len(grid), len(grid[0])

        def label_connected(r: int, c: int):
            """Label all connected land cells with the current component index, via
            recursive DFS."""
            if 0 <= r < n and 0 <= c < m and grid[r][c] == "1":
                grid[r][c] = component_idx
                for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    label_connected(i, j)
            return

        component_idx = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    label_connected(r, c)
                    component_idx += 1
        return component_idx
