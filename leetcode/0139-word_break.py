#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (43.23%)
# Total Accepted:    892.1K
# Total Submissions: 2.1M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
#
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
#
#

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Bottom-up DP approach. Builds a boolean array B, such that B[i] = True
        indicates the substring s[:i] can be built.

        Recursion: consider a window (l, r) over string s.

        B[r] = True     if B[l] == True and s[l:r] is a word, for any l < r
               False

        where B[0] is initialized to True.

        Time  : O(n^2 + m)
        Space : O(m)

        Some minor optimizations can be made regarding the set of windows (l, r) to
        consider. For example, there is no need to check a window if it is smaller than
        the smallest valid word.
        """
        words = set(wordDict)

        B = [False] * (len(s) + 1)
        B[0] = True
        for r in range(1, len(s) + 1):
            B[r] = any(B[l] and s[l:r] in words for l in range(r))

        return B[-1]
