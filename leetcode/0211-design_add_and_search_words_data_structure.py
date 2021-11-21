#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (42.40%)
# Total Accepted:    325.7K
# Total Submissions: 768.2K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n'
# + '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports adding new words and finding if a
# string matches any previously added string.
#
# Implement the WordDictionary class:
#
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched
# later.
# bool search(word) Returns true if there is any string in the data structure
# that matches word or false otherwise. word may contain dots '.' where dots
# can be matched with any letter.
#
#
#
# Example:
#
#
# Input
#
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
#
# Constraints:
#
#
# 1 <= word.length <= 500
# word in addWord consists lower-case English letters.
# word in search consist of  '.' or lower-case English letters.
# At most 50000 calls will be made to addWord and search.
#
#
#


from collections import deque


class WordDictionary:
    """
    Implements a word dictionary supporting fuzzy matching with a trie.

    Saves words in a nested dictionary with demarcated endings, and searches via DFS.

    Space : O(n*m)

    where n is the number of words, and m is the length of the longest word.
    """

    def __init__(self):
        self.D = dict()

    def addWord(self, word: str) -> None:
        """
        Adds a word to the trie, marking the end with an "END" key.

        Time  : O(n)
        """
        d = self.D
        for char in word:
            if char not in d:
                d[char] = dict()
            d = d[char]
        d["END"] = dict()
        return

    def search(self, word: str) -> bool:
        """
        Searches for the word in the trie via DFS.

        For each character of the word, look for a matching dictionary entry, including
        all existing entries if the character is the "." wildcard. When the end of the
        word is reached, ensure the "END" token is an entry in this sub-tree.

        Time  : O(nm)
        """
        d = self.D
        queue = deque([(word, d)])
        while len(queue) > 0:
            w, d = queue.pop()
            char = w[0]
            if len(w) == 1:
                if (char in d and "END" in d[char]) or (
                    char == "." and any("END" in d[k] for k in d.keys() if k != "END")
                ):
                    return True
            elif char == "." and len(d) > 0:
                queue.extend([(w[1:], d[k]) for k in d])
            elif char in d:
                queue.append((w[1:], d[char]))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
