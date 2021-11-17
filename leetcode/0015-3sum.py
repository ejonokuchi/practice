#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (29.61%)
# Total Accepted:    1.5M
# Total Submissions: 5.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
#
#
# Constraints:
#
#
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Computes valid triplets by repeatedly solving the 2-sum problem over the sorted
        input array.

        For each element x at index i, set up two pointers, j and k, at i + 1 and n - 1.
        Check the three-sum for this triplet. If it's too low, slide the left pointer to
        the middle. If it's too high, slide the right pointer to the middle.

        Time  : O(n^2)
        Space : O(n)

        Examples
        --------
        Given:
        sorted(nums) = [-2 -1 0 2 5]

        [-2 -1 0 2 5]
          i  j     k

        --> -2 + -1 + 5 = 2
        --> 2 is too high, k-- will decrease the sum.

        [-2 -1 0 2 5]
          i  j   k

        --> -2 + -1 + 2 = -1
        --> -1 is too low, j++ will increase the sum.

        [-2 -1 0 2 5]
          i    j k

        --> -2 + 0 + 2 = 0
        --> Sum is 0, save this triplet. Since j now crosses k, all solutions including
        nums[i] have now been considered.

        """
        n = len(nums)
        nums.sort()
        solutions = set()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates
                continue
            # Solve two-sum for target of nums[i].
            target = -nums[i]
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    solutions.add(tuple(sorted((nums[i], nums[j], nums[k]))))
                    while j < k and nums[j] == nums[j + 1]:  # skip duplicates
                        j += 1
                    j += 1

        return [list(x) for x in solutions]
