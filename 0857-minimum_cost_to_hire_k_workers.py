    #
# @lc app=leetcode id=857 lang=python3
#
# [857] Minimum Cost to Hire K Workers
#
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/
#
# algorithms
# Hard (47.45%)
# Total Accepted:    17.7K
# Total Submissions: 37.3K
# Testcase Example:  '[10,20,5]\n[70,50,30]\n2'
#
# There are N workers.  The i-th worker has a quality[i] and a minimum wage
# expectation wage[i].
#
# Now we want to hire exactly K workers to form a paid group.  When hiring a
# group of K workers, we must pay them according to the following rules:
# - Every worker in the paid group should be paid in the ratio of their quality
# compared to other workers in the paid group.
# - Every worker in the paid group must be paid at least their minimum wage
# expectation.
#
# Return the least amount of money needed to form a paid group satisfying the
# above conditions.
#
#
# Example 1:
#
# Input: quality = [10,20,5], wage = [70,50,30], K = 2
# Output: 105.00000
# Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
#
#
# Example 2:
#
# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
# Output: 30.66667
# Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers
# seperately.
#
#
# Note:
#
# 1 <= K <= N <= 10000, where N = quality.length = wage.length
# 1 <= quality[i] <= 10000
# 1 <= wage[i] <= 10000
# Answers within 10^-5 of the correct answer will be considered correct.
#

import heapq

class Solution:

    def mincostToHireWorkers(self, quality, wage, k):
        """
        Calculates the minimum cost of hiring k workers from a pool of n
        workers.

        The cost of any group of workers is only dependent on two factors:
        • Σq, the sum of the chosen worker's qualities
        • r_max, the highest wage/quality ratio of any chosen worker

        If we begin with the k workers with the lowest possible r_max, then
        any candidate worker, w, would set the new r_max value. Thus, the only
        way to decrease the total cost by adding w is to remove the already
        chosen worker with the highest quality.

        We iterate this way through the n - k remainder of the workers.

        Complexity
        ----------
        Time  : O(n log n)
        Space : O(n)

        """
        # Sort workers by ratio
        workers = sorted((w/q, q, w) for q, w in zip(quality, wage))

        # Create a max heap of worker quality
        chosen = [-q for r, q, w in workers[:k]]
        heapq.heapify(chosen)

        # Swap workers one at a time with the current highest quality worker
        sum_quality = abs(sum(chosen))
        min_cost = workers[k - 1][0] * sum_quality
        for r, q, w in workers[k:]:
            top_q = heapq.heapreplace(chosen, -q)
            sum_quality += top_q + q  # this is a swap, top_q is negative
            min_cost = min(min_cost, r * sum_quality)
        return min_cost
