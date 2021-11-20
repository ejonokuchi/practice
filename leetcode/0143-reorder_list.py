#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (43.90%)
# Total Accepted:    375.7K
# Total Submissions: 855.8K
# Testcase Example:  '[1,2,3,4]'
#
# You are given the head of a singly linked-list. The list can be represented
# as:
#
#
# L0 → L1 → … → Ln - 1 → Ln
#
#
# Reorder the list to be on the following form:
#
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
#
# You may not modify the values in the list's nodes. Only nodes themselves may
# be changed.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000
#
#
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from collections import deque
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Splits the list into two halves, reverses the second half, and combines them by
        taking alternating elements from each.

        Time  : O(n)
        Space : O(1)

        Example
        -------
        Given LinkedList: [1 2 3 4 5]

        (1) Two pointers, slow and fast, proceed until the end of the list:
            head = [1 2 3 4 5]
                   sf
            ...
            head = [1 2 3 4 5]
                        s   f

        (2) The sub-list after slow is reversed:
            head = [1 2 3 4 5]
                        s
            s.next = [4 5]
            ...
            head = [1 2 3]
                        s
            prev = [5 4]

        (3) The lists are combined with alternating elements from both:
            list = [1 2 3]
                    h
            insert = [5 4]
                      h
            ...
            list = [1 5 4]
                      h
            insert = [2 3]
                      h
            ...
            list = [1 5 2 4 3]
                            h
            insert = [ ]
                      h
        """
        # (1) Find the middle of the list
        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # (2) Reverse the second half of the list
        prev, node = None, slow.next
        while node is not None:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        slow.next = None

        # (3) Alternate elements from both
        list_head, insert_head = head, prev
        while insert_head is not None:
            next_insert_head = list_head.next
            list_head.next = insert_head
            list_head = insert_head
            insert_head = next_insert_head

        return
