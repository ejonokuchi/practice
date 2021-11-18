#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#
# https://leetcode.com/problems/alien-dictionary/description/
#
# algorithms
# Hard (34.28%)
# Total Accepted:    239.2K
# Total Submissions: 697.7K
# Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
#
# There is a new alien language that uses the English alphabet. However, the
# order among the letters is unknown to you.
#
# You are given a list of strings words from the alien language's dictionary,
# where the strings in words are sorted lexicographically by the rules of this
# new language.
#
# Return a string of the unique letters in the new alien language sorted in
# lexicographically increasing order by the new language's rules. If there is
# no solution, return "". If there are multiple solutions, return any of them.
#
# A string s is lexicographically smaller than a string t if at the first
# letter where they differ, the letter in s comes before the letter in t in the
# alien language. If the first min(s.length, t.length) letters are the same,
# then s is smaller if and only if s.length < t.length.
#
#
# Example 1:
#
#
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
#
#
# Example 2:
#
#
# Input: words = ["z","x"]
# Output: "zx"
#
#
# Example 3:
#
#
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.
#
#
#

from collections import deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Implements Kahn's algorithm to find a valid topological ordering of characters,
        if any such ordering exists.

        Follows two main steps:

        (1) Build a graph G to represent character relationships as an adjacency list.
        For each character c, count its in-degree in the graph.
        • G["a"] = ["b", "c"]   --> a < b, a < c
        • in_degree["c"] = 2    --> "c" has 2 inbound edges, i.e. two edges (_, c)

        (2) Run breadth-first search from every character with an in-degree of 0.
        • When characters are visited, they are added to the solution.
        • After visiting, decrement the in-degree of all its neighbors, and enqueue the
        neighbors whose in-degree is now 0.

        If the graph is a DAG, when BFS exits, the solution will contain all of the
        characters in a valid topological sort.

        Time  : O(nm)
        Space : O(nm)

        where n is the number of words, and m is the length of the longest word.

        Notes
        -----
        To create the edges of the graph, i.e. the pair-wise character orderings,
        every consecutive pair of words in the input is considered, as only consecutive
        words can provide information about character relationships. For example, given:
            words = [
                "cat",
                "car",
                "cap",
                "box",
                "bat",
            ]

        We can use each pair to extract the following edges:

        ("cat", "car") --> edge ("t", "r")
        ("car", "cap") --> edge ("r", "p")
        ("cap", "box") --> edge ("c", "b")
        ("box", "bat") --> edge ("o", "a")

        While the triplet ("cat", "car", "cap") also implies "t" comes before "p", this
        dependency is captured in the graph through the edges ("t", "r") and ("r", "p").
        No other relationships can be deduced.

        """
        # (1) Build the graph and count the in-degrees.
        char_set = set("".join(words))

        G = {char: list() for char in char_set}
        in_degrees = {char: 0 for char in char_set}

        # For every pair of consecutive words, the first diff identifies one edge.
        for word_idx in range(len(words) - 1):
            w1 = words[word_idx]
            w2 = words[word_idx + 1]
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    G[w1[i]].append(w2[i])
                    in_degrees[w2[i]] += 1
                    break
            else:
                # If the words are the same up to n, the shorter one must come first.
                if len(w1) > len(w2):
                    return ""

        # (2) Run BFS to find a topological ordering for the characters.
        # Start from all characters with an in-degree of 0.
        ordered_chars = ""
        queue = deque([char for char, degree in in_degrees.items() if degree == 0])
        while len(queue) != 0:
            char = queue.popleft()
            ordered_chars += char

            for neighbor in G[char]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return ordered_chars if len(ordered_chars) == len(char_set) else ""
