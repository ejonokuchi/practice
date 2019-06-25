#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence
#
# https://leetcode.com/problems/shortest-common-supersequence/description/
#
# algorithms
# Hard (45.79%)
# Total Accepted:    1.7K
# Total Submissions: 3.6K
# Testcase Example:  '"abac"\n"cab"'
#
# Given two strings str1 and str2, return the shortest string that has both
# str1 and str2 as subsequences.  If multiple answers exist, you may return any
# of them.
#
# (A string S is a subsequence of string T if deleting some number of
# characters from T (possibly 0, and the characters are chosen anywhere from T)
# results in the string S.)
#
# Example 1:
#
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation:
# str1 = "abac" is a substring of "cabac" because we can delete the first "c".
# str2 = "cab" is a substring of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these
# properties.
#
#
# Note:
#
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.
#

class Solution:
    def shortestCommonSupersequence(self,
        A : str,
        B : str,
    ) -> str:
        """
        The shortest common supersequence between s1 and s2.

        Finds the LCS, and then adds characters from s1 and s2.

        """
        n, m = len(A), len(B)

        # Find the LCS
        dp = [['' for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + A[i]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
        lcs = dp[n][m]

        # Rebuild the string
        s = ''
        i, j = 0, 0
        for c in lcs:
            while A[i] != c:
                s += A[i]
                i += 1
            while B[j] != c:
                s += B[j]
                j += 1
            s += c
            i += 1
            j += 1
        return s + A[i:] + B[j:]
