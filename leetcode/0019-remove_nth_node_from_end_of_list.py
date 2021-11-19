#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (37.08%)
# Total Accepted:    1.1M
# Total Submissions: 2.9M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
#
# Example 2:
#
#
# Input: head = [1], n = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
#
# Follow up: Could you do this in one pass?
#
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Maintains two pointers, "slow" and "fast", giving the fast pointer a headstart
        of n, and removing the node after the slow pointer when the fast pointer reaches
        the end of the list.

        If the head is the target node to remove, the fast pointer will be None after
        the headstart.

        Time  : O(n)
        Space : O(1)
        """
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next if slow.next is not None else None
        return head
