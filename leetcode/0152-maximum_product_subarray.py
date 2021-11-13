#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (33.60%)
# Total Accepted:    568.6K
# Total Submissions: 1.7M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find a contiguous non-empty subarray within the
# array that has the largest product, and return the product.
#
# It is guaranteed that the answer will fit in a 32-bit integer.
#
# A subarray is a contiguous subsequence of the array.
#
#
# Example 1:
#
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Returns the maximum continuous product with a single pass, maintaining the
        values of the current mininum and maximum, and the global maximum.

        The current min and max are both kept, since negative numbers will increase the
        product as long as they are considered in an even number.

        For any element x in the input array, the current min and max must be one of:
        • the current max * x
        • the current min * x
        • x

        Time  : O(n)
        Space : O(1)
        """
        global_max = nums[0]
        cmin, cmax = nums[0], nums[0]
        for x in nums[1:]:
            current_vals = [x, cmin * x, cmax * x]
            cmin, cmax = min(current_vals), max(current_vals)
            global_max = max(global_max, cmax)
        return global_max
