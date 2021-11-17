#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (53.19%)
# Total Accepted:    1.1M
# Total Submissions: 2.1M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
# the x-axis forms a container, such that the container contains the most
# water.
#
# Notice that you may not slant the container.
#
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
#
#
# Example 2:
#
#
# Input: height = [1,1]
# Output: 1
#
#
# Example 3:
#
#
# Input: height = [4,3,2,1,4]
# Output: 16
#
#
# Example 4:
#
#
# Input: height = [1,2,1]
# Output: 2
#
#
#
# Constraints:
#
#
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
#
#
#

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Greedy two-pointer solution. Starts a window at the ends of the array, and
        slides each end towards the middle until a potentially higher interval is found.

        For a window given by bounds (l, r), the area can only be increased for a
        shorter window (l', r') if the heights of the new bounds are higher. Since the
        area is only determined by the shorter of the two bounds, moving the shorter
        bound will never skip over a better solution.

        At each iteration, choose the pointer from (l, r) with the shorter height, and
        slide it towards the middle until a higher height is found.

        Time  : O(n)
        Space : O(1)
        """
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            max_area = max(max_area, (r - l) * min(height[l], height[r]))
            a, b = l, r
            if height[l] < height[r]:
                while l < r and height[l] <= height[a]:
                    l += 1
            else:
                while l < r and height[r] <= height[b]:
                    r -= 1
        return max_area
