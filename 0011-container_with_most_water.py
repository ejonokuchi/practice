#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (44.91%)
# Total Accepted:    383.3K
# Total Submissions: 853.4K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
#
#
#
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49.
#
#
#
# Example:
#
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
#
#

from typing import List


class Solution:
    def maxArea(self,
        heights : List[int],
    ) -> int:
        l, r = 0, len(heights) - 1
        max_volume = 0
        while l < r:
            max_volume = max(max_volume, min(heights[l], heights[r]) * (r - l))
            # move in the smaller one
            if heights[l] < heights[r]:
                current = heights[l]
                while heights[l] <= current and l < r:
                    l += 1
            else:
                current = heights[r]
                while heights[r] <= current and l < r:
                    r -= 1
        return max_volume
