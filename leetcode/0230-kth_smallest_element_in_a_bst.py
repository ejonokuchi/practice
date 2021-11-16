#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (64.97%)
# Total Accepted:    623.5K
# Total Submissions: 959.6K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given the root of a binary search tree, and an integer k, return the k^th
# smallest value (1-indexed) of all the values of the nodes in the tree.
#
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
#
#
#
# Follow up: If the BST is modified often (i.e., we can do insert and delete
# operations) and you need to find the kth smallest frequently, how would you
# optimize?
#
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Returns the kth smallest element by traversing the tree depth-first, and
        returning after visiting k nodes.

        From a given node in the tree, traverse left-first until a leaf is reached,
        adding visited nodes to a stack. Then remove the last node from the stack,
        increment the count, and recurse on the right sub-tree of the last parent.

        Time  : O(n)
        Space : O(n)
        """
        nodes, count = deque([]), 0
        node = root
        while True:
            while node is not None:
                nodes.append(node)
                node = node.left
            node = nodes.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right
