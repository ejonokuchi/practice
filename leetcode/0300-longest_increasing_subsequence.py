#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (47.21%)
# Total Accepted:    677.5K
# Total Submissions: 1.4M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting
# some or no elements without changing the order of the remaining elements. For
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#
#
# Example 1:
#
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
#
# Example 3:
#
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
#
#

from bisect import bisect_left
from collections import deque
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Greedily builds the longest increasing subsequence (LIS), using a bisection to
        replace existing elements when lower ones are found.

        Time  : O(n log n)
        Space : O(n)

        Although the new array does not always reflect the actual optimal solution, it
        will always capture an increasing subsequence, so its length is always equal
        to the length of the LIS thus far.

        For example, given nums = [10, 9, 10, 2, 5, 3, 7, 101, 18]:
            x = 10      -> L = [10]
            x = 9       -> L = [9]
            x = 10      -> L = [9, 10]
            x = 2       -> L = [2, 10]  * see note below
            x = 5       -> L = [2, 5]
            x = 3       -> L = [2, 3]
            x = 7       -> L = [2, 3, 7]
            x = 101     -> L = [2, 3, 7, 101]
            x = 18      -> L = [2, 3, 7, 18]

        * At this step, the new array is out-of-order. But [9, 10] is the LIS up to this
        point, and any future sequence starting from 2 will replace this value.
        """
        L = deque([nums[0]])
        for x in nums[1:]:
            if x > L[-1]:
                L.append(x)
            else:
                L[bisect_left(L, x)] = x
        return len(L)

    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        """
        Below is the classical dynamic programming solution.

        L[i] stores the value of the LIS of the sub-array ending at i.

        Recursion:
        L[i] = 1                if i == 0 or nums[i] < nums[j] ∀ j < i
             = max(L[j]) + 1    else, ∀ j < i where nums[i] > nums[j]

        Time  : O(n^2)
        Space : O(n)
        """
        L = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    L[i] = max(L[i], L[j] + 1)
        return max(L)
