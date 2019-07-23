#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (36.68%)
# Total Accepted:    187.5K
# Total Submissions: 511.4K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
#
#
#
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def run(self, head, k):
        count = 0
        while head is not None and count < k:
            head = head.next
            count += 1
        return head

    def reverse_sublist(self, prev_tail, head, tail):
        # reverse the sublist
        prev = head
        current = head.next
        # first, point the new tail to the next sublist head
        head.next = tail.next
        while current is not None and prev != tail:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        # point previous sublist tail to the new head
        prev_tail.next = tail
        return prev_tail, tail, head

    def reverseKGroup(self, head, k):
        if k < 2:
            return head
        temp = ListNode(-1)
        head_ = current = runner = head
        runner = self.run(head, k - 1)
        while runner is not None:
            # reverse the sublist
            temp, current, runner = self.reverse_sublist(temp, current, runner)
            if temp.val == -1:
                head_ = current
            # run ahead
            runner = self.run(runner, k)
            current = self.run(current, k)
            temp = self.run(temp, k)
        return head_
