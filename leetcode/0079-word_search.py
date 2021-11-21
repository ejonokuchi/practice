#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (38.83%)
# Total Accepted:    797K
# Total Submissions: 2.1M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
#
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Searches for the word in the board via DFS.

        Starts a search from every position in the board matching the first character
        of the word. In each search, as characters are matched, the board is modified
        in-place to ensure positions are not used twice. The board is reset if the
        search fails.

        Time  : O(n * m * 3^W)
        Space : O(W), not including the board

        where the board is size (n, m) and W is the length of the word
        """
        n, m = len(board), len(board[0])

        def dfs(r: int, c: int, word_idx: int):
            """Search for a word via DFS, modifying the grid in-place."""
            if word_idx == len(word):
                return True
            char = board[r][c]
            board[r][c] = "$"
            for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= i < n and 0 <= j < m and board[i][j] == word[word_idx]:
                    if dfs(i, j, word_idx + 1):
                        return True
            board[r][c] = char
            return False

        return any(
            dfs(i, j, 1) for i in range(n) for j in range(m) if board[i][j] == word[0]
        )
