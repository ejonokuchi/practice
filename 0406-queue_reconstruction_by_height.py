#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (59.99%)
# Total Accepted:    80.8K
# Total Submissions: 134.8K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# Suppose you have a random list of people standing in a queue. Each person is
# described by a pair of integers (h, k), where h is the height of the person
# and k is the number of people in front of this person who have a height
# greater than or equal to h. Write an algorithm to reconstruct the queue.
#
#
# Note:
# The number of people is less than 1,100.
#
#
#
#
# Example
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
#
#
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:


# # class Person {
# #   int height;
# #   int numberTallerAhead;
# # }

# # Input: List of people, in random order
# # Output: Original order of the list


# def sort_people(people : list) -> list:
# 	"""
#     Sort people by height.

#     """
# 	return sorted(people, key=)


# def get_offset_position(people : list, offset : int) -> int:
#   	"""
#     Return the index of the (n - offset) position of the remaining spaces.

#     """
#     passed_free_spaces = 0
#     for ix, p in enumerate(people[::-1]):
#     	if offset == passed_free_spaces:
#           	return len(people) - ix - 1
#         if p is None:
#         	passed_free_spaces += 1
# 	return 0


# def original_order(people : list) -> list:
# 	"""
#     Outputs the original order of a list based on their height and the number
#     of people that were taller than them in the original list.

#     """
# 	sorted_people = sort_people(people)
#     original_people = [None for _ in range(len(people))]
#     for p in sorted_people:
#     	index = get_offset_position(original_people, p.numberTallerAhead)
#         original_people[index] = p
#     return original_people


