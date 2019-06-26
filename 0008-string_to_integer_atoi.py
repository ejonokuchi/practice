#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (14.67%)
# Total Accepted:    373.7K
# Total Submissions: 2.5M
# Testcase Example:  '"42"'
#
# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of this
# function.
#
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
#
# Note:
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical
# value is out of the range of representable values, INT_MAX (231 − 1) or
# INT_MIN (−231) is returned.
#
#
# Example 1:
#
# Input: "42"
# Output: 42
#
#
# Example 2:
#
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus
# sign.
# Then take as many numerical digits as possible, which gets 42.
#
#
# Example 3:
#
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a
# numerical digit.
#
#
# Example 4:
#
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a
# numerical
# digit or a +/- sign. Therefore no valid conversion could be performed.
#
# Example 5:
#
#
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed
# integer.
# Thefore INT_MIN (−231) is returned.
#

MAX_INT = (2 ** 31) - 1
MIN_INT = (- MAX_INT) - 1

WHITESPACE = {' ', '\r', '\t', '\n'}
SIGN = {'-', '+'}
DIGITS = {str(x): x for x in range(10)}


class Solution:
    def myAtoi(self, s : str) -> int:
        """
        Converts a string to an integer according to the above rules.

        Does not use int(), regexes, or strip methods.

        """
        n = len(s)
        if n == 0:
            return 0

        i = 0

        # Ignore whitespace
        while i < n and s[i] in WHITESPACE:
            i += 1
        if i == n or s[i] not in SIGN.union(set(DIGITS.keys())):
            return 0

        # Read sign
        positive = s[i] in DIGITS or s[i] == '+'
        if s[i] in SIGN:
            i += 1

        # Read digits, ignore leading zeros
        leading_zero = True
        q = []
        while i < n and s[i] in DIGITS:
            if s[i] == '0':
                if leading_zero:
                    i += 1
                    continue
            else:
                leading_zero = False
            q.append(DIGITS[s[i]])
            i += 1
        if len(q) == 0:
            return 0
        elif len(q) > 10:
            return MAX_INT if positive else MIN_INT

        # Build number
        num = 0
        c = 1
        while len(q) > 0:
            num += (q.pop() * c)
            c *= 10
        return min(num, MAX_INT) if positive else max(-num, MIN_INT)



# TESTING

s = Solution()

def test_atoi_1():
    assert s.myAtoi('42') == 42

def test_atoi_2():
    assert s.myAtoi('   -42') == -42

def test_atoi_3():
    assert s.myAtoi('4193 with words') == 4193

def test_atoi_4():
    assert s.myAtoi('words and -987') == 0

def test_atoi_5():
    assert s.myAtoi('91283472332') == MAX_INT

def test_atoi_5():
    assert s.myAtoi('-91283472332') == MIN_INT
