#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (47.32%)
# Total Accepted:    722.7K
# Total Submissions: 1.5M
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might
# become:
#
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
#
#
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum
# element of this array.
#
# You must write an algorithm that runs in O(log n) time.
#
#
# Example 1:
#
#
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
#
#
# Example 2:
#
#
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4
# times.
#
#
# Example 3:
#
#
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4
# times.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.
#
#
#

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Runs a modified binary search to find the discontinuity in the input array.

        At each iteration:
        • Select the middle element, and check for the discontinuity. If found, return.
        • If the leftmost element > the middle element, search the left half.
        • If the leftmost element < the middle element, search the right right.

        Time  : O(log n)
        Space : O(1)
        """
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[(mid + 1) % n]:
                return nums[(mid + 1) % n]
            elif nums[l] > nums[mid]:
                r = mid
            else:
                l = mid + 1
        return nums[(l + 1) % n]
