"""
Substring Search
----------------
Linear time algorithms for efficient substring search.

"""


def find_substring(S: str, pattern: str) -> int:
    """
    Rabin-Karp algorithm, based on a rolling hash. Returns the index of the pattern in
    the string to search, S. If the pattern is not found, returns -1.

    Slides a rolling hash of size len(pattern) over S, and only evaluates positions
    where the hash value is equal to the hash value of pattern.

    Time  : O(n) avg, O(n^2) worst
    Space : O(1)
    """
    n, m = len(S), len(pattern)
    target = RollingHash(pattern).hash
    window = RollingHash(S[:m])
    for i in range(m, n):
        if window.hash == target and S[i - m : i] == pattern:
            return i - m
        elif i < n:
            window.update(first_char=S[i - m], new_char=S[i])
    return -1


class RollingHash:
    """
    Rolling hash function to compute the hash of a string and update it in linear time.
    """

    def __init__(self, s: str, c: int = 256, p: int = 101):
        self.n = len(s)
        self.c = c
        self.p = p
        self._compute_hash(s)

    def _compute_hash(self, s: str):
        """
        Computes the hash value from the string.

        For string s,
        hash(s) = (ord(s[0]) * c^(n-1) % p) + ... + (ord(s[0]) * c^0 % p)
        """
        self.hash = 0
        for idx, char in enumerate(s):
            self.hash = self.hash + ord(char) * (self.c ** (len(s) - idx - 1)) % self.p
            self.hash %= self.p
        return

    def update(self, first_char: str, new_char: str):
        """
        Updates the hash based on the first character and a new character.

        hash(s[1:] + "a") = (((hash(s) - hash(s[0])) * c) % p + hash[a]) % p
        """
        if self.hash is None:
            raise RuntimeError("No hash has been set!")

        first_char_hash = ord(first_char) * (self.c ** (self.n - 1)) % self.p
        new_char_hash = ord(new_char) % self.p

        self.hash = ((self.hash - first_char_hash) * self.c % self.p) + new_char_hash
        self.hash %= self.p
        return


def test_find_substring_no_match():
    S = "My name is Evan"
    pattern = "hello there"
    assert find_substring(S, pattern) == S.find(pattern)


def test_find_substring_near_match():
    S = "Hello there, my name is Evan"
    pattern = "hello there"
    assert find_substring(S, pattern) == S.find(pattern)


def test_find_substring_one_char():
    S = "My name is Evan"
    pattern = "e"
    assert find_substring(S, pattern) == S.find(pattern)


def test_find_substring_one_match():
    S = "My name is Evan, hello there!"
    pattern = "hello there"
    assert find_substring(S, pattern) == S.find(pattern)


def test_find_substring_two_matches():
    S = "My name is Evan, hello there! Hi. Hello there!"
    pattern = "hello there"
    assert find_substring(S, pattern) == S.find(pattern)
