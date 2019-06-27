#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.77%)
# Total Accepted:    352.6K
# Total Submissions: 770.5K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
#
# Example:
#
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#

from typing import List

import itertools

class Solution:
    def threeSumClosest(self,
        l: List[int],
        target: int,
    ) -> int:
        """
        Finds the triplet sum closest to the target value.

        Sorts the array, fixes the first element of the triplet, and then uses
        a two pointer paradigm to check all pairs. Since the array is sorted,
        we know which pointer to move to guarantee that we move towards the
        target value.

        Time: O(n^2)
        Space: O(1)

        """
        n = len(l)
        l.sort()
        closest = l[0] + l[1] + l[2]
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                x = l[i] + l[j] + l[k]
                if abs(target - x) < abs(target - closest):
                    closest = x
                if x < target:  # too low, slide left pointer in
                    j += 1
                elif x > target:  # too high, slide right pointer in
                    k -= 1
                else:
                    return x
        return closest
