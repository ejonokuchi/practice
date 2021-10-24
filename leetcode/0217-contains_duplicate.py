#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (58.90%)
# Total Accepted:    1M
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,3,1]'
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
#
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Compare the set length to the original list length.

        Time  : O(n)
        Space : O(n)
        """
        return len(set(nums)) < len(nums)
