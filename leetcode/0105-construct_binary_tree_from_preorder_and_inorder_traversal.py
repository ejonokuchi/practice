#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (55.33%)
# Total Accepted:    590.6K
# Total Submissions: 1.1M
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
#
#
# Example 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
#
# Example 2:
#
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
#
# Constraints:
#
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
#
#
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Recursively builds the tree specified by the pre-order and in-order traversals.

        At each step, repeat the following:
        1. The root of the current sub-tree is the first pre-order element.
        2. Search for the root in the in-order array. This gives the number of elements
            in each of the left and right sub-trees.
        3. Recursively build the left and right sub-trees.

        To avoid repeated searches on the in-order array, the index of each value in the
        in-order array is pre-computed to a dictionary. We also use indices during
        recursion, rather than creating sub-lists. This sacrifices clarity, but ensures
        the time and space complexity remain linear.

        Time  : O(n)
        Space : O(n)

        Example
        -------
        Given tree t rooted at 3:
                  3
              4      9
            2   1      7

        At the first iteration:

        pre-order = [3  4  2  1  9  7]
                    p1                p2
        in-order  = [2  4  1  3  9  7]
                    i1       idx      i2

        1. The root is 3, at p1.
        2. The root is at in-order location idx, with the size of the sub-trees as:
            • n_left = idx - i1
            • n_right = i2 - 1 - idx
        3. Recurse on each sub-tree.
            • Left:
                • preorder from (p1 + 1) to (p1 + 1 + n_left)
                • inorder from i1 to idx
            • Right:
                • preorder from (p2 - n_right) to p2
                • inorder from (idx + 1) to i2
        """
        n = len(preorder)
        inorder_idxs = {x: idx for idx, x in enumerate(inorder)}

        def build_tree_rec(p1: int, p2: int, i1: int, i2: int) -> TreeNode:
            """Builds the tree specified by preorder[p1:p2] and inorder[i1:i2]."""
            if p2 == p1:
                return None
            root = TreeNode(val=preorder[p1])
            if p2 - p1 == 1:
                return root
            # Find the index of the root in the in-order array.
            idx = inorder_idxs[root.val]
            n_left, n_right = idx - i1, i2 - 1 - idx
            # Recursively build the left and right sub-trees.
            root.left = build_tree_rec(p1=p1 + 1, p2=p1 + 1 + n_left, i1=i1, i2=idx)
            root.right = build_tree_rec(p1=p2 - n_right, p2=p2, i1=idx + 1, i2=i2)
            return root

        return build_tree_rec(p1=0, p2=n, i1=0, i2=n)
