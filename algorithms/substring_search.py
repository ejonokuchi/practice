"""
Substring Search
----------------
Linear time algorithms for efficient substring search.

"""


def find_substring_rk(S: str, pattern: str) -> int:
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
        hash(s) = (ord(s[0]) * c^(n-1) % p) + ... + (ord(s[-1]) * c^0 % p)
        """
        self.hash = 0
        for idx, char in enumerate(s):
            self.hash = self.hash + ord(char) * (self.c ** (len(s) - idx - 1)) % self.p
            self.hash %= self.p
        return

    def update(self, first_char: str, new_char: str):
        """
        Updates the hash based on the first character and a new character.

        hash(s[1:] + "a") = (hash(s) - ((hash(s[0]) * c^(n-1)) % p) + hash[a]) % p
        """
        if self.hash is None:
            raise RuntimeError("No hash has been set!")

        first_char_hash = ord(first_char) * (self.c ** (self.n - 1)) % self.p
        new_char_hash = ord(new_char) % self.p

        self.hash = ((self.hash - first_char_hash) * self.c % self.p) + new_char_hash
        self.hash %= self.p
        return


def find_substring_kmp(S: str, pattern: str) -> int:
    """
    Knuth-Morris-Pratt (KMP) algorithm for linear-time substring search.

    Pre-computes a prefix array P for the pattern, where P[i] = x indicates that
    pattern[i] is preceded by a prefix of pattern of length x. When matching the pattern
    against the string S, if a mismatch is found, we can continue matching from the
    length of this prefix.

    For example, given:
              S = "abcacabc"
        pattern = "abcab"
              P =  00012

    From i = 0, there is a near match, but S[4] = c while pattern[4] = b. In the naive
    approach, we restart matching from i = 2. However, in KMP, since the prior prefix
    was 1 (i.e. P[3] = 1), we can continue from i = 4 with the current match set to
    pattern[1]. This results in a single iteration over S.

    Time  : O(n)
    Space : O(m)
    """
    n, m = len(S), len(pattern)

    # Compute prefix table P
    P = [0] * m
    j = 0
    for i in range(1, m):
        while pattern[i] != pattern[j] and j > 0:
            j = P[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            P[i] = j

    # Iterate over S
    j = 0
    for i in range(n):
        if S[i] == pattern[j]:
            if j == m - 1:
                return i - j
            j += 1
        else:
            j = P[j - 1]
            if S[i] == pattern[j]:
                j += 1
    return -1


def test_find_substring_no_match():
    S = "My name is Evan"
    pattern = "hello there"
    assert find_substring_rk(S, pattern) == S.find(pattern)
    assert find_substring_kmp(S, pattern) == S.find(pattern)


def test_find_substring_near_match():
    S = "Hello there, my name is Evan"
    pattern = "hello there"
    assert find_substring_rk(S, pattern) == S.find(pattern)
    assert find_substring_kmp(S, pattern) == S.find(pattern)


def test_find_substring_one_char():
    S = "My name is Evan"
    pattern = "e"
    assert find_substring_rk(S, pattern) == S.find(pattern)
    assert find_substring_kmp(S, pattern) == S.find(pattern)


def test_find_substring_one_match():
    S = "My name is Evan, hello there!"
    pattern = "hello there"
    assert find_substring_rk(S, pattern) == S.find(pattern)
    assert find_substring_kmp(S, pattern) == S.find(pattern)


def test_find_substring_two_matches():
    S = "My name is Evan, hello there! Hi. Hello there!"
    pattern = "hello there"
    assert find_substring_rk(S, pattern) == S.find(pattern)
    assert find_substring_kmp(S, pattern) == S.find(pattern)
