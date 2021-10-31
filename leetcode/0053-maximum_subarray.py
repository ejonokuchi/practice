#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (48.87%)
# Total Accepted:    1.7M
# Total Submissions: 3.6M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
#
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: 1
#
#
# Example 3:
#
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
#

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Runs Kadane's algorithm on the input array.

        Current sum is the maximum continuous sum up to the current array index.
        At each step, if the current sum is negative, the current element is larger
        without it. If the current sum is positive, the current element is added to it.

        Time  : O(n)
        Space : O(n)
        """
        current_sum = max_sum = nums[0]
        for x in nums[1:]:
            current_sum = max(x, current_sum + x)
            max_sum = max(max_sum, current_sum)
        return max_sum

