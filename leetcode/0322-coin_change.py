#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (38.94%)
# Total Accepted:    777.1K
# Total Submissions: 2M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
# Example 1:
#
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Example 3:
#
#
# Input: coins = [1], amount = 0
# Output: 0
#
#
# Example 4:
#
#
# Input: coins = [1], amount = 1
# Output: 1
#
#
# Example 5:
#
#
# Input: coins = [1], amount = 2
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Unbounded knapsack problem.

        Recursion:  C[i] = 0                if i == 0
                         = -1               if i < c
                         = 1 + C[i - c]     if i >= c

        Where the value of any C[i] is its minimum value over all coins c.

        Time  : O(nc), where n is the amount and c is the number of coins
        Space : O(n)
        """
        # Use infinity as the invalid value instead of -1, so we can use min(C[i]).
        C = [0] + ([float("inf")] * amount)
        for c in coins:
            for i in range(c, amount + 1):
                C[i] = min(C[i], C[i - c] + 1)

        return C[amount] if C[amount] != float("inf") else -1
