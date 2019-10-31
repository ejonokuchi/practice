#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (41.88%)
# Total Accepted:    224.9K
# Total Submissions: 537K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
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
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
#
#


class Solution:

    def c_sum_rec(self, l, target, i, choices):
        if target == 0:
            return [choices]
        solutions = []
        for ix in range(i, len(l)):
            if l[ix] > target:
                break
            solutions += self.c_sum_rec(l, target - l[ix], i + 1, choices + [l[ix]])
            solutions += self.c_sum_rec(l, target, i + 1, choices)
        return solutions


    def combinationSum2(self, candidates, target):
        return self.c_sum_rec(sorted(candidates), target, 0, [])



import pytest

s = Solution()


def test_combination_sum_2_1():
    candidates = [2, 5, 2, 1, 2]
    target = 5
    solution = [
        [1, 2, 2],
        [5],
    ]
    assert sorted(s.combinationSum2(candidates, target)) == sorted(solution)


def test_combination_sum_2_2():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    solution = [
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6],
    ]
    assert sorted(s.combinationSum2(candidates, target)) == sorted(solution)

