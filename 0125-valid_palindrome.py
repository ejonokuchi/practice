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
        
