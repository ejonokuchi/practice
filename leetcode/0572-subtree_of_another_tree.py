#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (44.85%)
# Total Accepted:    373K
# Total Submissions: 831.5K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# Given the roots of two binary trees root and subRoot, return true if there is
# a subtree of root with the same structure and node values of subRoot and
# false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree tree could also be considered as a
# subtree of itself.
#
#
# Example 1:
#
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4
#
#
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Converts each tree to a pre-order string encoding, and checks if the subRoot
        encoding appears anywhere in the root encoding.

        Time  : O(n) avg, O(nm) worst-case
        Space : O(n)

        Notes
        -----
        The naive approach to this question is the following recursive check:
            return (
                isSameTree(tree, sub_tree)
                or isSameTree(tree.left, sub_tree)
                or isSameTree(tree.right, sub_tree)
            )

        A linear time complexity can be guaranteed by either using a linear-time
        substring search algorithm instead of (string in text), or by using a sub-tree
        hashing approach, where sub-tree hashes are cached.
        """
        return self.serialize(subRoot) in self.serialize(root)

    def serialize(self, root: TreeNode) -> str:
        if root is None:
            return "X"
        return "^{}{}{}$".format(
            str(root.val), self.serialize(root.left), self.serialize(root.right),
        )
