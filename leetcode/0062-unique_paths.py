#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (58.00%)
# Total Accepted:    748K
# Total Submissions: 1.3M
# Testcase Example:  '3\n7'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# How many possible unique paths are there?
#
#
# Example 1:
#
#
# Input: m = 3, n = 7
# Output: 28
#
#
# Example 2:
#
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#
#
# Example 3:
#
#
# Input: m = 7, n = 3
# Output: 28
#
#
# Example 4:
#
#
# Input: m = 3, n = 3
# Output: 6
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10^9.
#
#
#

from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Computes the number of unique paths as a combination.

        Given a grid of size (m, n), we want to move from the upper left space, (0, 0),
        to the bottom right space, (m - 1, n - 1). Thus, we have to take (m - 1) steps
        down and (n - 1) steps right, that can be made in any order.

        This can be visualized as an array of moves down (↓) or right (→):
            e.g. [↓, ↓, →, →, →] for m = 3 and n = 4.

        The total number of unique paths is thus given by the unique permutations of
        this array: T! / (D! R!)

        where:
            • T is the total number of moves = (m - 1 + n - 1)
            • D is the number of down moves = (m - 1)
            • R is the number of right moves = (n - 1)

        This can be considered as the number of ways to choose D elements from T, i.e.
        D choose T, or the number of ways to arrange T elements where there are D and R
        repeated elements.

        Time  : O(mn)
        Space : O(1)
        """
        return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))
