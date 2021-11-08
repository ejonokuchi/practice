#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (49.41%)
# Total Accepted:    377.6K
# Total Submissions: 764.2K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n'
# + '[[],[1],[2],[],[3],[]]'
#
# The median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value and the median is the mean of the two
# middle values.
#
#
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
#
#
# Implement the MedianFinder class:
#
#
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data
# structure.
# double findMedian() returns the median of all elements so far. Answers within
# 10^-5 of the actual answer will be accepted.
#
#
#
# Example 1:
#
#
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
#
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
#
#
#
# Constraints:
#
#
# -10^5 <= num <= 10^5
# There will be at least one element in the data structure before calling
# findMedian.
# At most 5 * 10^4 calls will be made to addNum and findMedian.
#
#
#
# Follow up:
#
#
# If all integer numbers from the stream are in the range [0, 100], how would
# you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how
# would you optimize your solution?
#
#
#

import heapq


class MedianFinder:
    """
    Supports median-finding from a stream of data via a min-heap for values higher than
    the median and a max-heap for values lower than the median.

    To make the median calculation simpler, we maintain the invariant that the length
    of the hi-heap is always >= the length of the lo-heap.

    Space : O(n)

    Note: the follow-up question can be solved in linear time by maintaining an array of
    size 101, where each element represents the count of that integer seen so far. To
    compute the median, traverse the array until half of the total elements have been
    seen.
    """

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        """
        Adds a number to the two internal heaps.

        A push-pop to the hi-heap followed by a push to the lo-heap ensures that the
        two heaps are non-overlapping. Then, we ensure the invariant has not been
        broken, rebalancing the heaps accordingly.

        Time  : O(log n)
        """
        lo, hi = self.heaps
        heapq.heappush(lo, -heapq.heappushpop(hi, num))
        if len(hi) < len(lo):
            heapq.heappush(hi, -heapq.heappop(lo))

    def findMedian(self) -> float:
        """
        Returns the median of the two heaps.

        Time  : O(1)
        """
        lo, hi = self.heaps
        if len(hi) > len(lo):
            return hi[0]
        return (hi[0] - lo[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
