"""
Longest Common Subsequence/Substring
------------------------------------
Given two lists, determine the length of the longest common subsequence or substring
between them.

"""

from functools import partial


def longest_common_subsequence(A: str, B: str) -> int:
    """
    Returns the longest common subsequence between A and B, where subsequences can be
    non-continuous.

    Bottom-up DP approach. Builds a table of values LCS of size (n + 1, m + 1), such
    that LCS[i, j] is the longest common subsequence between A[:i] and B[:j].

    Recursion:
    LCS[i, j] = LCS[i - 1, j - 1] + A[i - 1]                if A[i] == B[j]
                argmax_len(LCS[i - 1, j], LCS[i, j - 1])    else

    Time  : O(nm)
    Space : O(nm)
    """
    n, m = len(A), len(B)
    LCS = [["" for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                LCS[i][j] = LCS[i - 1][j - 1] + A[i - 1]
            else:
                LCS[i][j] = max((LCS[i - 1][j], LCS[i][j - 1]), key=len)

    return LCS[-1][-1]


def longest_common_substring(A: str, B: str) -> int:
    """
    Returns the longest common substring. Substrings must be continuous subsets of the
    input string.

    Same bottom-up DP approach as the longest common subsequence function, except we
    restrict our search to only continuous sequences, by leaving L[i, j] = 0 for all
    i, j where A[i] != A[j].

    Recursion:
    LCS[i, j] = LCS[i - 1, j - 1] + A[i - 1]    if A[i] == B[j]
                0                               else

    Time  : O(nm)
    Space : O(nm)
    """
    n, m = len(A), len(B)
    LCS = [["" for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                LCS[i][j] = LCS[i - 1][j - 1] + A[i - 1]

    argmax_len = partial(max, key=len)
    return argmax_len(map(argmax_len, LCS))


def test_lc_subsequence_0():
    s1 = ""
    s2 = "racecar"
    assert longest_common_subsequence(s1, s2) == ""


def test_lc_subsequence_1():
    s1 = "grape"
    s2 = "racecar"
    assert longest_common_subsequence(s1, s2) == "rae"


def test_lc_subsequence_2():
    s1 = "hellothere"
    s2 = "shit"
    assert longest_common_subsequence(s1, s2) == "ht"


def test_lc_substring_0():
    s1 = ""
    s2 = "racecar"
    assert longest_common_substring(s1, s2) == ""


def test_lc_substring_1():
    s1 = "grape"
    s2 = "racecar"
    assert longest_common_substring(s1, s2) == "ra"


def test_lc_substring_2():
    s1 = "hellothere"
    s2 = "shit"
    assert longest_common_substring(s1, s2) == "h"

