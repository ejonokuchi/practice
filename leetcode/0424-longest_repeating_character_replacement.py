#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (49.77%)
# Total Accepted:    147.9K
# Total Submissions: 297.1K
# Testcase Example:  '"ABAB"\n2'
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
#
#
# Example 1:
#
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#
#
# Example 2:
#
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
#
#
#

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Two-pointer approach. Maintains the count of all characters in the current
        window, computing the number of replacements as the difference between the
        window size and the count of the most frequent character in the window.

        The number of unique characters is bound by the encoding used, so the counts
        dictionary never grows larger than a constant, thus finding the max is O(1).

        Time  : O(n)
        Space : O(1)
        """
        window_counts = defaultdict(int)
        max_length = 0
        l = 0
        for r in range(len(s)):
            window_counts[s[r]] += 1
            # (window_size - max_char_count_in_window) > k, means too many replacements
            if r - l + 1 - max(window_counts.values()) > k:
                window_counts[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length
