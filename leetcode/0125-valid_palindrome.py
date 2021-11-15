#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (39.83%)
# Total Accepted:    1M
# Total Submissions: 2.5M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string s, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two pointer solution. Starts from the beginning and end of the input string s,
        checking the next alpha-numeric value at each point until all characters have
        been compared.

        Time  : O(n)
        Space : O(1)

        This can also be solved in one-line with O(n) space as:

        def isPalindrome(self, s: str) -> bool:
            chars = "".join(c for c in s.lower() if c.isalnum())
            return chars == chars[::-1]

        """
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
