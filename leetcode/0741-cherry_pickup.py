#
# @lc app=leetcode id=741 lang=python3
#
# [741] Cherry Pickup
#
# https://leetcode.com/problems/cherry-pickup/description/
#
# algorithms
# Hard (35.81%)
# Total Accepted:    45.1K
# Total Submissions: 125.9K
# Testcase Example:  '[[0,1,-1],[1,0,-1],[1,1,1]]'
#
# You are given an n x n grid representing a field of cherries, each cell is
# one of three possible integers.
#
#
# 0 means the cell is empty, so you can pass through,
# 1 means the cell contains a cherry that you can pick up and pass through,
# or
# -1 means the cell contains a thorn that blocks your way.
#
#
# Return the maximum number of cherries you can collect by following the rules
# below:
#
#
# Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right
# or down through valid path cells (cells with value 0 or 1).
# After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up
# through valid path cells.
# When passing through a path cell containing a cherry, you pick it up, and the
# cell becomes an empty cell 0.
# If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries
# can be collected.
#
#
#
# Example 1:
#
#
# Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
# Output: 5
# Explanation: The player started at (0, 0) and went down, down, right right to
# reach (2, 2).
# 4 cherries were picked up during this single trip, and the matrix becomes
# [[0,1,-1],[0,0,-1],[0,0,0]].
# Then, the player went left, up, up, left to return home, picking up one more
# cherry.
# The total number of cherries picked up is 5, and this is the maximum
# possible.
#
#
# Example 2:
#
#
# Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
# Output: 0
#
#
#
# Constraints:
#
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# grid[i][j] is -1, 0, or 1.
# grid[0][0] != -1
# grid[n - 1][n - 1] != -1
#
#
#

from functools import lru_cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        Memoized DP approach using depth-first search.

        If we consider paths of the structure A -> B -> C, then we build out solutions
        in a middle-out fashion, starting from the end location, B, and increasing the
        path in both directions, e.g. (B') -> B -> (B''), where B' is x steps before B
        on the outbound trip, and B'' is x steps after reaching B on the return trip.

        Let C[r1, c1, r2, c2] be the maximum number of cherries that can be picked up in
        a path from (r1, c1) to (n - 1, n - 1) and back to (r2, c2).

        Recursion:
        C[r1, c1, r2, c2] = -inf            if any position is out of bounds
                          = -inf            if either position is a thorn
                          = grid[r1][c1]    if the position is the end
                                            otherwise:
                          = num_cherries_here + max(
                              C[r1 + 1, c1, r2 + 1, c2],
                              C[r1 + 1, c1, r2, c2 + 1],
                              C[r1, c1 + 1, r2 + 1, c2],
                              C[r1, c1 + 1, r2, c2 + 1],
                          )

        where 'num_cherries_here' is the number of cherries at (r1, c1) and (r2, c2), or
        just (r1, c1) if the points are the same.

        Time  : O(n^4)
        Space : O(n^4)
        """
        n = len(grid)

        @lru_cache(None)
        def max_pickup(r1: int, c1: int, r2: int, c2: int) -> float:
            """
            Recursively computes and memoizes the maximum number of cherries attainable
            in a path from (r1, c1) to (n - 1, n - 1) and back to (r2, c2).

            Note: since steps are made simultaneously, if (r1, c1) == (n - 1, n - 1),
            and the bounds are valid, then (r2, c2) must also equal (n - 1, n - 1).
            """
            if r1 == n or c1 == n or r2 == n or c2 == n:
                return -float("inf")
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -float("inf")
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            num_cherries_here = (
                grid[r1][c1] if r1 == r2 and c1 == c2 else grid[r1][c1] + grid[r2][c2]
            )
            return num_cherries_here + max(
                max_pickup(r1 + 1, c1, r2 + 1, c2),
                max_pickup(r1 + 1, c1, r2, c2 + 1),
                max_pickup(r1, c1 + 1, r2 + 1, c2),
                max_pickup(r1, c1 + 1, r2, c2 + 1),
            )

        return max(max_pickup(0, 0, 0, 0), 0)
