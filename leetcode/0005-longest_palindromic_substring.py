#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (31.34%)
# Total Accepted:    1.5M
# Total Submissions: 4.8M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
# Example 3:
#
#
# Input: s = "a"
# Output: "a"
#
#
# Example 4:
#
#
# Input: s = "ac"
# Output: "a"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
#
#


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Computes the length of the longest palindrome centered at each index, and
        returns the substring corresponding to the longest one.

        From each index, checks for repeating characters, and sends two pointers left
        and right until their characters no longer match or the end of the string is
        reached.

        Time  : O(n^2)
        Space : O(1)

        Example
        -------
        Given s = "raceecars"

        idx = 0
        (1) -> base window is from (0, 0): "r"
        (2) -> window expands to: "r"
        (3) -> not longer than current max (base case of first letter)

        ... 1 and 2 are the same

        idx = 3
        (1) -> base window is from (3, 4): "ee"
        (2) -> window expands to: "raceecar"
        (3) -> longer than current max, update longest
        --> this palindrome was centered on "ee", so we can skip idx = 4

        idx = 5
        (1) -> base window is from (5, 5): "c"
        (2) -> window expands to: "c"
        (3) -> not longer than current max

        ... and so on.

        """
        n = len(s)
        a, b, longest = 0, 1, 1
        idx = 0
        while idx < n:
            i = j = idx
            # (1) Find the "base window" including any repeated characters
            while j < n - 1 and s[j + 1] == s[idx]:
                j += 1
            num_repeated = j - idx
            # (2) Expand the window while the next characters match
            while 0 < i and j < n - 1 and s[i - 1] == s[j + 1]:
                i -= 1
                j += 1
            # (3) Compare to the longest palindrome thus far
            if j - i + 1 > longest:
                longest = j - i + 1
                a, b = i, j + 1
            idx = idx + 1 + num_repeated  # no need to check indices of the base window
        return s[a:b]
