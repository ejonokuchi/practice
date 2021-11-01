#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (52.05%)
# Total Accepted:    511.2K
# Total Submissions: 982.1K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
# Example 4:
#
#
# Input: root = [1,2]
# Output: [1,2]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
#
#
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Returns a pre-order string encoding of a tree, with `.` representing None.

        Time  : O(n)
        Space : O(n)

        For example, given tree:
               1
            2
              3

        serialize(root)
        >>> '1 2 . 3 .'
        """
        if root is None:
            return "."
        return " ".join(
            [str(root.val), self.serialize(root.left), self.serialize(root.right)]
        )

    def deserialize(self, data: str) -> TreeNode:
        """Returns the full tree encoded by the serialized string.

        Since the encoding is a full tree including leaf nodes, a greedy, recursive
        pre-order traversal will build the full tree.

        Time  : O(n)
        Space : O(n)
        """

        def deserialize_rec(values):
            val = next(values)
            if val == ".":
                return None
            node = TreeNode(val)
            node.left = deserialize_rec(values)
            node.right = deserialize_rec(values)
            return node

        return deserialize_rec(iter(data.split()))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
