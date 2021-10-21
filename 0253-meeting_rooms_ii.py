#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (48.39%)
# Total Accepted:    507.3K
# Total Submissions: 1M
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals intervals where intervals[i] =
# [starti, endi], return the minimum number of conference rooms required.
# 
# 
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^4
# 0 <= starti < endi <= 10^6
# 
# 
#
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
