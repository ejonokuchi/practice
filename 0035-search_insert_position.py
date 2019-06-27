#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (40.91%)
# Total Accepted:    409.2K
# Total Submissions: 1M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
#
# Input: [1,3,5,6], 5
# Output: 2
#
#
# Example 2:
#
#
# Input: [1,3,5,6], 2
# Output: 1
#
#
# Example 3:
#
#
# Input: [1,3,5,6], 7
# Output: 4
#
#
# Example 4:
#
#
# Input: [1,3,5,6], 0
# Output: 0
#
#

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Conducts a binary search on the nums array.

        """
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            ix = (l + r) // 2
            if nums[ix] < target:
                l = ix + 1
            elif nums[ix] > target:
                r = ix - 1
            else:
                return ix
        return l
