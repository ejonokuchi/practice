#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Easy (71.90%)
# Total Accepted:    428.4K
# Total Submissions: 595.8K
# Testcase Example:  '2'
#
# Given an integer n, return an array ans of length n + 1 such that for each i
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of
# i.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#
#
# Example 2:
#
#
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^5
#
#
#
# Follow up:
#
#
# It is very easy to come up with a solution with a runtime of O(n log n). Can
# you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like
# __builtin_popcount in C++)?
#
#
#

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Sets bit counts iteratively:
        • For any even number x, bin(x) is the same as bin(x/2), but with a trailing 0.
        • For any odd number x, bin(x) is the same as bin(x//2), but with a trailing 1.

        Examples:
        • 6  => 110     3  => 11
        • 25 => 11001   12 => 1100

        Recursion:
        B[x] = B[x // 2]        if x is even
             = B[x // 2] + 1    if x is odd

        Time  : O(n)
        Space : O(n)
        """
        B = [0] * (n + 1)
        for x in range(0, n + 1):
            B[x] = B[x >> 1] + x % 2
        return B
