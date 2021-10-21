"""
Longest Common Subsequence/Substring
------------------------------------
Given two lists, determine the length of the longest common subsequence between them.

"""


def longest_common_substring(A: str, B: str) -> int:
    """
    Returns the longest common substring. Sequences do not need to be continuous.

    Time  :
    Space :
    """
    pass


def longest_common_continuous_substring(A: str, B: str) -> int:
    """
    Returns the longest common substring. Sequences must be continuous.

    Time  :
    Space :
    """
    pass


def test_lcs_1():
    s1 = "grape"
    s2 = "racecar"
    assert longest_common_substring(s1, s2) == "rae"


def test_lcs_2():
    s1 = "hellothere"
    s2 = "shit"
    assert longest_common_substring(s1, s2) == "ht"


def test_lcs_c_1():
    s1 = "grape"
    s2 = "racecar"
    assert longest_common_continuous_substring(s1, s2) == "ra"


def test_lcs_c_2():
    s1 = "hellothere"
    s2 = "shit"
    assert longest_common_continuous_substring(s1, s2) == "h"

