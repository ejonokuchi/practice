#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.62%)
# Total Accepted:    477.8K
# Total Submissions: 1.4M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#
#

from typing import List

class Solution:

    def longestCommonPrefix(self,
        strs: List[str]
    ) -> str:
        """
        Returns the length of the longest common prefix.

        Uses the un-'zip' built-in to create sets of characters at each index.

        """
        if len(strs) == 0:
            return ''
        for ix, char_set in enumerate(zip(*strs)):
            if len(set(char_set)) > 1:
                return strs[0][:ix]
        return min(strs, key=len)
