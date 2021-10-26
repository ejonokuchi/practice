#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (58.18%)
# Total Accepted:    1.7M
# Total Submissions: 2.9M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a sorted list. The list should
# be made by splicing together the nodes of the first two lists.
#
#
# Example 1:
#
#
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
#
#
# Input: l1 = [], l2 = []
# Output: []
#
#
# Example 3:
#
#
# Input: l1 = [], l2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.
#
#
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Creates a dummy head for the new list and merges the list by iteratively
        selecting the lesser element of the two lists.

        Time  : O(n)
        Space : O(1)
        """
        dummy = current = ListNode()
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 if l2 is None else l2
        return dummy.next
