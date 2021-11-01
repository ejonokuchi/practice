#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (58.83%)
# Total Accepted:    285.8K
# Total Submissions: 485.9K
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
#
#
# For example, "ace" is a subsequence of "abcde".
#
#
# A common subsequence of two strings is a subsequence that is common to both
# strings.
#
#
# Example 1:
#
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
#
# Example 2:
#
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
#
# Example 3:
#
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
#
# Constraints:
#
#
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
#
#
#


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Bottom-up DP approach. Builds a table of values, LCS, such that LCS[i, j] is the
        length of the longest common subsequence between text1[:i] and text2[:j].

        Recursion:
        LCS[i, j] = 1 + LCS[i - 1, j - 1]               if text1[i] == text2[j]
                    max(LCS[i - 1, j], LCS[i, j - 1])   else

        Time  : O(nm)
        Space : O(nm)
        """
        n, m = len(text1), len(text2)
        LCS = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    LCS[i][j] = 1 + LCS[i - 1][j - 1]
                else:
                    LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

        return max(map(max, LCS))
