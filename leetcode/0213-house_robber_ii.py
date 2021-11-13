#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (38.68%)
# Total Accepted:    294.9K
# Total Submissions: 762.4K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have a security system connected, and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
#
#
# Example 1:
#
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2), because they are adjacent houses.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 3:
#
#
# Input: nums = [1,2,3]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
#
#
#

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Returns the maximum amount obtained by robbing houses under the condition that
        adjacent houses can't be robbed, and the first and last houses are adjacent.

        Recursion:

        M[i] = nums[0]                  if i == 0
             = max(nums[0], nums[1])    if i == 1
             = max(                     else
                 M[i - 2] + nums[i],
                 M[i - 1],
             )

        Since values further back than i - 2 are never referenced, we only need to store
        the last two values at any given point.

        To ensure only one of the first or last house is taken, returns the maximum of
        the result on the houses from [1, n] and [0, n - 1]. The first element of the
        array is also included, in case it is the only element in the input.

        Time  : O(n)
        Space : O(1)
        """
        n = len(nums)

        def _rob(i: int = 0, j: int = n) -> int:
            """
            Returns the maximum amount obtained by robbing houses from index i to j,
            under the condition that adjacent houses can't be robbed. See Problem 198.
            """
            previous, current = 0, 0  # M[i - 2], M[i - 1]
            for idx in range(i, j):
                previous, current = current, max(previous + nums[idx], current)
            return current

        return max(_rob(1, n), _rob(0, n - 1), nums[0])
