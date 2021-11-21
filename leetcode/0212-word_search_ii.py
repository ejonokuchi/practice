#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (38.39%)
# Total Accepted:    365.1K
# Total Submissions: 951.1K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n'
# + '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
#
#
# Example 1:
#
#
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
#
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
#
#
#

from typing import Any, Dict, List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Builds a trie of words, and runs DFS from each position of the board which
        matches an entry at the current sub-trie.

        Given words with significant overlap, e.g. "computer" and "computers", a trie
        enables one search to cover both words, only branching when they differ.

        During each DFS call, the board is modified in-place to track the current path.
        Before returning, the board is reset for any future calls.

        Time  : O(n * m * w * k)
        Space : O(w * k)

        where the board is size (n, m), w is the number of words, and k is the length of
        the longest word.
        """
        n, m = len(board), len(board[0])

        # Construct a trie for efficient prefix searching.
        trie = dict()
        for word in words:
            d = trie
            for char in word:
                if char not in d:
                    d[char] = dict()
                d = d[char]
            d["END"] = word

        found = set()

        def dfs(r: int, c: int, d: Dict[str, Any]):
            """Search for a word via DFS, modifying the grid in-place."""
            if "END" in d:
                found.add(d["END"])
            char = board[r][c]
            board[r][c] = "$"
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < n and 0 <= j < m:
                    if board[i][j] in d:
                        dfs(i, j, d[board[i][j]])
            board[r][c] = char
            return

        # From each location matching a first letter, begin DFS.
        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]])

        return list(found)
