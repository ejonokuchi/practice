#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (55.66%)
# Total Accepted:    489.2K
# Total Submissions: 878.9K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n'
# + '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are
# various applications of this data structure, such as autocomplete and
# spellchecker.
#
# Implement the Trie class:
#
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie
# (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously
# inserted string word that has the prefix prefix, and false otherwise.
#
#
#
# Example 1:
#
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
#
# Constraints:
#
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and
# startsWith.
#
#
#


class Trie:
    """
    Implements a Trie, or a prefix tree, which supports fast insertion, search, and
    prefix search.

    For speed and clarity, maintains both a Set and a Trie internally. The Trie is
    implemented as a nested dictionary, rather than an actual tree of nodes.

    Space complexity is O(nm), where n is the number of words in the tree and m is the
    length of the words.
    """

    def __init__(self):
        """
        Create the trie and the set.

        Time  : O(1)
        """
        self.D = dict()
        self.S = set()

    def insert(self, word: str) -> None:
        """
        Adds a word to the trie and the set.

        Time  : O(|word|)
        """
        d = self.D
        for x in word:
            if x not in d:
                d[x] = dict()
            d = d[x]
        self.S.add(word)
        return

    def search(self, word: str) -> bool:
        """
        Checks if a word is in the set.

        Time  : O(1)
        """
        return word in self.S

    def startsWith(self, prefix: str) -> bool:
        """
        Checks if a prefix is in the trie.

        Time  : O(|prefix|)
        """
        d = self.D
        for x in prefix:
            if x not in d:
                return False
            d = d[x]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
