#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.96%)
# Total Accepted:    523.6K
# Total Submissions: 1.1M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Returns the longest consecutive sequence of numbers in the input array.

        Creates a set from the input array. For each element x which is the lowest
        number in a consecutive sequence (i.e. x - 1 is not present), count the number
        of consecutive elements starting from x.

        Time  : O(n)
        Space : O(n)
        """
        S = set(nums)
        max_count = 0
        for x in S:
            if x - 1 not in S:
                y = x + 1
                while y in S:
                    y += 1
                max_count = max(max_count, y - x)
        return max_count
