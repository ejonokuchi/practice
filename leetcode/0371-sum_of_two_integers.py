#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (50.70%)
# Total Accepted:    253.5K
# Total Submissions: 500K
# Testcase Example:  '1\n2'
#
# Given two integers a and b, return the sum of the two integers without using
# the operators + and -.
#
#
# Example 1:
# Input: a = 1, b = 2
# Output: 3
# Example 2:
# Input: a = 2, b = 3
# Output: 5
#
#
# Constraints:
#
#
# -1000 <= a, b <= 1000
#
#
#


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Use binary operations to add the numbers.

        If there are no digits where 1s overlap in the binary representation, a XOR (^)
        adds the numbers correctly. With overlapping 1s, we iteratively carry these to
        the left and re-add the carry. This continues until there are no bits to carry.

        Notes
        -----
        Python also requires additional steps due to its variable-length integers.
        (Integers in the range [-5, 256] are pre-allocated, and everything else is a
        variable-length PyLongObject.)

        To handle this, we choose a bit mask size with at least 1 more digit than the
        maximum result of 1000 + 1000 (constraint given), and mask the result of each
        computation. Before returning, we check the most significant digit to determine
        if the number needs to be inverted from its two's complement representation.

        ---

        In C++, the solution can be written recursively as:

        int getSum(int a, int b) {
            return (b == 0) ? a : getSum(a ^ b, (unsigned int) (a & b) << 1);
        }

        where the unsigned cast is required because a left-shift on a negative number
        can be undefined.
        """
        mask = 0xFFFF
        while b != 0:
            sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum
            b = carry

        # Check the most significant bit.
        # Note: we cannot simply use `(a >> 15) & 1` to check the most significant bit,
        # since we may not have masked the value of a (in the case of b == 0).
        if a > 0x7FFF:
            return ~(a ^ mask)
        else:
            return a
