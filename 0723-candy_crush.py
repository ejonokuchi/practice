# @lc app=leetcode id=723 lang=python3

"""
LeetCode Premium only, so I wrote my own tests.

Given an array of integers, return the resulting array from a "Candy Crush"
game, where groups of 3 or more repeated integers are "crushed" and removed,
with any newly combined elements also considered for crushing.

Examples:

>>> l = [1, 2, 2, 2, 3]
>>> crush(l)
[1, 3]

>>> l = [1, 2, 2, 2, 1, 1, 1]
>>> crush(l)
[]

>>> l = [1, 2, 3, 4, 5]
>>> crush(l)
[1, 2, 3, 4, 5]

"""

class Solution:

    def crush(self, l):
        """
        Crush from left to right, using a stack of elements and repeat counts.

        If a repeated item is found, increment the count.
        If a new item is found, remove the repeated elements if there are
        enough. Otherwise, start a new counter for the item.
        At the end of the list, make a final crush if applicable, and translate
        the list back into the input form.

        Complexity
        ----------
        Time  : O(n)
        Space : O(n)

        """
        counts = [{
            'x': l[0],
            'n': 1,
        }]
        i = 1
        while i < len(l):
            # repeated item
            if l[i] == counts[-1]['x']:
                counts[-1]['n'] += 1
            # new item
            else:
                if counts[-1]['n'] > 2:
                    # crush the last sequence and don't increment counter
                    counts.pop()
                    continue
                else:
                    counts.append({
                        'x': l[i],
                        'n': 1,
                    })
            i += 1
        if counts[-1]['n'] > 2:
            counts.pop()
        return [y for sub in [[x['x']] * x['n'] for x in counts] for y in sub]



# Testing

import pytest

s = Solution()

def test_no_crush():
    l = [1, 2, 2, 3, 3, 2]
    assert s.crush(l) == l

def test_1_crush():
    l = [1, 2, 3, 3, 3, 2]
    assert s.crush(l) == [1, 2, 2]

def test_2_crush():
    l = [1, 2, 2, 3, 3, 3, 2]
    assert s.crush(l) == [1]

def test_all_crush():
    l = [1, 3, 3, 3, 3, 1, 2, 2, 2, 1]
    assert s.crush(l) == []
