#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (24.12%)
# Total Accepted:    565K
# Total Submissions: 2.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#
class Solution:
    def threeSum(self, l):
        n = len(l)
        if n < 3:
            return []

        s = set(l)
        solutions = set()
        for i in range(n - 1):
            for j in range(i + 1, n):
                x = -(l[i] + l[j])
                if x in s and (l[i] != x and l[j] != x):
                    solutions.add(tuple(sorted((l[i], l[j], x))))
        if l.count(0) > 2:
            solutions.add((0, 0, 0))
        return [list(tup) for tup in solutions]