#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (48.85%)
# Total Accepted:    350.1K
# Total Submissions: 716.6K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (l) (without duplicates) and a
# target number (target), find all unique combinations in l where the
# candidate numbers sums to target.
#
# The same repeated number may be chosen from l unlimited number of
# times.
#
# Note:
#
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: l = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: l = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#
#

from typing import List, Dict

class Solution:

    def dfs(self, l, target, index, path, solutions):
        if target == 0:
            return solutions + [path]
        else:
            for i in range(index, len(l)):
                if l[i] > target:
                    break
                solutions = self.dfs(l, target - l[i], i, path + [l[i]], solutions)
            return solutions

    def combinationSum(self, l, target):
        """
        Run a DFS on the sorted l.

        At each step, tries to go down a solution path of taking one element of
        the possible elements and recursing on the remaining target.

        """
        return self.dfs(sorted(l), target, 0, [], [])
