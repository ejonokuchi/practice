#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (37.80%)
# Total Accepted:    632K
# Total Submissions: 1.7M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
#
# The testcases will be generated such that the answer is unique.
#
# A substring is a contiguous sequence of characters within the string.
#
#
# Example 1:
#
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
#
#
# Example 2:
#
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
#
# Example 3:
#
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
#
# Constraints:
#
#
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
#
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?
#

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Creates a dictionary of required character counts and slides a window over s,
        updating counts as characters are added and removed.

        Counts can be negative, indicating the window contains an extra copy of a given
        character. When no required characters are missing, the window is valid.

        Time  : O(m + n)
        Space : O(n)
        """
        # Create dictionary of required character counts
        counts = Counter(t)
        num_missing = len(t)

        # Slide a window (l, r) over string s
        start, end = 0, 0
        l, r = 0, -1
        while r < len(s) - 1:
            # Shift right pointer, until the window is valid or the end of s
            while r < len(s) - 1 and num_missing > 0:
                r += 1
                if counts[s[r]] > 0:
                    num_missing -= 1
                counts[s[r]] -= 1
            if num_missing > 0:
                break
            # Shift left pointer, until the leftmost character is required
            while counts[s[l]] < 0:
                counts[s[l]] += 1
                l += 1
            # Update minimum window, if applicable
            if end == 0 or r - l + 1 < end - start:
                start, end = l, r + 1
            # Increment left pointer for next iteration
            num_missing += 1
            counts[s[l]] += 1
            l += 1

        return s[start:end]
