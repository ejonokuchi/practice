#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (63.60%)
# Total Accepted:    333.3K
# Total Submissions: 524.2K
# Testcase Example:  '"abc"'
#
# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.
#
#
# Example 1:
#
#
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
# Example 2:
#
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
#
#
#


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Counts palindromes centered at each index in the string.

        Initialize the count to n, 1 for each length 1 palindrome. For each index, add 1
        for every repeated character in the center, and then expand two pointers to the
        left and right, and add 1 for every valid expansion.

        Time  : O(n^2)
        Space : O(1)
        """
        n = len(s)
        count = n
        for idx in range(n):
            i = j = idx
            while j < n - 1 and s[j + 1] == s[idx]:
                j += 1
                count += 1
            while 0 < i and j < n - 1 and s[i - 1] == s[j + 1]:
                i -= 1
                j += 1
                count += 1
        return count
