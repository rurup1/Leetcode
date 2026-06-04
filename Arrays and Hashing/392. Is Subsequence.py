class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Two pointers
        # Continuously increment j, increment i if match
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            # Only increment i if there is a match
            if s[i] == t[j]:
                i += 1

            # Increment j always
            j += 1

        # If we went all the way through i, then there exists a subsequence
        return i == len(s)