#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.48%)
# Total Accepted:    1.7M
# Total Submissions: 4.2M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
#
# Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: s = "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: s = "{[]}"
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Checks pairs with a stack of parentheses, ensuring the most recent parenthesis
        is closed by it's matching character. By the end of the string, there should be
        nothing in the stack.

        Time  : O(n)
        Space : O(n)
        """
        matching_char = {")": "(", "]": "[", "}": "{"}
        opened = deque([])
        for c in s:
            if len(opened) == 0 or c in {"(", "[", "{"}:
                opened.append(c)
            elif c in matching_char and opened[-1] == matching_char[c]:
                opened.pop()
            else:
                return False
        return len(opened) == 0
