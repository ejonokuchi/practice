#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#
# https://leetcode.com/problems/encode-and-decode-strings/description/
#
# algorithms
# Medium (35.32%)
# Total Accepted:    79.7K
# Total Submissions: 225.7K
# Testcase Example:  '["Hello","World"]'
#
# Design an algorithm to encode a list of strings to a string. The encoded
# string is then sent over the network and is decoded back to the original list
# of strings.
#
# Machine 1 (sender) has the function:
#
#
# string encode(vector<string> strs) {
# ⁠ // ... your code
# ⁠ return encoded_string;
# }
# Machine 2 (receiver) has the function:
#
#
# vector<string> decode(string s) {
# ⁠ //... your code
# ⁠ return strs;
# }
#
#
# So Machine 1 does:
#
#
# string encoded_string = encode(strs);
#
#
# and Machine 2 does:
#
#
# vector<string> strs2 = decode(encoded_string);
#
#
# strs2 in Machine 2 should be the same as strs in Machine 1.
#
# Implement the encode and decode methods.
#
# You are not allowed to solve the problem using any serialize methods (such as
# eval).
#
#
# Example 1:
#
#
# Input: dummy_input = ["Hello","World"]
# Output: ["Hello","World"]
# Explanation:
# Machine 1:
# Codec encoder = new Codec();
# String msg = encoder.encode(strs);
# Machine 1 ---msg---> Machine 2
#
# Machine 2:
# Codec decoder = new Codec();
# String[] strs = decoder.decode(msg);
#
#
# Example 2:
#
#
# Input: dummy_input = [""]
# Output: [""]
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] contains any possible characters out of 256 valid ASCII
# characters.
#
#
#
# Follow up: Could you write a generalized algorithm to work on any possible
# set of characters?
#
#

from typing import List


class Codec:
    """
    Encodings begin with a prefix indicating the length of each string. When decoding,
    the delimiting character is found greedily, and then each substring is extracted
    one by one.

    Alternatively, since we know the input is ASCII-only, we could use join/split with
    a non-ASCII character, like π.

    Example
    -------
    >>> strs = [
        "hello",
        "my",
        "old",
        "friend",
    ]
    >>> encode(strs)
    >>> "5.2.3.6/hellomyoldfriend"

    """

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        return ".".join(f"{len(s)}" for s in strs) + "/" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        idx = s.index("/")
        lengths = map(int, s[:idx].split("."))
        strings = []
        idx += 1
        for n in lengths:
            strings.append(s[idx : idx + n])
            idx += n
        return strings


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
