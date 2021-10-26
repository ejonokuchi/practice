#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (32.34%)
# Total Accepted:    2.6M
# Total Submissions: 8.1M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
# Example 4:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Slides a two pointer window over the string, recording the position of the last
        occurrence of each character. Returns the maximum length of the window.

        When a character is encountered whose last position is in the current window,
        update the left bound of the window.

        Time  : O(n)
        Space : O(n)
        """
        l, r = 0, 0
        max_length = 0
        last_pos = dict()
        for idx, char in enumerate(s):
            if char in last_pos and l <= last_pos[char]:
                l = last_pos[char] + 1
            last_pos[char] = idx
            r = idx
            max_length = max(max_length, r - l + 1)
        return max_length
