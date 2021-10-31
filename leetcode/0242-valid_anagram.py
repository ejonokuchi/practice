#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (60.15%)
# Total Accepted:    969K
# Total Submissions: 1.6M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Creates a character count dictionary, adding for characters of s and subtracting
        for characters of t. If all counts are equal to 0, the strings are anagrams.

        Time  : O(n)
        Space : O(n)

        Using built-in Counter, this function can reduced to:
        ```
        def isAnagram(self, s: str, t: str) -> bool:
            return len(s) == len(t) and Counter(s) == Counter(t)
        ```
        """
        if len(s) != len(t):
            return False

        counts = defaultdict(int)
        for i in range(len(s)):
            counts[s[i]] += 1
            counts[t[i]] -= 1

        return all(x == 0 for x in counts.values())
