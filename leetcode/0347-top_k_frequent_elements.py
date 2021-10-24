#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.65%)
# Total Accepted:    699.3K
# Total Submissions: 1.1M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Counts elements in a dictionary and iterates over the results with a min-heap.

        Time  : O(n log k)
        Space : O(n)

        A simpler, though less interview-friendly implementation is:

        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            return list(zip(*Counter(nums).most_common(k)))[0]
        """
        counts = defaultdict(int)
        for x in nums:
            counts[x] += 1

        top_k = []
        for x, count in counts.items():
            if len(top_k) < k:
                heapq.heappush(top_k, (count, x))
            elif top_k[0][0] < count:
                heapq.heappush(top_k, (count, x))
                heapq.heappop(top_k)

        return list(zip(*top_k))[1]
