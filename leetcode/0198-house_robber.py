#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Medium (44.85%)
# Total Accepted:    851.3K
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
#
#

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Returns the maximum amount obtained by robbing houses under the condition that
        adjacent houses can't be robbed.

        Recursion:

        M[i] = nums[0]                  if i == 0
             = max(nums[0], nums[1])    if i == 1
             = max(                     else
                 M[i - 2] + nums[i],
                 M[i - 1],
             )

        Since we never reference values further back than M[i - 2], we only need to
        store the last two values at any given point.

        Time  : O(n)
        Space : O(n)
        """
        n = len(nums)
        previous, current = 0, 0  # M[i - 2], M[i - 1]
        for i in range(n):
            previous, current = current, max(previous + nums[i], current)
        return current
