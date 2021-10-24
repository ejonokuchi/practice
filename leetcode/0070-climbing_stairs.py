#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (49.98%)
# Total Accepted:    1.2M
# Total Submissions: 2.4M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#
# Constraints:
#
#
# 1 <= n <= 45
#
#
#


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Fibonacci sequence, with only the final number required.

        Recursion: S[i] = S[i - 1] + S[i - 2]

        Time  : O(n), where n is the value of the input
        Space : O(1)
        """
        a = 1  # current
        b = 0  # previous
        for _ in range(n):
            a, b = a + b, a
        return a
