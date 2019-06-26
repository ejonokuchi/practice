#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (26.52%)
# Total Accepted:    446.9K
# Total Submissions: 1.7M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
# Example 2:
#
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#

from typing import List


class Solution:

    def median(self,
        A: List[int],
    ) -> float:
        if len(A) == 0:
            return []
        elif len(A) == 1:
            return A[0]
        else:
            mid = len(A) // 2
            return (A[mid] + A[mid - 1]) / 2 if len(A) % 2 == 0 else A[mid]


    def findMedianSortedArrays(self,
        A: List[int],
        B: List[int],
    ) -> float:
        """
        Returns the median of two sorted arrays in log-time.

        Let A and B be the two input arrays, where A is smaller (or same size).
        Let |A| = n, and |B| = m.

        Imagine the hypothetical array C (of size n + m) that would result from
        a linear-time merge of A and B. The global median is the last and
        largest element of the first half of C (or the average of this and the
        next element, in the case of an even number of elements).

        Let i be the exact number of elements contributed by A to the first
        half of C. If i is known, the number of elements from B is known, and
        because A and B are sorted, the median is also known (the largest of
        the values from A and B).

        We run a binary search for i in the range [0, n]

        Thus, the time-complexity of this algorithm is O(log(n + m)).

        An alternate (and very practical) approach is the below one-liner:
        >>> return self.median(sorted(A + B))  # timsort!

        """
        # Ensure A is smaller
        n, m = len(A), len(B)
        if n > m:
            A, B, n, m = B, A, m, n

        # Empty array cases
        if n == 0:
            return self.median(B)

        # Search for i, the number of elements A contributes to C
        mid_C = (n + m + 1) // 2
        min_i, max_i = 0, n  # i in the range [0, n]

        while min_i <= max_i:
            i = (min_i + max_i) // 2
            j = mid_C - i

            if i < n and A[i] < B[j - 1]:  # i too small
                min_i = i + 1
            elif i > 0 and A[i - 1] > B[j]:  # i too large
                max_i = i - 1
            else:  # i is correct
                if i == 0:
                    left_max = B[j-1]
                elif j == 0:
                    left_max = A[i-1]
                else:
                    left_max = max(A[i - 1], B[j - 1])

                if (n + m) % 2 == 1:
                    return left_max

                if i == n:
                    right_min = B[j]
                elif j == m:
                    right_min = A[i]
                else:
                    right_min = min(A[i], B[j])
                return (left_max + right_min) / 2.0


s = Solution()

def test_findMedianSortedArrays_both_empty():
    l1 = []
    l2 = []
    assert s.findMedianSortedArrays(l1, l2) == []

def test_findMedianSortedArrays_a_empty():
    l1 = []
    l2 = [0, 4, 98]
    assert s.findMedianSortedArrays(l1, l2) == 4

def test_findMedianSortedArrays_b_empty():
    l1 = [0, 4, 98]
    l2 = []
    assert s.findMedianSortedArrays(l1, l2) == 4


def test_findMedianSortedArrays_odd():
    l1 = [0, 4]
    l2 = [15, 18, 44]
    assert s.findMedianSortedArrays(l1, l2) == 15


def test_findMedianSortedArrays_even():
    l1 = [17, 18, 61]
    l2 = [12, 93, 100]
    assert s.findMedianSortedArrays(l1, l2) == 39.5
