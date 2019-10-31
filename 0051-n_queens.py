#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (39.61%)
# Total Accepted:    143.8K
# Total Submissions: 362.9K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
#
# Example:
#
#
# Input: 4
# Output: [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
#
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.
#
#
#
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:









# # You have N queens. You must place them on an N x N chessboard such that none of the queens can attack each other.
# # Return a list of all the unique solutions.

# # Example: n = 4
# # Input: 4
# # Output: [
# #  [".Q..",  // Solution 1
# #   "...Q",
# #   "Q...",
# #   "..Q."],

# #  ["..Q.",  // Solution 2
# #   "Q...",
# #   "...Q",
# #   ".Q.."]
# # ]
# # where Q is a queen and '.' signifies an empty space on the chessboard.

# def export_board(placed_queens : list) -> list:
#   	board = []
#   	for i in placed_queens:
#     	row = ['.' for _ in range(len(placed_queens))]
# 		row[i] = 'Q'
#         board.append(row)
#     return board

# def valid_placement(row, col, placed_queens):
#   	for ix, queen in enumerate(placed_queens[:row]):
#     	if queen == col or abs(queen - col) == row - ix:
#         	return False
#     return True

# def place_queen(n : int, all_solutions : list, placed_queens : list, row : int):
# 	if row == n:
#       	# valid solution
#     	all_solutions.append(export_board(placed_queens))
# 	else:
#       	for col in range(n):
#           	if valid_placement(row, col, placed_queens):
#               	placed_queens[row] = col
#               	place_queen(n, all_solutions, placed_queens, row + 1)
# 	return

# def place_n_queens(n : int):
# 	"""
#     Outputs: List[List[str]]

# 	"""
#     all_solutions = []
#     place_queen(n, all_solutions, [None for _ in range(n)], 0)
# 	return all_solutions
